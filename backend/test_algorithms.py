from datetime import date

from app.services.task_algorithms import (
    sort_tasks_by_deadline,
    search_tasks_by_title,
    sort_tasks_by_priority
)


class MockTask:

    def __init__(self, title, due_date,priority="Medium"):

        self.title = title
        self.due_date = due_date
        self.priority = priority


tasks = [

    MockTask(
        "LPU Assignment",
        date(2026, 7, 28)
    ),

    MockTask(
        "DSA Practice",
        date(2026, 7, 20)
    ),

    MockTask(
        "Internship Class",
        date(2026, 7, 25)
    )

]

priority_tasks = [

    MockTask(
        "Read Notes",
        date(2026,7,30),
        "Low"
    ),

    MockTask(
        "Submit CA",
        date(2026,7,22),
        "High"
    ),

    MockTask(
        "Practice DSA",
        date(2026,7,25),
        "Medium"
    )

]


sorted_tasks = sort_tasks_by_deadline(tasks)


for task in sorted_tasks:

    print(
        task.title,
        task.due_date
    )

print("\nSearch Result:")

searched_tasks = search_tasks_by_title(
    tasks,
    "DSA"
)


for task in searched_tasks:

    print(task.title)


print("\nSorted by Priority:")

sorted_priority = sort_tasks_by_priority(
    priority_tasks
)

for task in sorted_priority:

    print(
        task.title,
        task.priority
    )