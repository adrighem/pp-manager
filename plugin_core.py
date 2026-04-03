import Domoticz
import os
import subprocess
import sys

import urllib
import urllib.request
import urllib.error
import re

import time

import platform

#from urllib2 import urlopen
from datetime import datetime, timedelta



class BasePlugin:
    enabled = False
    pluginState = "Not Ready"
    sessionCookie = ""
    privateKey = b""
    socketOn = "FALSE"

    def __init__(self):
        self.debug = False
        self.error = False
        self.nextpoll = None
        self.pollinterval = 60
        self.ExceptionList = []
        self.SecPolUserList = {}
        self.plugindata = {}
        self.last_update_date = None

    def fetch_registry(self):
        import json
        import urllib.request
        import urllib.error
        import os

        registry_url = "https://raw.githubusercontent.com/adrighem/pp-manager/refs/heads/master/registry.json"
        Domoticz.Debug("Fetching plugin registry from GitHub.")
        try:
            req = urllib.request.Request(registry_url)
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    self.plugindata = json.loads(response.read().decode('utf-8'))
                    Domoticz.Log("Successfully fetched plugin registry from GitHub.")
                else:
                    Domoticz.Error("Failed to fetch registry, status code: " + str(response.status))
        except Exception as e:
            Domoticz.Error("Error fetching registry: " + str(e))
            # Fallback to local file if fetch fails
            local_reg = os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "plugins", "00-PP-MANAGER", "registry.json")
            if os.path.isfile(local_reg):
                with open(local_reg, 'r') as f:
                    self.plugindata = json.load(f)
                Domoticz.Log("Loaded plugin registry from local file.")
            else:
                Domoticz.Error("No local registry found. Plugins cannot be managed.")

    def onStart(self):
        import json
        Domoticz.Debug("onStart called")

        if Parameters["Mode6"] == 'Debug':
            self.debug = True
            Domoticz.Debugging(1)
            DumpConfigToLog()
        else:
            Domoticz.Debugging(0)

        Domoticz.Log("Domoticz Node Name is:" + platform.node())
        Domoticz.Log("Domoticz Platform System is:" + platform.system())
        Domoticz.Debug("Domoticz Platform Release is:" + platform.release())
        Domoticz.Debug("Domoticz Platform Version is:" + platform.version())
        Domoticz.Log("Default Python Version is:" + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) + ".")

        if platform.system() == "Windows":
            Domoticz.Error("Windows Platform NOT YET SUPPORTED!!")
            return
            
        home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
        plugins_dir = os.path.join(home_folder, "plugins")
        
        # Inject shared dependencies into sys.path
        shared_deps_dir = os.path.join(plugins_dir, "00-PP-MANAGER", ".shared_deps")
        if os.path.isdir(shared_deps_dir) and shared_deps_dir not in sys.path:
            sys.path.insert(0, shared_deps_dir)
            Domoticz.Log(f"Injected PP-MANAGER shared dependencies into sys.path: {shared_deps_dir}")

        self.fetch_registry()

        pluginKey = Parameters.get("Mode3", "").strip() or Parameters["Mode2"]
        if pluginKey == "Idle":
            pluginAuthor, pluginRepository, pluginText, pluginBranch = "Idle", "Idle", "Idle", "master"
        elif pluginKey in self.plugindata:
            pluginAuthor = self.plugindata[pluginKey][0]
            pluginRepository = self.plugindata[pluginKey][1]
            pluginText = self.plugindata[pluginKey][2]
            pluginBranch = self.plugindata[pluginKey][3]
        else:
            Domoticz.Error("Selected plugin not found in registry.")
            return

        if Parameters["Mode5"] == 'True':
            Domoticz.Log("Plugin Security Scan is enabled")
            secpoluserFile = os.path.join(plugins_dir, "00-PP-MANAGER", "secpoluser.txt")
            Domoticz.Debug("Checking for SecPolUser file on:" + secpoluserFile)
            if os.path.isfile(secpoluserFile):
                Domoticz.Log("secpoluser file found. Processing!!!")
                with open(secpoluserFile) as secpoluserFileHandle:
                    for line in secpoluserFileHandle:
                        line = line.strip()
                        if line.startswith("--->"):
                            secpoluserSection = line[4:]
                            Domoticz.Log("secpoluser settings found for plugin:" + secpoluserSection)
                        elif line and not line.startswith("--->"):
                            Domoticz.Debug("SecPolUserList exception (" + secpoluserSection + "):'" + line + "'")
                            if secpoluserSection not in self.SecPolUserList:
                                self.SecPolUserList[secpoluserSection] = []
                            self.SecPolUserList[secpoluserSection].append(line)
                Domoticz.Log("SecPolUserList exception:" + str(self.SecPolUserList))
            else:
                self.SecPolUserList = {"Global":[]}
            
            for root, dirs, files in os.walk(plugins_dir):
                for d in dirs:
                    if d:
                        py_file = os.path.join(plugins_dir, d, "plugin.py")
                        if os.path.isfile(py_file):
                            self.parseFileForSecurityIssues(py_file, d)
                break # Only scan depth 1

        exceptionFile = os.path.join(plugins_dir, "00-PP-MANAGER", "exceptions.txt")
        Domoticz.Debug("Checking for Exception file on:" + exceptionFile)
        if os.path.isfile(exceptionFile):
            Domoticz.Log("Exception file found. Processing!!!")
            with open(exceptionFile) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        Domoticz.Log("File ReadLine result:'" + line + "'")
                        self.ExceptionList.append(line)    
        Domoticz.Debug("self.ExceptionList:" + str(self.ExceptionList))

        if Parameters["Mode4"] == 'All':
            Domoticz.Log("Updating All Plugins!!!")
            for root, dirs, files in os.walk(plugins_dir):
                for d in dirs:
                    if d:
                        if d in self.plugindata:
                            self.UpdatePythonPlugin(self.plugindata[d][0], self.plugindata[d][1], d)
                        elif d == "00-PP-MANAGER":
                            Domoticz.Debug("PP-Manager Folder found. Skipping!!")      
                        else:
                            Domoticz.Log("Plugin:" + d + " cannot be managed with PP-Manager!!.")      
                break

        if Parameters["Mode4"] == 'AllNotify':
            Domoticz.Log("Collecting Updates for All Plugins!!!")
            for root, dirs, files in os.walk(plugins_dir):
                for d in dirs:
                    if d:
                        if d in self.plugindata:
                            self.CheckForUpdatePythonPlugin(self.plugindata[d][0], self.plugindata[d][1], d)
                        elif d == "00-PP-MANAGER":
                            Domoticz.Debug("PP-Manager Folder found. Skipping!!")      
                        else:
                            Domoticz.Log("Plugin:" + d + " cannot be managed with PP-Manager!!.")      
                break

        if Parameters["Mode4"] == 'SelectedNotify': 
            Domoticz.Log("Collecting Updates for Plugin:" + pluginKey)
            if pluginKey in self.plugindata:
                self.CheckForUpdatePythonPlugin(pluginAuthor, pluginRepository, pluginKey)

        if pluginKey == "Idle":
            Domoticz.Log("Plugin Idle")
            Domoticz.Heartbeat(60)
        else:
            plugin_target_dir = os.path.join(plugins_dir, pluginKey)
            Domoticz.Debug("Checking for dir:" + plugin_target_dir)
            if os.path.isdir(plugin_target_dir):
                Domoticz.Debug("Folder for Plugin:" + pluginKey + " already exists!!!")
                if Parameters["Mode4"] == 'Selected':
                    Domoticz.Debug("Updating Enabled for Plugin:" + pluginText + ".Checking For Update!!!")
                    self.UpdatePythonPlugin(pluginAuthor, pluginRepository, pluginKey)
                Domoticz.Heartbeat(60)
            else:
                Domoticz.Log("Installation requested for Plugin:" + pluginText)
                Domoticz.Debug("Installation URL is: https://github.com/" + pluginAuthor + "/" + pluginRepository)
                Domoticz.Debug("Current Working dir is:" + plugins_dir)
                if pluginKey in self.plugindata:
                    Domoticz.Log("Plugin Display Name:" + pluginText)
                    Domoticz.Log("Plugin Author:" + pluginAuthor)
                    Domoticz.Log("Plugin Repository:" + pluginRepository)
                    Domoticz.Log("Plugin Key:" + pluginKey)
                    Domoticz.Log("Plugin Branch:" + pluginBranch)
                    self.InstallPythonPlugin(pluginAuthor, pluginRepository, pluginKey, pluginBranch)
                Domoticz.Heartbeat(60)

    def onStop(self):
        Domoticz.Debug("onStop called")
        Domoticz.Log("Plugin is stopping.")
        self.UpdatePythonPlugin("adrighem", "pp-manager", "00-PP-MANAGER")
        Domoticz.Debugging(0)

    def onHeartbeat(self):
        from datetime import datetime
        Domoticz.Debug("onHeartbeat called")
        pluginKey = Parameters.get("Mode3", "").strip() or Parameters["Mode2"]

        now = datetime.now()
        Domoticz.Debug(f"Current time: {now.strftime('%H:%M')}")

        if now.hour >= 12 and (self.last_update_date is None or self.last_update_date < now.date()):
            Domoticz.Log("Its time!!. Trigering Actions!!!")
            self.last_update_date = now.date()
            
            home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
            plugins_dir = os.path.join(home_folder, "plugins")

            if Parameters["Mode4"] == 'All':
                Domoticz.Log("Checking Updates for All Plugins!!!")
                for root, dirs, files in os.walk(plugins_dir):
                    for d in dirs:
                        if d:
                            if d in self.plugindata:
                                self.UpdatePythonPlugin(self.plugindata[d][0], self.plugindata[d][1], d)
                            elif d == "00-PP-MANAGER":
                                Domoticz.Debug("PP-Manager Folder found. Skipping!!")      
                            else:
                                Domoticz.Log("Plugin:" + d + " cannot be managed with PP-Manager!!.")      
                    break

            if Parameters["Mode4"] == 'AllNotify':
                Domoticz.Log("Collecting Updates for All Plugins!!!")
                for root, dirs, files in os.walk(plugins_dir):
                    for d in dirs:
                        if d:
                            if d in self.plugindata:
                                self.CheckForUpdatePythonPlugin(self.plugindata[d][0], self.plugindata[d][1], d)
                            elif d == "00-PP-MANAGER":
                                Domoticz.Debug("PP-Manager Folder found. Skipping!!")      
                            else:
                                Domoticz.Log("Plugin:" + d + " cannot be managed with PP-Manager!!.")      
                    break

            if Parameters["Mode4"] == 'SelectedNotify':
                Domoticz.Log("Collecting Updates for Plugin:" + pluginKey)
                if pluginKey in self.plugindata:
                    self.CheckForUpdatePythonPlugin(self.plugindata[pluginKey][0], self.plugindata[pluginKey][1], pluginKey)
                else:
                    Domoticz.Log("Plugin:" + pluginKey + " not found in plugindata. Skipping update check.")

            if Parameters["Mode4"] == 'Selected' and pluginKey in self.plugindata:
                Domoticz.Log("Checking Updates for Plugin:" + self.plugindata[pluginKey][2])
                self.UpdatePythonPlugin(self.plugindata[pluginKey][0], self.plugindata[pluginKey][1], pluginKey)

    def InstallPythonPlugin(self, ppAuthor, ppRepository, ppKey, ppBranch):
        Domoticz.Debug("InstallPythonPlugin called")
        
        home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
        plugins_dir = os.path.join(home_folder, "plugins")

        Domoticz.Log("Installing Plugin:" + self.plugindata[ppKey][2])
        ppCloneCmd = ["git", "clone", "-b", ppBranch, f"https://github.com/{ppAuthor}/{ppRepository}.git", ppKey]
        Domoticz.Log("Calling: " + " ".join(ppCloneCmd))
        
        env = os.environ.copy()
        env['LANG'] = 'en_US.UTF-8'
        env['LC_ALL'] = 'en_US.UTF-8'
        
        try:
            pr = subprocess.Popen(ppCloneCmd, cwd=plugins_dir, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out, error = pr.communicate()
            if out:
                Domoticz.Log("Succesfully installed: " + out.strip())
                Domoticz.Log("---Restarting Domoticz MAY BE REQUIRED to activate new plugins---")
            if error:
                Domoticz.Debug("Git Error: " + error.strip())
                if "Cloning into" in error:
                   Domoticz.Log("Plugin " + ppKey + " installed Succesfully")
        except OSError as e:
            Domoticz.Error("Git ErrorNo:" + str(e.errno))
            Domoticz.Error("Git StrError:" + str(e.strerror))

        self.installDependencies(ppKey)
        return None

    def UpdatePythonPlugin(self, ppAuthor, ppRepository, ppKey):
        Domoticz.Debug("UpdatePythonPlugin called")
        
        home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
        plugin_dir = os.path.join(home_folder, "plugins", ppKey)

        if ppKey == "00-PP-MANAGER":
            Domoticz.Log("Self Update Initiated")
        elif (ppKey in self.plugindata and self.plugindata[ppKey][2] in self.ExceptionList):
            Domoticz.Log("Plugin:" + self.plugindata[ppKey][2] + " excluded by Exclusion file (exclusion.txt). Skipping!!!")
            return
            
        Domoticz.Log("Resetting and Updating Plugin:" + ppKey)
        env = os.environ.copy()
        env['LANG'] = 'en_US.UTF-8'
        env['LC_ALL'] = 'en_US.UTF-8'

        ppGitReset = ["git", "reset", "--hard", "HEAD"]
        try:
            res_reset = subprocess.run(ppGitReset, cwd=plugin_dir, env=env, capture_output=True, text=True)
            if res_reset.stdout:
                Domoticz.Debug("Git Reset Response:" + res_reset.stdout)
            if res_reset.stderr:
                Domoticz.Debug("Git Reset Error:" + res_reset.stderr.strip())
        except OSError as eReset:
            Domoticz.Error("Git ErrorNo:" + str(eReset.errno))
            Domoticz.Error("Git StrError:" + str(eReset.strerror))

        ppUrl = ["git", "pull", "--force"]
        Domoticz.Debug("Calling: " + " ".join(ppUrl) + " on folder " + plugin_dir)
        
        try:
            res = subprocess.run(ppUrl, cwd=plugin_dir, env=env, capture_output=True, text=True)
            out = res.stdout
            error = res.stderr
            if out:
                Domoticz.Debug("Git Response:" + out)
                if "Already up to date" in out or "Already up-to-date" in out:
                   Domoticz.Log("Plugin " + ppKey + " already Up-To-Date")
                elif "Updating" in out and "error" not in out.lower():
                   Domoticz.Log("Succesfully pulled gitHub update for plugin " + ppKey)
                   Domoticz.Log("---Restarting Domoticz MAY BE REQUIRED to activate new plugins---")
                else:
                   Domoticz.Error("Something went wrong with update of " + str(ppKey))
            if error:
                Domoticz.Debug("Git Error:" + error.strip())
                if "Not a git repository" in error:
                   Domoticz.Log("Plugin:" + ppKey + " is not installed from gitHub. Cannot be updated with PP-Manager!!.")
        except OSError as e:
            Domoticz.Error("Git ErrorNo:" + str(e.errno))
            Domoticz.Error("Git StrError:" + str(e.strerror))

        self.installDependencies(ppKey)
        return None

    def CheckForUpdatePythonPlugin(self, ppAuthor, ppRepository, ppKey):
        Domoticz.Debug("CheckForUpdatePythonPlugin called")

        if ppKey in self.plugindata and self.plugindata[ppKey][2] in self.ExceptionList:
            Domoticz.Log("Plugin:" + self.plugindata[ppKey][2] + " excluded by Exclusion file (exclusion.txt). Skipping!!!")
            return

        Domoticz.Debug("Checking Plugin:" + ppKey + " for updates")
        
        home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
        plugin_dir = os.path.join(home_folder, "plugins", ppKey)
        
        env = os.environ.copy()
        env['LANG'] = 'en_US.UTF-8'
        env['LC_ALL'] = 'en_US.UTF-8'

        ppGitFetch = ["git", "fetch"]
        try:
            prFetch = subprocess.Popen(ppGitFetch, cwd=plugin_dir, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            outFetch, errorFetch = prFetch.communicate()
            if outFetch:
                Domoticz.Debug("Git Response:" + outFetch)
            if errorFetch:
                Domoticz.Debug("Git Error:" + errorFetch.strip())
        except OSError as eFetch:
            Domoticz.Error("Git ErrorNo:" + str(eFetch.errno))
            Domoticz.Error("Git StrError:" + str(eFetch.strerror))

        ppUrl = ["git", "status", "-uno"]
        Domoticz.Debug("Calling: " + " ".join(ppUrl) + " on folder " + plugin_dir)

        try:
            pr = subprocess.Popen(ppUrl, cwd=plugin_dir, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out, error = pr.communicate()
            if out:
                Domoticz.Debug("Git Response:" + out)
                if "up to date" in out or "up-to-date" in out:
                   Domoticz.Log("Plugin " + ppKey + " already Up-To-Date")
                elif "Your branch is behind" in out and "error" not in out.lower():
                   Domoticz.Log("Found that we are behind on plugin " + ppKey)
                   self.fnSelectedNotify(ppKey)
                elif "Your branch is ahead" in out and "error" not in out.lower():
                   Domoticz.Debug("Found that we are ahead on plugin " + ppKey + ". No need for update")
                else:
                   Domoticz.Error("Something went wrong with update of " + str(ppKey))
            if error:
                Domoticz.Debug("Git Error:" + error.strip())
                if "Not a git repository" in error:
                   Domoticz.Log("Plugin:" + ppKey + " is not installed from gitHub. Ignoring!!.")
        except OSError as e:
            Domoticz.Error("Git ErrorNo:" + str(e.errno))
            Domoticz.Error("Git StrError:" + str(e.strerror))

        return None

    def fnSelectedNotify(self, pluginKey):
        import urllib.request
        import urllib.parse
        import urllib.error
        Domoticz.Debug("fnSelectedNotify called")
        Domoticz.Log("Preparing Notification")
        domoticz_port = Parameters.get("Mode1", "8080")
        ServerURL = f"http://127.0.0.1:{domoticz_port}/json.htm?param=sendnotification&type=command"
        pluginName = self.plugindata[pluginKey][2] if pluginKey in self.plugindata else pluginKey
        MailSubject = urllib.parse.quote(platform.node() + ":Domoticz Plugin Updates Available for " + pluginName)
        MailBody = urllib.parse.quote(pluginName + " has updates available!!")
        MailDetailsURL = "&subject=" + MailSubject + "&body=" + MailBody + "&subsystem=email"
        notificationURL = ServerURL + MailDetailsURL
        Domoticz.Debug("ConstructedURL is:" + notificationURL)
        try:
            response = urllib.request.urlopen(notificationURL, timeout=2).read()
        except urllib.error.URLError as err1:
            Domoticz.Error("HTTP Request error: " + str(err1) + " URL: " + notificationURL)
        except Exception as e:
            Domoticz.Error("Unexpected Error notifying: " + str(e))
            
        Domoticz.Debug("Notification URL is :" + str(notificationURL))
        return None

    def parseIntValue(self, s):
        Domoticz.Debug("parseIntValue called")
        try:
            return int(s)
        except:
            return None

    def parseFileForSecurityIssues(self, pyfilename, pypluginid):
        Domoticz.Debug("parseFileForSecurityIssues called")
        if Parameters["Mode5"] == 'Monitor':
            Domoticz.Log("Plugin Security Scan is enabled")

        ips = {}
        if pypluginid not in self.SecPolUserList:
            self.SecPolUserList[pypluginid] = []

        try:
            with open(pyfilename, "r") as file:
                for lineNum, text in enumerate(file, 1):
                    text = text.rstrip()
                    regexFound = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', text)
                    paramFound = re.findall(r'<param field=', text)
                    
                    if regexFound and not paramFound:
                        for rex in regexFound:
                            clean_text = text.strip()
                            if (clean_text not in self.SecPolUserList.get("Global", []) and 
                                clean_text not in self.SecPolUserList[pypluginid] and 
                                clean_text != "" and 
                                not text.startswith("#")):
                                Domoticz.Error(f"Security Finding(IP):-->{clean_text}<-- LINE: {lineNum} FILE:{pyfilename}")
                                ips[f"IP{lineNum}"] = (rex, "IP Address")
            Domoticz.Debug("IPS Table contents are:" + str(ips))
        except Exception as e:
            Domoticz.Error(f"Error parsing security issues for {pyfilename}: {str(e)}")

    def installDependencies(self, pluginKey):
        Domoticz.Debug("installDependencies called")
        home_folder = Parameters.get("HomeFolder", str(os.getcwd()) + "/")
        plugin_dir = os.path.join(home_folder, "plugins", pluginKey)
        requirementsFile = os.path.join(plugin_dir, "requirements.txt")
        shared_deps_dir = os.path.join(home_folder, "plugins", "00-PP-MANAGER", ".shared_deps")

        if os.path.isfile(requirementsFile):
            Domoticz.Log("requirements.txt found for plugin: " + pluginKey)
            os.makedirs(shared_deps_dir, exist_ok=True)
            
            # Using 'uv' instead of 'sudo pip3' for fast, non-sudo, dependency resolution
            installCmd = ["uv", "pip", "install", "-r", requirementsFile, "--target", shared_deps_dir]
            Domoticz.Log("Installing dependencies using: " + " ".join(installCmd))
            try:
                pr = subprocess.Popen(installCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                out, error = pr.communicate()
                if pr.returncode == 0:
                    Domoticz.Log("Dependencies installed successfully: " + out.strip())
                else:
                    Domoticz.Error("Error installing dependencies (Check if 'uv' is installed): " + error.strip())
            except OSError as e:
                Domoticz.Error("OS Error running 'uv' (Is it installed?): " + str(e))
        else:
            Domoticz.Log("No requirements.txt found for plugin: " + pluginKey)
        return None

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
    return
