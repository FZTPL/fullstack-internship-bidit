import json
import urllib.request
import urllib.error


def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Python"}
        )

        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())

            return data

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Error: User not found.")
        else:
            print(f"HTTP Error: {e.code}")

    except urllib.error.URLError as e:
        print(f"Error: Could not connect to GitHub API. {e}")

    return None