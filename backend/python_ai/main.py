from fastapi import FastAPI
from routes import health

app = FastAPI(
    # title="python-ai",
    # version="1.0.0",
    # description="python-ai Boilerplate"
)


# Routes
app.include_router(health.router)

# Routes
@app.get("/")
def root():
    return {"message": "FastAPI is running "}