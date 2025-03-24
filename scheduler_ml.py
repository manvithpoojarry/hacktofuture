import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample employee data
employees = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "skills": ["Python", "Java", "Python", "SQL"],
    "availability": [40, 35, 45, 30],  # Hours per week
    "workload": [0, 0, 0, 0]  # Assigned hours
})

# Generate synthetic data for ML model training
data = pd.DataFrame({
    "availability": [30, 35, 40, 25, 50, 45, 20, 30],  # Renamed to match employees data
    "tasks_completed": [3, 4, 5, 2, 6, 5, 2, 3]
})

# Train ML model
X = data[["availability"]]  # Now matches the column used in employees
y = data["tasks_completed"]
model = LinearRegression()
model.fit(X, y)

# Predict workload capacity
employees["predicted_tasks"] = model.predict(employees[["availability"]])

print(employees)
