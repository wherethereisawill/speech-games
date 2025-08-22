# cd backend
# uvicorn main:app --reload --host 0.0.0.0 --port 8000

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}