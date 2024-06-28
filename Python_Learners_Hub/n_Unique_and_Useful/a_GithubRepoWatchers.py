import requests

owner = 'your-username'
repo = 'your-repo'
url = f'https://api.github.com/repos/{owner}/{repo}/subscribers'

response = requests.get(url, headers={'Accept': 'application/vnd.github.v3+json'})
watchers = response.json()

for watcher in watchers:
    print(watcher['login'])
