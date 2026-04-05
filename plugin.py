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
                <option label="Broadlink devices" value="Broadlink-Domoticz-plugin"/>
                <option label="Chromecast plugin for Domoticz" value="ChromecastPlugin"/>
                <option label="Creasol DomBus RS485 I/O/Sens modules" value="CreasolDomBus"/>
                <option label="DDS238 ZN/S energy meter, single phase, Modbus RTU" value="domoticz-dds238"/>
                <option label="deCONZ bridge (For Conbee,Raspbee)" value="deCONZ"/>
                <option label="Denon/Marantz Amplifier" value="Denon4306"/>
                <option label="Domoticz Theme Manager" value="domoticz-theme-manager"/>
                <option label="DS238-2 ZN/S ModbusTCP" value="ds238-modbus-tcp"/>
                <option label="DTS238 ZN/S energy meter, three phase, Modbus RTU" value="domoticz-dts238"/>
                <option label="Dyson Pure Link" value="DysonPureLink"/>
                <option label="E-Flux by Road back office" value="E-Flux"/>
                <option label="ebusd bridge" value="ebusd"/>
                <option label="Electrolux / AEG Wellbeing" value="domoticz-wellbeing-plugin"/>
                <option label="Emmeti EQ 2021 amd EQ 3021 ES hot water heat pumps" value="domoticz-emmeti-eq2021"/>
                <option label="Emmeti Mirai heat pumps" value="domoticz-emmeti-mirai"/>
                <option label="EMS bus Wi-Fi Gateway" value="ems-gateway"/>
                <option label="EVCC IO Plugin" value="Domoticz-EVCC-IO-Plugin"/>
                <option label="FoxESS inverter" value="FoxESS-domoticz"/>
                <option label="Freebox V6 (Revolution)" value="freeboxv6"/>
                <option label="GoodWE Solar inverter via SEMS API" value="GoodWeAPI"/>
                <option label="Govee Local Api Control" value="GoveeDiscovery"/>
                <option label="Hisense air conditioners" value="Hisense-AirCon-Domoticz"/>
                <option label="Homewizard" value="Homewizard"/>
                <option label="Homewizard Battery" value="Homewizard-Battery"/>
                <option label="Hyundai and Kia vehicles" value="HyundaiKiaConnect"/>
                <option label="iDetect Presence Detection" value="iDetect"/>
                <option label="IKEA Tradfri" value="IKEA-Tradfri"/>
                <option label="Integrate with AWTRIX3 Smart Clock" value="AWTRIX3"/>
                <option label="Itho Wifi module" value="IthoWifi"/>
                <option label="LG ThinQ devices" value="domoticz_lg_thinq_plugin"/>
                <option label="Link-Tap Watering System" value="Link-Tap"/>
                <option label="Linky" value="Linky"/>
                <option label="Luxtronik heat pump v2" value="luxtronik-domoticz-plugin-v2"/>
                <option label="Lyrion Music Server (LMS)" value="LyrionMusicServer"/>
                <option label="MQTT discovery" value="MQTTDiscovery"/>
                <option label="MQTT Mapper" value="domoticz-mqttmapper-plugin"/>
                <option label="OpenWRT WiFi Presence MQTT translator" value="owrtwifi2domo"/>
                <option label="Peblar wallbox" value="domoticz-peblar"/>
                <option label="PZEM-016 PZEM-014 PZEM-004T energy meters" value="pzem016"/>
                <option label="Quatt" value="Quatt"/>
                <option label="SMA solar inverters" value="Domoticz-SMA-Inverter"/>
                <option label="SolarEdge ModbusTCP" value="domoticz-solaredge-modbustcp-plugin"/>
                <option label="Solax inverter ModBUS TCP" value="Domoticz-Solax-plugin"/>
                <option label="Sonoff Mini" value="sonoff-domoticz-plugin"/>
                <option label="Steam player status" value="steam"/>
                <option label="Synology SurveillanceStation" value="Synology SurveillanceStation"/>
                <option label="Tailscale Integration" value="domoticz-tailscale-plugin"/>
                <option label="Tile Bluetooth Tracker" value="DomoticzTile"/>
                <option label="Tuya" value="tuyaha"/>
                <option label="Tuya Cloud API" value="domoticz-tuya-cloud"/>
                <option label="Wan IP Checker" value="WAN-IP-CHECKER"/>
                <option label="WLANThermo" value="WLANThermo"/>
                <option label="WLED" value="WLED"/>
                <option label="Xiaomi Mi Flower Mate" value="Mi_Flower_mate_plugin"/>
                <option label="Xiaomi Mi Robot Vacuum" value="xiaomi-mi-robot-vacuum"/>
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


