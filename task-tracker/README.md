# Task Tracker CLI

A simple command-line task tracker built with Python.

Project URL:
https://roadmap.sh/projects/task-tracker

## Description
A simple command-line task tracker built with Python.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as in progress
- Mark tasks as done
- List all tasks
- List tasks by status
- Stores data in a JSON file
- No external libraries required

## Requirements

- Python 3.10+

## Usage

### Add a task

```bash
python task.py add "Learn Python"
```

### Update a task

```bash
python task.py update 1 "Learn Advanced Python"
```

### Delete a task

```bash
python task.py delete 1
```

### Mark task as in progress

```bash
python task.py progress 1
```

### Mark task as done

```bash
python task.py done 1
```

### List all tasks

```bash
python task.py list
```

### List todo tasks

```bash
python task.py list todo
```

### List in-progress tasks

```bash
python task.py list progress
```

### List completed tasks

```bash
python task.py list done
```

## Example Output

```text
1 - Learn Python [todo]
2 - Build CLI App [progress]
3 - Complete Project [done]
```
