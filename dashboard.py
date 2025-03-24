import streamlit as st
import pandas as pd
from scheduler_ml import ml_allocate_tasks, employees, tasks

# Run the task allocation model
assignments = ml_allocate_tasks(employees, tasks)

# Dashboard Title
st.title("AI-Driven Workforce Planning Dashboard")

# Employee Availability Table
st.subheader("Employee Availability")
st.dataframe(employees)

# Task Assignments Table
st.subheader("Task Allocations")
st.dataframe(assignments)

# Workload Visualization
st.subheader("Employee Workload")
st.bar_chart(employees.set_index("name")["workload"])

# Refresh Button
if st.button("Reallocate Tasks"):
    assignments = ml_allocate_tasks(employees, tasks)
    st.dataframe(assignments)
    st.bar_chart(employees.set_index("name")["workload"])
