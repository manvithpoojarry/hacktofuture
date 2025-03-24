import pandas as pd

# Sample employee data
employees = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "skills": ["Python", "Java", "Python", "SQL"],
    "availability": [40, 35, 45, 30],  # Hours per week
    "workload": [0, 0, 0, 0]  # Assigned hours
})

# Sample tasks
tasks = pd.DataFrame({
    "task_id": [101, 102, 103],
    "skill_required": ["Python", "Java", "SQL"],
    "hours_required": [20, 25, 15]
})

# Function to allocate tasks
def allocate_tasks(employees, tasks):
    assignments = []
    for _, task in tasks.iterrows():
        eligible = employees[employees["skills"] == task["skill_required"]]
        if not eligible.empty:
            best_match = eligible.sort_values("availability", ascending=False).iloc[0]
            employees.loc[employees["id"] == best_match["id"], "workload"] += task["hours_required"]
            assignments.append({"task_id": task["task_id"], "assigned_to": best_match["name"]})
    return pd.DataFrame(assignments)

# Run the scheduler
assignments = allocate_tasks(employees, tasks)

# Print the results
print("Task Assignments:")
print(assignments)
