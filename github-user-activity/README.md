# GitHub Activity CLI

A simple command-line application that fetches and displays a GitHub user's recent activity.

## Features

- Fetch recent GitHub activity
- Display activity in a readable format
- Handle invalid usernames
- Handle API errors
- No external libraries used

## Requirements

- Python 3.x

## Usage

```bash
python main.py <github_username>
```

Example:

```bash
python main.py torvalds
```

Sample Output:

```text
Recent GitHub Activity:

- Pushed 3 commit(s) to owner/repository
- Opened an issue in owner/repository
- Starred owner/repository
```
