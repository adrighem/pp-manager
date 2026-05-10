import json
import os
import urllib.request
import urllib.parse
from urllib.error import HTTPError
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_FILE = os.path.join(SCRIPT_DIR, '../../registry.json')

def get_repo_info(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'User-Agent': 'Domoticz-Plugin-Scanner', 'Accept': 'application/vnd.github.v3+json'}
    
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'token {token}'
        
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except HTTPError as e:
        if e.code == 404:
            return "DELETED"
        print(f"Error fetching {owner}/{repo}: {e}")
        return None

def search_github():
    # Search for repositories matching 'domoticz plugin' in Python
    query = urllib.parse.quote('domoticz plugin language:python')
    url = f'https://api.github.com/search/repositories?q={query}&sort=updated&order=desc&per_page=100'
    headers = {'User-Agent': 'Domoticz-Plugin-Scanner', 'Accept': 'application/vnd.github.v3+json'}
    
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'token {token}'
        
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('items', [])
    except HTTPError as e:
        print(f"Error searching GitHub: {e}")
        return []

def main():
    if not os.path.exists(REGISTRY_FILE):
        print(f"Registry file not found at {REGISTRY_FILE}")
        return

    with open(REGISTRY_FILE, 'r') as f:
        registry = json.load(f)
        
    stats = {"updated": 0, "removed": 0, "added": 0}
    
    # 1. Sync Existing Plugins
    print("Syncing existing plugins...")
    for key in list(registry.keys()):
        if key == "Idle": continue
        
        data = registry[key]
        owner, repo_name = data[0], data[1]
        
        # Determine if we need to fetch info (for existing plugins, we check 1 in 4 to stay under rate limits if no token)
        # In GitHub Actions, GITHUB_TOKEN is present, so we can check all.
        info = get_repo_info(owner, repo_name)
        
        if info == "DELETED":
            print(f"[-] Removing {key} (Repo deleted)")
            del registry[key]
            stats["removed"] += 1
        elif info:
            if info.get('archived'):
                print(f"[-] Removing {key} (Repo archived)")
                del registry[key]
                stats["removed"] += 1
            else:
                # Update metadata
                updated_desc = info.get('description') or data[2]
                updated_branch = info.get('default_branch') or data[3]
                updated_at = info.get('pushed_at') or info.get('updated_at')
                
                # Check if changed
                if (updated_desc != data[2] or 
                    updated_branch != data[3] or 
                    len(data) < 5 or 
                    data[4] != updated_at):
                    
                    print(f"[*] Updating {key}")
                    # Keep structure but append timestamp at index 4
                    registry[key] = [
                        owner,
                        repo_name,
                        updated_desc,
                        updated_branch,
                        updated_at
                    ]
                    stats["updated"] += 1
        
        # Throttle to respect rate limits
        if not os.environ.get('GITHUB_TOKEN'):
            time.sleep(1)

    # 2. Discover New Plugins
    print("Searching for new plugins...")
    new_items = search_github()
    existing_full_names = {f"{v[0].lower()}/{v[1].lower()}" for k, v in registry.items() if k != "Idle"}
    
    for repo in new_items:
        full_name = repo['full_name'].lower()
        if full_name not in existing_full_names:
            if repo.get('archived'): continue
            
            owner = repo['owner']['login']
            repo_name = repo['name']
            description = repo['description'] or f"{repo_name} plugin for Domoticz"
            default_branch = repo['default_branch']
            pushed_at = repo.get('pushed_at') or repo.get('updated_at')
            
            key = repo_name
            if key in registry:
                key = f"{owner}-{repo_name}"
                
            print(f"[+] Adding {key}")
            registry[key] = [
                owner,
                repo_name,
                description,
                default_branch,
                pushed_at
            ]
            stats["added"] += 1

    # 3. Save Results
    if stats["updated"] > 0 or stats["removed"] > 0 or stats["added"] > 0:
        with open(REGISTRY_FILE, 'w') as f:
            json.dump(registry, f, indent=4)
            f.write('\n')
        print(f"Registry updated: {stats['added']} added, {stats['updated']} updated, {stats['removed']} removed.")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    main()
