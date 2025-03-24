from fastapi import FastAPI
from scheduler_ml import ml_allocate_tasks, employees, tasks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Workforce Scheduler API"}

@app.get("/allocate")
def allocate():
    assignments = ml_allocate_tasks(employees, tasks)
    return assignments.to_dict(orient="records")

# Run with: uvicorn api:app --reload
