from fastapi import FastAPI

app = FastAPI(title="Tasks")

@app.get("/")
def index():
    return f"Hello World"