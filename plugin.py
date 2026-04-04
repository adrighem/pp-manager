# pp-manager - PythonPlugin Manager
#
# Author: adrighem, 2018
#
#  Since (2018-02-23): Initial Version
#


"""
<plugin key="PP-MANAGER" name="Python Plugin Manager" author="adrighem" version="1.5.47" externallink="https://www.domoticz.com/forum/viewtopic.php?f=65&t=22339">
    <description>
		<h2>Python Plugin Manager 1.5.47</h2><br/>
		<h3>Features</h3>
		<ul style="list-style-type:square">
			<li>Install plugins</li>
			<li>Update All/Selected plugins</li>
			<li>Update Notification for All/Selected</li>
		</ul>
		<h3>----------------------------------------------------------------------</h3>
		<h3>WARNING:</h3>
		<h2>         Auto Updating plugins without verifying their code</h2>
		<h2>         makes you system vulnerable to developer's code intensions!!</h2>
		<h3>----------------------------------------------------------------------</h3>
		<h2>NOTE: After selecting your options press "Update" button!!</h2>
    </description>
     <params>
        <param field="Mode2" label="Plugin to install" width="200px">
            <options>
                <option label="Idle" value="Idle"  default="true" />
                <option label="Battery monitoring for Z-Wave nodes" value="BatteryLevel"/>
                <option label="Buienradar.nl (Weather lookup)" value="Buienradar"/>
                <option label="Chromecast plugin for Domoticz" value="ChromecastPlugin"/>
                <option label="Creasol DomBus RS485 I/O/Sens modules" value="CreasolDomBus"/>
                <option label="Crow Runner Alarm" value="AAPIPModule"/>
                <option label="DDS238 ZN/S energy meter, single phase, Modbus RTU" value="domoticz-dds238"/>
                <option label="deCONZ bridge (For Conbee,Raspbee)" value="deCONZ"/>
                <option label="Denon/Marantz Amplifier" value="Denon4306"/>
                <option label="Domoticz Theme Manager" value="domoticz-theme-manager"/>
                <option label="DS238-2 ZN/S ModbusTCP" value="ds238-modbus-tcp"/>
                <option label="DTS238 ZN/S energy meter, three phase, Modbus RTU" value="domoticz-dts238"/>
                <option label="Dummy Plugin" value="Dummy_Plugin"/>
                <option label="Dyson Pure Link" value="DysonPureLink"/>
                <option label="E-Flux by Road back office" value="E-Flux"/>
                <option label="ebusd bridge" value="ebusd"/>
                <option label="Emmeti EQ 2021 amd EQ 3021 ES hot water heat pumps" value="domoticz-emmeti-eq2021"/>
                <option label="Emmeti Mirai heat pumps" value="domoticz-emmeti-mirai"/>
                <option label="EMS bus Wi-Fi Gateway" value="ems-gateway"/>
                <option label="eQ-3 MAX! Cube" value="eq3max"/>
                <option label="EVCC IO Plugin" value="Domoticz-EVCC-IO-Plugin"/>
                <option label="Freebox V6 (Revolution)" value="freeboxv6"/>
                <option label="Global Cache 100" value="GC-100"/>
                <option label="GoodWE Solar inverter via SEMS API" value="GoodWeAPI"/>
                <option label="Govee Local Api Control" value="GoveeDiscovery"/>
                <option label="Hisense AC (AEH-W4A1)" value="aeh-w4a1"/>
                <option label="Hive Plugin" value="HivePlug"/>
                <option label="Homewizard" value="Homewizard"/>
                <option label="Homewizard Battery" value="Homewizard-Battery"/>
                <option label="Hyundai and Kia vehicles" value="HyundaiKiaConnect"/>
                <option label="iDetect Presence Detection" value="iDetect"/>
                <option label="IKEA Tradfri" value="IKEA-Tradfri"/>
                <option label="Integrate with AWTRIX3 Smart Clock" value="AWTRIX3"/>
                <option label="Itho Wifi module" value="IthoWifi"/>
                <option label="Link-Tap Watering System" value="Link-Tap"/>
                <option label="Linky" value="Linky"/>
                <option label="Meteo Alarm EU RSS Reader" value="MeteoAlarmEU"/>
                <option label="Mikrotik RouterOS" value="mikrotik-routeros"/>
                <option label="Moon Phases" value="MoonPhases"/>
                <option label="MQTT discovery" value="MQTTDiscovery"/>
                <option label="Onkyo AV Receiver" value="Onkyo"/>
                <option label="OpenWRT WiFi Presence MQTT translator" value="owrtwifi2domo"/>
                <option label="PZEM-016 PZEM-014 PZEM-004T energy meters" value="pzem016"/>
                <option label="Quatt" value="Quatt"/>
                <option label="RAVEn Zigbee energy monitor" value="RAVEn"/>
                <option label="RTL_433 MQTT receiver" value="pyrtl433"/>
                <option label="Shelly MQTT translator" value="Shelly_MQTT"/>
                <option label="SmogTok Air Quality monitor" value="SmogTok"/>
                <option label="SNMP Reader" value="SNMPreader"/>
                <option label="Sonoff Mini" value="sonoff-domoticz-plugin"/>
                <option label="Sonos Players" value="Sonos"/>
                <option label="Sony Bravia TV (with Kodi remote)" value="sony"/>
                <option label="Steam player status" value="steam"/>
                <option label="Synology SurveillanceStation" value="Synology SurveillanceStation"/>
                <option label="SYSFS-Switches" value="SYSFS-Switches"/>
                <option label="Tuya" value="tuyaha"/>
                <option label="UPS Monitor" value="NUT_UPS"/>
                <option label="Wan IP Checker" value="WAN-IP-CHECKER"/>
                <option label="WLANThermo" value="WLANThermo"/>
                <option label="WLED" value="WLED"/>
                <option label="Xiaomi Mi Flower Mate" value="Mi_Flower_mate_plugin"/>
                <option label="Xiaomi Mi Robot Vacuum" value="xiaomi-mi-robot-vacuum"/>
                <option label="Yamaha AV Receiver" value="YamahaPlug"/>
                <option label="Yi Hack" value="YiHack"/>
                <option label="Zigate plugin" value="Zigate"/>
                <option label="Zigbee2Mqtt" value="Zigbee2Mqtt"/>
            </options>
        </param>
        <param field="Mode3" label="Custom Plugin ID (from registry)" width="200px" default=""/>
        <param field="Mode4" label="Auto Update" width="175px">
            <options>
                <option label="All" value="All"/>
                <option label="All (NotifyOnly)" value="AllNotify" default="true"/>
                <option label="Selected" value="Selected"/>
                <option label="Selected (NotifyOnly)" value="SelectedNotify"/>
                <option label="None" value="None"/>
            </options>
        </param>
         <param field="Mode5" label="Security Scan (Experimental)" width="75px">
            <options>
                <option label="True" value="True"/>
                <option label="False" value="False"  default="true" />
            </options>
        </param>
         <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>
"""

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
            local_reg = os.path.join(os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", "..")), "plugins", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), "registry.json")
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
            
        home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
        plugins_dir = os.path.join(home_folder, "plugins")
        
        current_folder = os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/')))
        if not current_folder.startswith("00-"):
            warn_msg = f"PP-MANAGER is in '{current_folder}'. It is strongly advised to rename the folder to start with '00-' (e.g., '00-PP-MANAGER') so it loads first."
            Domoticz.Error(warn_msg)
            Domoticz.SendNotification("PP-MANAGER Setup Warning", warn_msg)

        # Inject shared dependencies into sys.path
        shared_deps_dir = os.path.join(plugins_dir, os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), ".shared_deps")
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
            secpoluserFile = os.path.join(plugins_dir, os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), "secpoluser.txt")
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

        exceptionFile = os.path.join(plugins_dir, os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), "exceptions.txt")
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
                        elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
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
                        elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
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
        self.UpdatePythonPlugin("adrighem", "pp-manager", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))))
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
            
            home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
            plugins_dir = os.path.join(home_folder, "plugins")

            if Parameters["Mode4"] == 'All':
                Domoticz.Log("Checking Updates for All Plugins!!!")
                for root, dirs, files in os.walk(plugins_dir):
                    for d in dirs:
                        if d:
                            if d in self.plugindata:
                                self.UpdatePythonPlugin(self.plugindata[d][0], self.plugindata[d][1], d)
                            elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
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
                            elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
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
        
        home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
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
        
        home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
        plugin_dir = os.path.join(home_folder, "plugins", ppKey)

        if ppKey == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
            Domoticz.Log("Self Update Initiated but disabled to preserve local fixes.")
            return None
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
        
        home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
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
        Domoticz.Debug("fnSelectedNotify called")
        Domoticz.Log("Preparing Notification")
        pluginName = self.plugindata[pluginKey][2] if pluginKey in self.plugindata else pluginKey
        MailSubject = platform.node() + ": Domoticz Plugin Updates Available for " + pluginName
        MailBody = pluginName + " has updates available!!"
        Domoticz.SendNotification(MailSubject, MailBody)
        Domoticz.Debug("Notification sent natively.")
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
        home_folder = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", ".."))
        plugin_dir = os.path.join(home_folder, "plugins", pluginKey)
        requirementsFile = os.path.join(plugin_dir, "requirements.txt")
        shared_deps_dir = os.path.join(home_folder, "plugins", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), ".shared_deps")

        def check_cmd(cmd):
            try:
                subprocess.run([cmd, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            except:
                return False

        if os.path.isfile(requirementsFile):
            Domoticz.Log("requirements.txt found for plugin: " + pluginKey)
            os.makedirs(shared_deps_dir, exist_ok=True)
            
            # Check for 'uv' then 'pip' as fallbacks
            installCmd = None
            if check_cmd("uv"):
                installCmd = ["uv", "pip", "install", "-r", requirementsFile, "--target", shared_deps_dir]
            elif check_cmd("pip3"):
                installCmd = ["pip3", "install", "-r", requirementsFile, "--target", shared_deps_dir]
            elif check_cmd("pip"):
                installCmd = ["pip", "install", "-r", requirementsFile, "--target", shared_deps_dir]
            
            if installCmd:
                Domoticz.Log("Installing dependencies using: " + " ".join(installCmd))
                try:
                    pr = subprocess.Popen(installCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    out, error = pr.communicate()
                    if pr.returncode == 0:
                        Domoticz.Log("Dependencies installed successfully: " + out.strip())
                    else:
                        Domoticz.Error("Error installing dependencies: " + error.strip())
                except Exception as e:
                    Domoticz.Error("Error running installation command: " + str(e))
            else:
                Domoticz.Log("Neither 'uv' nor 'pip' found. Skipping automatic dependency installation.")
                Domoticz.Log(f"Please install dependencies manually from {requirementsFile} into {shared_deps_dir}")
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
