from app import database, finnhub, routes, scratch
from fastapi import FastAPI

app = FastAPI()

app.include_router(routes.stocks.router, tags=["Stocks"])
app.include_router(finnhub.finnhub_routes.router, tags=["Finnhub"])
app.include_router(scratch.router, tags=["Scratch"])  # Testing Routes.


@app.on_event("shutdown")
async def close_mongo_client() -> None:
    database.mongo_client.close()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "I\'d do anything, for you, in the dark."}
