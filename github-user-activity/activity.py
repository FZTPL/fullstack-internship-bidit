def display_activity(events):
    if not events:
        print("No recent activity found.")
        return

    for event in events:
        event_type = event["type"]
        repo = event["repo"]["name"]

        match event_type:
            case "PushEvent":
                commits = len(event["payload"]["commits"])
                print(f"- Pushed {commits} commit(s) to {repo}")

            case "WatchEvent":
                print(f"- Starred {repo}")

            case "ForkEvent":
                print(f"- Forked {repo}")

            case "IssuesEvent":
                print(f"- Opened an issue in {repo}")

            case "PullRequestEvent":
                print(f"- Opened a pull request in {repo}")

            case _:
                print(f"- {event_type} in {repo}")