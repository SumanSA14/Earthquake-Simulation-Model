import random
from models.person import Person
from models.building import Building
import scheduling

def run_simulation():

    people = []
    buildings = []

    for i in range(20):
        people.append(Person(i,
                             random.uniform(20,25),
                             random.uniform(75,80)))

    for i in range(10):
        buildings.append(Building(i,
                                  random.uniform(20,25),
                                  random.uniform(75,80)))

    epicenter = {
        "lat":22,
        "lng":77
    }

    tasks = []

    for p in people:
        tasks.append({
            "id":p.id,
            "burst":random.randint(1,10),
            "priority":random.randint(1,5)
        })

    fcfs = scheduling.fcfs(tasks.copy())
    sjf = scheduling.sjf(tasks.copy())
    priority = scheduling.priority_schedule(tasks.copy())
    rr = scheduling.round_robin(tasks.copy(),3)

    return {
        "epicenter":epicenter,
        "people":[p.to_dict() for p in people],
        "buildings":[b.to_dict() for b in buildings],
        "fcfs":fcfs,
        "sjf":sjf,
        "priority":priority,
        "round_robin":rr
    }