from fastapi import FastAPI, Depends
from pymongo.database import Database
from app import database, routes


app = FastAPI()
app.include_router(routes.stocks.router, tags=["stocks"])


@app.on_event("shutdown")
async def close_mongo_client() -> None:
    database.mongo_client.close()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}
