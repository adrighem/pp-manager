import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_FILE = os.path.join(SCRIPT_DIR, '../../plugin_core.py')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, '../../plugin.py')

def generate_plugin():
    xml_header = f'''# pp-manager - PythonPlugin Manager
#
# Author: adrighem, 2018
#
#  Since (2018-02-23): Initial Version
#


"""
<plugin key="PP-MANAGER" name="Python Plugin Manager" author="adrighem" version="2.0.0" externallink="https://www.domoticz.com/forum/viewtopic.php?f=65&t=22339"> &lt;!-- x-release-please-version --&gt;
    <description>
        &lt;h2&gt;Python Plugin Manager&lt;/h2&gt;&lt;br/
        This plugin manages other Domoticz Python plugins.&lt;br/&gt;&lt;br/
        &lt;b&gt;Usage:&lt;/b&gt;&lt;br/
        1. Add this hardware to Domoticz.&lt;br/
        2. Navigate to &lt;b&gt;Custom&lt;/b&gt; -&gt; &lt;b&gt;Plugin Manager&lt;/b&gt; in the top menu to manage your plugins.
    &lt;/description&gt;
    &lt;params&gt;
        &lt;param field="Mode4" label="Auto Update" width="175px"&gt;
            &lt;options&gt;
                &lt;option label="All" value="All"/>
                &lt;option label="All (NotifyOnly)" value="AllNotify" default="true"/>
                &lt;option label="None" value="None"/>
            &lt;/options&gt;
        &lt;/param&gt;
        &lt;param field="Mode6" label="Debug" width="75px"&gt;
            &lt;options&gt;
                &lt;option label="True" value="Debug"/>
                &lt;option label="False" value="Normal" default="true" /&gt;
            &lt;/options&gt;
        &lt;/param&gt;
    &lt;/params&gt;
&lt;/plugin&gt;
"""
'''

    with open(CORE_FILE, 'r') as f:
        core_code = f.read()

    with open(OUTPUT_FILE, 'w') as f:
        f.write(xml_header + "\n" + core_code)

    print("plugin.py successfully generated.")

if __name__ == '__main__':
    generate_plugin()
