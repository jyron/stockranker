"""
Server main runtime
"""

# pylint: disable=unused-import

from app import jwt
from app.app import app
from app.routes.auth import router as AuthRouter
from app.routes.mail import router as MailRouter
from app.routes.register import router as RegisterRouter
from app.routes.user import router as UserRouter
from app.routes.stock import router as StockRouter


app.include_router(AuthRouter)
app.include_router(MailRouter)
app.include_router(RegisterRouter)
app.include_router(UserRouter)
app.include_router(StockRouter)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}
