import json
import os
import urllib.request
import urllib.parse
from urllib.error import HTTPError
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_FILE = os.path.join(SCRIPT_DIR, 'registry.json')

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

def main():
    with open(REGISTRY_FILE, 'r') as f:
        registry = json.load(f)

    print(f"Auditing {len(registry)} plugins...")

    for key, data in list(registry.items()):
        if key == "Idle": continue

        owner = data[0]
        repo_name = data[1]
        desc = data[2]
        branch = data[3]

        print(f"Checking {owner}/{repo_name}...", end=' ', flush=True)

        info = get_repo_info(owner, repo_name)

        if info == "DELETED":
            print("❌ DELETED (Should be removed)")
        elif info:
            if info.get('archived'):
                print("⚠️ ARCHIVED (Should we remove?)")
            else:
                current_desc = info.get('description', '')
                if current_desc and current_desc != desc:
                    print("📝 Description out of date")
                else:
                    print("✅ OK")
        else:
            print("❓ Unknown Error")

        # Avoid hitting rate limits
        time.sleep(0.5)

if __name__ == '__main__':
    main()
