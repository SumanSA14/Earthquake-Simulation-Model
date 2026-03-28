from flask import Flask, render_template, jsonify
import random
from scheduling import fcfs, sjf, priority_schedule, round_robin

app = Flask(__name__)

tasks = []

def generate_tasks():
    global tasks
    tasks = []

    for i in range(8):
        task = {
            "id": i,
            "type": random.choice(["rescue", "medical", "rebuild"]),
            "burst": random.randint(1,10),
            "priority": random.randint(1,5)
        }
        tasks.append(task)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/earthquake")
def earthquake():
    generate_tasks()

    fcfs_result = fcfs(tasks.copy())
    sjf_result = sjf(tasks.copy())
    priority_result = priority_schedule(tasks.copy())
    rr_result = round_robin(tasks.copy(), 3)

    return jsonify({
        "tasks": tasks,
        "fcfs": fcfs_result,
        "sjf": sjf_result,
        "priority": priority_result,
        "round_robin": rr_result
    })

if __name__ == "__main__":
    app.run(debug=True)