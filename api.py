from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


json_file = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

try:
    with open(json_file) as f:
        marks_data = json.load(f)
except Exception as e:
    print("Error loading JSON:", e)
    marks_data = {}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
