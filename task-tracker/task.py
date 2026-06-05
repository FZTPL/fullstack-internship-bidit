import sys

from operation import add_task
from operation import update_task
from operation import delete_task
from operation import mark_in_progress
from operation import mark_done
from operation import list_tasks


if len(sys.argv) < 2:
    print("Please enter a command.")

else:
    command = sys.argv[1]

    if command == "add":

        description = sys.argv[2]
        add_task(description)

    elif command == "update":

        task_id = int(sys.argv[2])
        description = sys.argv[3]

        update_task(task_id, description)

    elif command == "delete":

        task_id = int(sys.argv[2])

        delete_task(task_id)

    elif command == "mark-in-progress":

        task_id = int(sys.argv[2])

        mark_in_progress(task_id)

    elif command == "mark-done":

        task_id = int(sys.argv[2])

        mark_done(task_id)

    elif command == "list":

        if len(sys.argv) == 2:

            list_tasks()

        else:

            status = sys.argv[2]

            list_tasks(status)

    else:
        print("Invalid command.")