def fcfs(tasks):
    return [task["id"] for task in tasks]


def sjf(tasks):
    tasks.sort(key=lambda x: x["burst"])
    return [task["id"] for task in tasks]


def priority_schedule(tasks):
    tasks.sort(key=lambda x: x["priority"])
    return [task["id"] for task in tasks]


def round_robin(tasks, quantum):

    queue = tasks.copy()
    result = []

    while queue:

        task = queue.pop(0)

        if task["burst"] > quantum:
            task["burst"] -= quantum
            queue.append(task)

        else:
            result.append(task["id"])

    return result