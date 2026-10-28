import sys
import json
from urllib.request import urlopen


username = sys.argv[1]

print(f'Github username {username}')

url = f"https://api.github.com/users/{username}/events"

with urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))


print(data)

