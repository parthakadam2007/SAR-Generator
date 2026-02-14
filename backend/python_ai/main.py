from fastapi import FastAPI
from routes import health
from routes import riskscore_route
from routes import evidence_generator_routes
from contextlib import asynccontextmanager
from routes.pipeline_route import pipeline_router
import threading


from services.kafka_consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):

    thread = threading.Thread(
        target=start_consumer,
        daemon=True
    )
    thread.start()

    yield   # App runs here


    print("App shutting down...")


app = FastAPI(

    lifespan=lifespan
)



# Routes
app.include_router(health.router)
# app.include_router(riskscore_route.router)
# app.include_router(evidence_generator_routes.evidence_router)
app.include_router(pipeline_router)

# Routes
@app.get("/")
def root():
    return {"message": "FastAPI is running "}