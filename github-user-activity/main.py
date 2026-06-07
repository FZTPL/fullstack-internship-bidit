import sys
from github_api import get_github_activity
from activity import display_activity


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <github_username>")
        return

    username = sys.argv[1]

    events = get_github_activity(username)

    if events is not None:
        display_activity(events)


if __name__ == "__main__":
    main()