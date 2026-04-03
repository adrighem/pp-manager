# Python Plugin Manager for Domoticz (PP-MANAGER)

A robust and modern plugin manager for Domoticz that allows you to install and automatically update other Python plugins directly from GitHub.

**Note:** This plugin runs exclusively on Linux Systems (including Raspberry Pi).

## 🚀 Key Features

*   **Install Plugins:** Easily install plugins from a curated registry directly from the Domoticz Hardware page.
*   **Auto Updates:** Automatically checks and pulls updates for installed plugins.
*   **Dependency Management with `uv`:** Fully PEP 668 compliant. Dependencies from `requirements.txt` are safely installed into a local `.shared_deps` isolated folder without requiring `sudo` or global `pip` access.
*   **Update Notifications:** Opt-in to receive email/system notifications when a plugin update is available.
*   **Decoupled Registry:** Uses `registry.json` dynamically fetched from GitHub, so you don't need to constantly update the manager just to see new plugins in your list.
*   **Custom Plugin Installation:** Support for entering a custom plugin ID (defined in `registry.json`) outside of the dropdown menu.

---

## 🛠 Prerequisites

1.  **Git:** Required to clone and update repositories. (`sudo apt install git`)
2.  **uv:** Required for fast and safe Python dependency resolution. (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

---

## 📥 Installation

Navigate to your Domoticz `plugins` folder and clone this repository as `00-PP-MANAGER`.

```bash
cd domoticz/plugins
git clone https://github.com/adrighem/pp-manager.git 00-PP-MANAGER
```

### Why `00-PP-MANAGER`?
Domoticz loads Python plugins alphabetically by folder name. Prefixing with `00-` ensures that the manager loads first. This enables `PP-MANAGER` to set up the shared `uv` dependency environment (`.shared_deps`) so other plugins can load their required libraries immediately on startup.

After cloning, restart your Domoticz service:
```bash
sudo systemctl restart domoticz.service
```

---

## ⚙️ Configuration (Domoticz Hardware Page)

Once installed and Domoticz is restarted, go to **Setup -> Hardware** and add **Python Plugin Manager**.

### Parameters

*   **Domoticz Port:** The HTTP port your Domoticz instance is running on (default: `8080`). This is required for the manager to send local notifications.
*   **Plugin to install:** Dropdown list populated from the community registry. Select a plugin and click "Update" to install it.
*   **Custom Plugin ID:** If the plugin you want to install is in the registry but not showing up in your dropdown (because you haven't updated the PP-MANAGER plugin itself yet), you can manually type its registry ID here.
*   **Auto Update:**
    *   **All:** Continuously updates all installed plugins.
    *   **All (NotifyOnly):** Checks all plugins for updates and notifies you.
    *   **Selected:** Continuously updates only the plugin selected in the dropdown.
    *   **Selected (NotifyOnly):** Checks only the selected plugin for updates and notifies you.
    *   **None:** Disables auto-updating.
*   **Security Scan (Experimental):** Set to True to scan for potentially suspicious IPs and subprocess executions within downloaded plugins.

---

## 📚 For Plugin Developers (Adding to the Registry)

To add your plugin to the manager, simply submit a Pull Request to update `registry.json` in this repository.

The format is:
```json
"Your_Plugin_ID": [
    "GitHub_Author",
    "GitHub_Repository_Name",
    "Display Name / Description",
    "branch_name"
]
```

When a Pull Request modifying `registry.json` is merged, a GitHub Action automatically regenerates the `plugin.py` XML dropdown parameters so Domoticz users will immediately see your new plugin available for download.

---

## ⚠️ Security Warning
Auto-updating plugins without manually reviewing the code changes exposes your system to whatever the developer pushes. By using auto-update, you trust the developers of your installed plugins.

## 💬 Discussion & Support
Join the conversation on the official Domoticz forums:
http://www.domoticz.com/forum/viewtopic.php?f=65&t=22339
