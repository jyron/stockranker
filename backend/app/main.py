from app import database, finnhub_module, scratch, stock_module, user_module
from fastapi import FastAPI

app = FastAPI()

app.include_router(stock_module.routes.router, tags=["Stocks"])
app.include_router(finnhub_module.routes.router, tags=["Finnhub"])
app.include_router(scratch.router, tags=["Scratch"])  # Testing Routes.
app.include_router(user_module.routes.router, tags=["Users"])


@app.on_event("shutdown")
async def close_mongo_client() -> None:
    database.mongo_client.close()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "I\'d do anything, for you, in the dark."}
