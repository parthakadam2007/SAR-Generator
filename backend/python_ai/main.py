from fastapi import FastAPI
from routes import health
from routes import riskscore_route
from routes import evidence_generator_routes
from contextlib import asynccontextmanager
from routes.pipeline_route import pipeline_router
import threading
from contextlib import asynccontextmanager
from database import connect_to_db, close_db_connection
from services.kafka_consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("trying to connect to database...")
    await connect_to_db()
    print("✅ Database connected")


    thread = threading.Thread(
        target=start_consumer,
        daemon=True
    )
    thread.start()

    yield   # App runs here

    # await close_db_connection()


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