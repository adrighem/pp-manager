import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_FILE = os.path.join(SCRIPT_DIR, '../../registry.json')
CORE_FILE = os.path.join(SCRIPT_DIR, '../../plugin_core.py')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, '../../plugin.py')

def generate_plugin():
    with open(REGISTRY_FILE, 'r') as f:
        registry = json.load(f)

    # Sort plugins by label (index 2)
    plugins = []
    for key, data in registry.items():
        if key == "Idle": continue
        plugins.append((key, data[2]))
    
    plugins.sort(key=lambda x: x[1].lower())

    options_xml = '                <option label="Idle" value="Idle"  default="true" />\n'
    for key, label in plugins:
        options_xml += f'                <option label="{label}" value="{key}"/>\n'

    xml_header = f'''# pp-manager - PythonPlugin Manager
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
        <param field="Mode1" label="Domoticz Port" width="75px" required="true" default="8080"/>
        <param field="Mode2" label="Plugin to install" width="200px">
            <options>
{options_xml.rstrip()}
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
'''

    with open(CORE_FILE, 'r') as f:
        core_code = f.read()

    with open(OUTPUT_FILE, 'w') as f:
        f.write(xml_header + "\n" + core_code)

    print("plugin.py successfully generated.")

if __name__ == '__main__':
    generate_plugin()
