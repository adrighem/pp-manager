# Python Plugin Manager for Domoticz (PP-MANAGER)

A robust and modern plugin manager for Domoticz that allows you to install and automatically update other Python plugins directly from GitHub.

**Note:** This plugin runs exclusively on Linux Systems (including Raspberry Pi).

> **A Fork for the Future:** This repository is a modernized fork of the original [ycahome/pp-manager](https://github.com/ycahome/pp-manager). It was created to clean up the codebase, ensure full compatibility with modern Python versions (including Python 3.13 and up), and introduce significantly advanced security and dependency management features.

---

## 🚀 Key Features

*   **Install Plugins:** Easily install plugins from a curated registry directly from the Domoticz Hardware page.
*   **Auto Updates:** Automatically checks and pulls updates for installed plugins.
*   **Flexible Dependency Management:** Supports automatic dependency installation using `uv` (recommended) or `pip`. Also allows for manual sysadmin-managed dependencies.
*   **PEP 668 Compliant:** When using `uv` or `pip`, dependencies are safely installed into a local `.shared_deps` isolated folder without requiring `sudo` or global `pip` access.
*   **Update Notifications:** Opt-in to receive email/system notifications when a plugin update is available.
*   **Decoupled Registry:** Uses `registry.json` dynamically fetched from GitHub, so you don't need to constantly update the manager just to see new plugins in your list.
*   **Custom Plugin Installation:** Support for entering a custom plugin ID (defined in `registry.json`) outside of the dropdown menu.

## 🛡️ Advanced Security Scanning

This fork introduces a vastly improved **Abstract Syntax Tree (AST)** based security scanner to protect your Domoticz instance from malicious plugins:
*   **Deep Execution Detection:** Detects calls to dangerous functions like `os.system`, `subprocess`, `eval`, `exec`, and `pickle` regardless of how deeply nested or aliased they are.
*   **Destructive Operation Blocking:** Flags destructive file operations such as `shutil.rmtree` or `os.remove`.
*   **AST Bomb & DoS Protection:** Implements hard file size limits (5MB) and recursive parsing exception handling to prevent malicious files from crashing your plugin manager.
*   **Suspicious IP Detection:** Uses precise regex to scan all downloaded code for hardcoded IPv4 addresses.

---

## 🛠 Prerequisites

1.  **Git:** Required to clone and update repositories. (`sudo apt install git`)
2.  **uv (Recommended):** For fast and safe Python dependency resolution. (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
3.  **pip/pip3 (Optional):** Fallback if `uv` is not installed.

---

## 📥 Installation

Navigate to your Domoticz `plugins` folder and clone this repository as `00-PP-MANAGER`.

```bash
cd domoticz/plugins
git clone https://github.com/adrighem/pp-manager.git 00-PP-MANAGER
```

### Why `00-PP-MANAGER`?
Domoticz loads Python plugins alphabetically by folder name. Prefixing with `00-` ensures that the manager loads first. This enables `PP-MANAGER` to set up the shared dependency environment (`.shared_deps`) so other plugins can load their required libraries immediately on startup.

After cloning, restart your Domoticz service:
```bash
sudo systemctl restart domoticz.service
```

---

## 📦 Manual Dependency Management

If you prefer to manage dependencies manually or are on a system where automatic installation is restricted, you can install the required libraries for your plugins manually.

PP-MANAGER looks for shared dependencies in its own `.shared_deps` directory and adds it to `sys.path`.

To install dependencies for a specific plugin manually:
1.  Check the `requirements.txt` file in the plugin's folder.
2.  Install them into the `00-PP-MANAGER/.shared_deps` folder:
    ```bash
    pip install -r /path/to/plugin/requirements.txt --target /path/to/domoticz/plugins/00-PP-MANAGER/.shared_deps
    ```

---

## ⚙️ Configuration (Domoticz Hardware Page)

Once installed and Domoticz is restarted, go to **Setup -> Hardware** and add **Python Plugin Manager**.

### Parameters

*   **Plugin to install:** Dropdown list populated from the community registry. Select a plugin and click "Update" to install it.
*   **Custom Plugin ID:** If the plugin you want to install is in the registry but not showing up in your dropdown, you can manually type its registry ID here.
*   **Auto Update:**
    *   **All:** Continuously updates all installed plugins.
    *   **All (NotifyOnly):** Checks all plugins for updates and notifies you.
    *   **Selected:** Continuously updates only the plugin selected in the dropdown.
    *   **Selected (NotifyOnly):** Checks only the selected plugin for updates and notifies you.
    *   **None:** Disables auto-updating.
*   **Security Scan (Experimental):** Set to True to enable the advanced AST and IP scanner to identify potentially suspicious code inside downloaded plugins.

---

## 📚 For Plugin Developers (Adding to the Registry)

To add your plugin to the manager, simply submit a Pull Request to update `registry.json` in this repository.

When a Pull Request modifying `registry.json` is merged, a GitHub Action automatically regenerates the `plugin.py` XML dropdown parameters.

---

## ⚠️ Security Warning
Auto-updating plugins without manually reviewing the code changes exposes your system to whatever the developer pushes. By using auto-update, you trust the developers of your installed plugins.

## 💬 Discussion & Support
Join the conversation on the official Domoticz forums:
https://forum.domoticz.com/viewtopic.php?t=22339
