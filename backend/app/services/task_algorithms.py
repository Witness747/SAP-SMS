from datetime import date


def sort_tasks_by_deadline(tasks):

    """
    Sort tasks according to due_date using Merge Sort.

    Time Complexity:
    O(n log n)

    Space Complexity:
    O(n)
    """

    if len(tasks) <= 1:
        return tasks


    mid = len(tasks) // 2


    left_half = sort_tasks_by_deadline(
        tasks[:mid]
    )

    right_half = sort_tasks_by_deadline(
        tasks[mid:]
    )


    return merge_deadline_tasks(
        left_half,
        right_half
    )



def merge_deadline_tasks(left, right):

    sorted_tasks = []

    i = 0
    j = 0


    while i < len(left) and j < len(right):

        if left[i].due_date <= right[j].due_date:

            sorted_tasks.append(
                left[i]
            )

            i += 1

        else:

            sorted_tasks.append(
                right[j]
            )

            j += 1


    sorted_tasks.extend(
        left[i:]
    )

    sorted_tasks.extend(
        right[j:]
    )


    return sorted_tasks

def search_tasks_by_title(tasks, keyword):

    """
    Linear Search algorithm.

    Searches tasks by title.

    Time Complexity:
    O(n)

    Space Complexity:
    O(1)
    """

    results = []

    keyword = keyword.lower()


    for task in tasks:

        if keyword in task.title.lower():

            results.append(task)


    return results

def sort_tasks_by_priority(tasks):

    """
    Selection Sort algorithm.

    Priority order:
    High → Medium → Low

    Time Complexity:
    O(n²)

    Space Complexity:
    O(1)
    """

    priority_rank = {

        "High": 1,
        "Medium": 2,
        "Low": 3

    }


    tasks = tasks.copy()


    for i in range(len(tasks)):

        min_index = i


        for j in range(i + 1, len(tasks)):

            if (
                priority_rank[tasks[j].priority]
                <
                priority_rank[tasks[min_index].priority]
            ):

                min_index = j


        tasks[i], tasks[min_index] = (
            tasks[min_index],
            tasks[i]
        )


    return tasks