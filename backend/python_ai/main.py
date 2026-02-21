import asyncio
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
from routes.ai_route import sar_router
from routes.graph_route import router as graph_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("trying to connect to database...")
#     await connect_to_db()
#     print("✅ Database connected")


#     thread = threading.Thread(
#         target=start_consumer,
#         daemon=True
#     )
#     thread.start()

#     yield   # App runs here

#     await close_db_connection()


#     print("App shutting down...")

@asynccontextmanager
async def lifespan(app: FastAPI):

    await connect_to_db()

    # ✅ Start consumer properly
    app.state.consumer_task = asyncio.create_task(start_consumer())

    print("✅ App started")

    yield

    # Shutdown
    app.state.consumer_task.cancel()
    await close_db_connection()

    print("🛑 App shutting down")


app = FastAPI(

    lifespan=lifespan
)



# Routes
app.include_router(health.router)
# app.include_router(riskscore_route.router)
# app.include_router(evidence_generator_routes.evidence_router)
app.include_router(pipeline_router)
app.include_router(sar_router)
app.include_router(graph_router)

# Routes
@app.get("/")
def root():
    return {"message": "FastAPI is running "}