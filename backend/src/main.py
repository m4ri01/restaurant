import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src.database import db
from src.config import PORT
from src.food_transactions.routers import router as food_transactions_router
from src.order_and_payments.routers import router as order_and_payments_router

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(food_transactions_router)
app.include_router(order_and_payments_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0" ,port=PORT,log_level="info",reload=True)