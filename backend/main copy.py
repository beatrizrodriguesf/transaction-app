from fastapi import FastAPI
from dependencies import lifespan
from endpoints import user, transaction, category

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(category.router)
app.include_router(transaction.router)