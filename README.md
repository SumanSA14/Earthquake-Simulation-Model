# Earthquake Simulation Model using Scheduling Algorithms

## Overview
This project presents an **Earthquake Response Simulation Model** designed to evaluate disaster management strategies using concepts from **Operating System scheduling algorithms**. 

The system simulates emergency response tasks that occur during an earthquake scenario and applies different CPU scheduling algorithms to determine how efficiently tasks can be handled. By comparing multiple scheduling techniques, the project analyzes how task allocation and response efficiency can be optimized during disaster situations.

The goal of this simulation is to demonstrate how **algorithmic scheduling strategies can improve emergency response coordination and resource allocation in disaster management systems**.

---

# Objectives

- Simulate emergency response tasks during an earthquake scenario.
- Apply different scheduling algorithms to manage disaster response tasks.
- Analyze how scheduling strategies impact response efficiency.
- Compare algorithm performance in handling emergency workloads.

---

# Scheduling Algorithms Implemented

The following Operating System scheduling algorithms are used in the simulation:

### 1. First Come First Serve (FCFS)
Tasks are executed in the order they arrive in the system. The first request received is processed first.

**Characteristics:**
- Simple to implement
- No task prioritization
- May cause long waiting times

---

### 2. Shortest Job First (SJF)
Tasks with the smallest execution time are processed first.

**Characteristics:**
- Reduces average waiting time
- More efficient than FCFS in many cases
- Requires knowledge of task duration

---

### 3. Priority Scheduling
Tasks are assigned priorities, and the system processes the highest priority task first.

**Characteristics:**
- Useful for emergency situations
- Critical tasks receive immediate attention
- May cause starvation for lower priority tasks

---

### 4. Round Robin Scheduling
Tasks are executed in a cyclic order using a fixed time quantum.

**Characteristics:**
- Fair allocation of CPU time
- Suitable for time-sharing systems
- Prevents starvation

---

# Simulation Workflow

Earthquake Event Simulation
│
▼
Emergency Task Generation
│
▼
Task Scheduling
(FCFS / SJF / Priority / Round Robin)
│
▼
Execution of Response Tasks
│
▼
Performance Evaluation
(Response Time, Efficiency)

---

# Project Structure
Earthquake-Simulation-Model
│
├── earthquake_simulation.py
├── scheduling_algorithms.py
├── results
│
└── README.md
---

# How the Simulation Works

1. An earthquake scenario is simulated.
2. Multiple emergency tasks are generated such as:
   - Rescue operations
   - Medical assistance
   - Resource distribution
   - Infrastructure assessment
3. Tasks are assigned execution times and priorities.
4. Scheduling algorithms determine the order of task execution.
5. The system evaluates performance metrics such as response efficiency.

---
Technologies Used
Python
Operating System Scheduling Algorithms
Simulation Modeling
Data Analysis
Applications

This project can be useful for:

Disaster management planning
Emergency response optimization
Simulation of real-time crisis management
Educational demonstration of OS scheduling algorithms
