"""App module."""

import uvicorn
from fastapi import FastAPI


from app.database import engine, Base
from app.routes import users
from app.routes import stocks
from app.routes import votes


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(votes.router)
app.include_router(stocks.router)


@app.get("/")
def root():
    return {"message": "hello there"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
