from fastapi import FastAPI
from routes import health
from routes import riskscore_route

app = FastAPI(
    # title="python-ai",
    # version="1.0.0",
    # description="python-ai Boilerplate"
)


# Routes
app.include_router(health.router)
app.include_router(riskscore_route.router)

# Routes
@app.get("/")
def root():
    return {"message": "FastAPI is running "}