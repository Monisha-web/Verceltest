from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

# Load data from the JSON file
data_file = "q-vercel-python.json"
with open(data_file, "r") as f:
    data = json.load(f)

# Create a lookup dictionary for quick access
marks_dict = {entry["name"]: entry["marks"] for entry in data}

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """
    API endpoint to retrieve marks based on names.
    Example request: /api?name=X&name=Y
    """
    marks = [marks_dict.get(n, None) for n in name]
    return {"marks": marks}

# Run locally if needed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
