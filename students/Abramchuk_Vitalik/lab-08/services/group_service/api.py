# services/group_service/api.py
from fastapi import FastAPI

app = FastAPI()

groups = {}

@app.post("/groups")
def create_group(data: dict):
    gid = str(len(groups) + 1)
    groups[gid] = data
    return {"id": gid}

@app.get("/groups")
def list_groups():
    return groups