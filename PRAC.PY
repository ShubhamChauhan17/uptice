from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return { "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
    "Salary": [50000, 60000, 55000, 65000, 70000]}