import os
import platform
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

import Domoticz



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
        self.exception_list = []
        self.secpoluser_list = {}
        self.plugin_data = {}
        self.last_update_date = None

    def fetch_registry(self):

        registry_url = "https://raw.githubusercontent.com/adrighem/pp-manager/refs/heads/master/registry.json"
        Domoticz.Debug("Fetching plugin registry from GitHub.")
        try:
            req = urllib.request.Request(registry_url)
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    self.plugin_data = json.loads(response.read().decode('utf-8'))
                    Domoticz.Log("Successfully fetched plugin registry from GitHub.")
                else:
                    Domoticz.Error("Failed to fetch registry, status code: " + str(response.status))
        except Exception as e:
            Domoticz.Error("Error fetching registry: " + str(e))
            # Fallback to local file if fetch fails
            local_reg = os.path.join(os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), "..", "..")), "plugins", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), "registry.json")
            if os.path.isfile(local_reg):
                with open(local_reg, 'r') as f:
                    self.plugin_data = json.load(f)
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

        Domoticz.Log(f"Domoticz Node Name is: {platform.node()}")
        Domoticz.Log(f"Domoticz Platform System is: {platform.system()}")
        Domoticz.Debug(f"Domoticz Platform Release is: {platform.release()}")
        Domoticz.Debug(f"Domoticz Platform Version is: {platform.version()}")
        Domoticz.Log(f"Default Python Version is: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")

        if platform.system() == "Windows":
            Domoticz.Error("Windows Platform NOT YET SUPPORTED!!")
            return

        plugins_dir = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), ".."))

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

        plugin_key = Parameters.get("Mode3", "").strip() or Parameters["Mode2"]
        if plugin_key == "Idle":
            plugin_author, plugin_repository, plugin_text, plugin_branch = "Idle", "Idle", "Idle", "master"
        elif plugin_key in self.plugin_data:
            plugin_author = self.plugin_data[plugin_key][0]
            plugin_repository = self.plugin_data[plugin_key][1]
            plugin_text = self.plugin_data[plugin_key][2]
            plugin_branch = self.plugin_data[plugin_key][3]
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
                            if secpoluserSection not in self.secpoluser_list:
                                self.secpoluser_list[secpoluserSection] = []
                            self.secpoluser_list[secpoluserSection].append(line)
                Domoticz.Log("SecPolUserList exception:" + str(self.secpoluser_list))
            else:
                self.secpoluser_list = {"Global":[]}

            # Scan all plugins in the plugins directory
            for plugin_folder in os.listdir(plugins_dir):
                plugin_path = os.path.join(plugins_dir, plugin_folder)

                # Make sure it's a directory and not the manager itself
                if os.path.isdir(plugin_path) and plugin_folder != os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):

                    # Recursively walk through the plugin's folder to find all .py files
                    for root, _, files in os.walk(plugin_path):
                        # Optional: skip hidden folders like .git or .shared_deps
                        if '/.' in root.replace('\\', '/'):
                            continue

                        for file in files:
                            if file.endswith('.py'):
                                py_file = os.path.join(root, file)
                                self.parseFileForSecurityIssues(py_file, plugin_folder)

        exceptionFile = os.path.join(plugins_dir, os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), "exceptions.txt")
        Domoticz.Debug("Checking for Exception file on:" + exceptionFile)
        if os.path.isfile(exceptionFile):
            Domoticz.Log("Exception file found. Processing!!!")
            with open(exceptionFile) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        Domoticz.Log("File ReadLine result:'" + line + "'")
                        self.exception_list.append(line)
        Domoticz.Debug("self.exception_list:" + str(self.exception_list))

        if Parameters["Mode4"] == 'All':
            Domoticz.Log("Updating All Plugins!!!")
            for root, dirs, files in os.walk(plugins_dir):
                for d in dirs:
                    if d:
                        if d in self.plugin_data:
                            self.UpdatePythonPlugin(self.plugin_data[d][0], self.plugin_data[d][1], d)
                        elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
                            Domoticz.Debug("PP-Manager Folder found. Skipping!!")
                        else:
                            Domoticz.Log(f"Plugin: {d} cannot be managed with PP-Manager!!.")
                break

        if Parameters["Mode4"] == 'AllNotify':
            Domoticz.Log("Collecting Updates for All Plugins!!!")
            for root, dirs, files in os.walk(plugins_dir):
                for d in dirs:
                    if d:
                        if d in self.plugin_data:
                            self.CheckForUpdatePythonPlugin(self.plugin_data[d][0], self.plugin_data[d][1], d)
                        elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
                            Domoticz.Debug("PP-Manager Folder found. Skipping!!")
                        else:
                            Domoticz.Log(f"Plugin: {d} cannot be managed with PP-Manager!!.")
                break

        if Parameters["Mode4"] == 'SelectedNotify':
            Domoticz.Log("Collecting Updates for Plugin:" + plugin_key)
            if plugin_key in self.plugin_data:
                self.CheckForUpdatePythonPlugin(plugin_author, plugin_repository, plugin_key)

        if plugin_key == "Idle":
            Domoticz.Log("Plugin Idle")
            Domoticz.Heartbeat(60)
        else:
            plugin_target_dir = os.path.join(plugins_dir, plugin_key)
            Domoticz.Debug("Checking for dir:" + plugin_target_dir)
            if os.path.isdir(plugin_target_dir):
                Domoticz.Debug("Folder for Plugin:" + plugin_key + " already exists!!!")
                if Parameters["Mode4"] == 'Selected':
                    Domoticz.Debug("Updating Enabled for Plugin:" + plugin_text + ".Checking For Update!!!")
                    self.UpdatePythonPlugin(plugin_author, plugin_repository, plugin_key)
                Domoticz.Heartbeat(60)
            else:
                Domoticz.Log("Installation requested for Plugin:" + plugin_text)
                Domoticz.Debug("Installation URL is: https://github.com/" + plugin_author + "/" + plugin_repository)
                Domoticz.Debug("Current Working dir is:" + plugins_dir)
                if plugin_key in self.plugin_data:
                    Domoticz.Log("Plugin Display Name:" + plugin_text)
                    Domoticz.Log("Plugin Author:" + plugin_author)
                    Domoticz.Log("Plugin Repository:" + plugin_repository)
                    Domoticz.Log("Plugin Key:" + plugin_key)
                    Domoticz.Log("Plugin Branch:" + plugin_branch)
                    self.InstallPythonPlugin(plugin_author, plugin_repository, plugin_key, plugin_branch)
                Domoticz.Heartbeat(60)

    def onStop(self):
        Domoticz.Debug("onStop called")
        Domoticz.Log("Plugin is stopping.")
        self.UpdatePythonPlugin("adrighem", "pp-manager", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))))
        Domoticz.Debugging(0)

    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat called")
        plugin_key = Parameters.get("Mode3", "").strip() or Parameters["Mode2"]

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
                            if d in self.plugin_data:
                                self.UpdatePythonPlugin(self.plugin_data[d][0], self.plugin_data[d][1], d)
                            elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
                                Domoticz.Debug("PP-Manager Folder found. Skipping!!")
                            else:
                                Domoticz.Log(f"Plugin: {d} cannot be managed with PP-Manager!!.")
                    break

            if Parameters["Mode4"] == 'AllNotify':
                Domoticz.Log("Collecting Updates for All Plugins!!!")
                for root, dirs, files in os.walk(plugins_dir):
                    for d in dirs:
                        if d:
                            if d in self.plugin_data:
                                self.CheckForUpdatePythonPlugin(self.plugin_data[d][0], self.plugin_data[d][1], d)
                            elif d == os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))):
                                Domoticz.Debug("PP-Manager Folder found. Skipping!!")
                            else:
                                Domoticz.Log(f"Plugin: {d} cannot be managed with PP-Manager!!.")
                    break

            if Parameters["Mode4"] == 'SelectedNotify':
                Domoticz.Log("Collecting Updates for Plugin:" + plugin_key)
                if plugin_key in self.plugin_data:
                    self.CheckForUpdatePythonPlugin(self.plugin_data[plugin_key][0], self.plugin_data[plugin_key][1], plugin_key)
                else:
                    Domoticz.Log(f"Plugin: {plugin_key} not found in plugin_data. Skipping update check.")

            if Parameters["Mode4"] == 'Selected' and plugin_key in self.plugin_data:
                Domoticz.Log(f"Checking Updates for Plugin: {self.plugin_data[plugin_key][2]}")
                self.UpdatePythonPlugin(self.plugin_data[plugin_key][0], self.plugin_data[plugin_key][1], plugin_key)

    def InstallPythonPlugin(self, ppAuthor, ppRepository, ppKey, ppBranch):
        Domoticz.Debug("InstallPythonPlugin called")

        plugins_dir = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), ".."))

        Domoticz.Log("Installing Plugin:" + self.plugin_data[ppKey][2])
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
        elif (ppKey in self.plugin_data and self.plugin_data[ppKey][2] in self.exception_list):
            Domoticz.Log("Plugin:" + self.plugin_data[ppKey][2] + " excluded by Exclusion file (exclusion.txt). Skipping!!!")
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

        if ppKey in self.plugin_data and self.plugin_data[ppKey][2] in self.exception_list:
            Domoticz.Log("Plugin:" + self.plugin_data[ppKey][2] + " excluded by Exclusion file (exclusion.txt). Skipping!!!")
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
                Domoticz.Debug(f"Git Response: {outFetch}")
            if errorFetch:
                Domoticz.Debug(f"Git Error: {errorFetch.strip()}")
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

    def fnSelectedNotify(self, plugin_key):
        Domoticz.Debug("fnSelectedNotify called")
        Domoticz.Log("Preparing Notification")
        plugin_name = self.plugin_data[plugin_key][2] if plugin_key in self.plugin_data else plugin_key
        MailSubject = platform.node() + ": Domoticz Plugin Updates Available for " + plugin_name
        MailBody = plugin_name + " has updates available!!"
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
        if Parameters.get("Mode5") == 'True':
            Domoticz.Log(f"Scanning {pyfilename} for security issues...")

        if pypluginid not in self.secpoluser_list:
            self.secpoluser_list[pypluginid] = []

        ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

        try:
            # 1. Prevent Large File DoS: Limit file read to 5MB
            MAX_FILE_SIZE = 5 * 1024 * 1024
            with open(pyfilename, "r", encoding="utf-8", errors="ignore") as file:
                source_code = file.read(MAX_FILE_SIZE)
                if file.read(1):
                    Domoticz.Error(f"Plugin file {pyfilename} exceeds 5MB limit. Plugin considered UNSAFE.")
                    return

            try:
                tree = ast.parse(source_code)
            except (SyntaxError, RecursionError, MemoryError, Exception) as e:
                Domoticz.Error(f"Failed to parse plugin file {pyfilename} (Possible AST Bomb or invalid syntax): {e}. Plugin considered UNSAFE.")
                return

            class SecurityScanner(ast.NodeVisitor):
                def __init__(self):
                    self.findings = []

                def get_full_name(self, node):
                    if isinstance(node, ast.Name):
                        return node.id
                    elif isinstance(node, ast.Attribute):
                        val = self.get_full_name(node.value)
                        return f"{val}.{node.attr}" if val else node.attr
                    return ""

                def visit_Call(self, node):
                    func_full_name = self.get_full_name(node.func)

                    func_base_name = ""
                    if isinstance(node.func, ast.Name):
                        func_base_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        func_base_name = node.func.attr

                    exact_matches = {'os.system', 'os.popen', 'eval', 'exec', '__import__', 'compile', 'pickle.loads', 'pickle.load', 'os.remove', 'os.unlink', 'shutil.rmtree'}

                    if func_full_name in exact_matches or func_full_name.startswith('subprocess.'):
                        self.findings.append((node.lineno, f"Suspicious Call: {func_full_name}"))
                    elif func_base_name in {'eval', 'exec', '__import__', 'compile'}:
                        self.findings.append((node.lineno, f"Suspicious Call: {func_base_name}"))
                    elif func_base_name in {'system', 'popen', 'loads', 'rmtree', 'unlink'}:
                        self.findings.append((node.lineno, f"Potentially Suspicious Call (Alias?): {func_base_name}"))

                    self.generic_visit(node)

                def visit_Name(self, node):
                    if node.id in {'eval', 'exec', '__import__', 'compile'} and isinstance(getattr(node, 'ctx', None), ast.Load):
                        self.findings.append((node.lineno, f"Dangerous Builtin Referenced: {node.id}"))
                    self.generic_visit(node)

            scanner = SecurityScanner()
            scanner.visit(tree)

            ast_findings_map = {}
            for lineno, finding in scanner.findings:
                if lineno not in ast_findings_map:
                    ast_findings_map[lineno] = []
                if finding not in ast_findings_map[lineno]:
                    ast_findings_map[lineno].append(finding)

            lines = source_code.splitlines()
            for i, text in enumerate(lines):
                lineNum = i + 1
                clean_text = text.strip()

                if not clean_text or clean_text.startswith('#') or '<param field=' in clean_text:
                    continue

                findings = []

                for ip in ip_pattern.findall(clean_text):
                    if all(0 <= int(octet) <= 255 for octet in ip.split('.')):
                        findings.append(f"IP Address: {ip}")

                if lineNum in ast_findings_map:
                    findings.extend(ast_findings_map[lineNum])

                for finding in findings:
                    is_excluded = False
                    combined_exclusions = self.secpoluser_list.get("Global", []) + self.secpoluser_list[pypluginid]
                    for exclusion in combined_exclusions:
                        if exclusion in clean_text or exclusion in finding:
                            is_excluded = True
                            break

                    if not is_excluded:
                        Domoticz.Error(f"Security Finding in {pypluginid}: --> {finding} <-- LINE: {lineNum} FILE: {pyfilename}")
                        Domoticz.Error(f"Code context: {clean_text}")

        except Exception as e:
            Domoticz.Error(f"Error reading or processing {pyfilename}: {str(e)}")

    def installDependencies(self, plugin_key):
        Domoticz.Debug("installDependencies called")
        plugins_dir = os.path.abspath(os.path.join(Parameters.get("HomeFolder", str(os.getcwd()) + "/"), ".."))
        plugin_dir = os.path.join(plugins_dir, plugin_key)
        requirementsFile = os.path.join(plugin_dir, "requirements.txt")
        shared_deps_dir = os.path.join(home_folder, "plugins", os.path.basename(os.path.normpath(Parameters.get('HomeFolder', str(os.getcwd()) + '/'))), ".shared_deps")

        def check_cmd(cmd):
            try:
                subprocess.run([cmd, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            except:
                return False

        if os.path.isfile(requirementsFile):
            Domoticz.Log("requirements.txt found for plugin: " + plugin_key)
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
            Domoticz.Log("No requirements.txt found for plugin: " + plugin_key)
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
