import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PASSWORD =os.getenv("DATABASE_PASSWORD")
print(f"Database URL: {DATABASE_URL}")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

pool: asyncpg.Pool | None = None


async def connect_to_db():
    """
    Create asyncpg pool using Supabase Transaction Pooler.
    """
    global pool
    print("✅Creating pool created ")


    pool = await asyncpg.create_pool(
        user="postgres.iravjtmvujenyrlqngsw",
        password=DATABASE_PASSWORD,  # raw password here
        host="aws-1-ap-south-1.pooler.supabase.com",
        port=6543,
        database="postgres",
        ssl="require",
        statement_cache_size=0,
        min_size=5,
        max_size=20,
        )

    print("✅ Database pool created successfully")


async def close_db_connection():
    """
    Gracefully close pool on shutdown.
    """
    global pool

    if pool:
        await pool.close()
        print("🔴 Database pool closed")


async def get_db():
    """
    Dependency for FastAPI routes.
    Usage: async with get_db() as conn:
    """
    if not pool:
        raise Exception("Database pool not initialized")

    async with pool.acquire() as connection:
        yield connection
