from fastapi import FastAPI

from Lesson16.Lesson16.main import message
from models import Developer,Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"messages":"Developer created successfully","developer":developer}

@app.post("/projects/")
def create_projects(project:Project):
    return {"messages":"Developer created successfully","project":project}