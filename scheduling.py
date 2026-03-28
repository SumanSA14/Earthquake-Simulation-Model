def fcfs(tasks):
    order = []
    for task in tasks:
        order.append(task["id"])
    return order


def sjf(tasks):
    tasks = sorted(tasks, key=lambda x: x["burst"])
    return [task["id"] for task in tasks]


def priority_schedule(tasks):
    tasks = sorted(tasks, key=lambda x: x["priority"])
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