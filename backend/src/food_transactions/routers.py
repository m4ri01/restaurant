from fastapi import APIRouter,Depends
from src.database import db
from sqlalchemy import select, func, cast, Date
from uuid import UUID
from src.config import TIMEZONE
from src.food_transactions.models import food_transactions
from src.order_and_payments.models import order_and_payments
from src.food.models import ms_food
from datetime import date
import pendulum

router = APIRouter(
    prefix="/food_transactions",
    tags=["food_transactions"]
)

@router.get("/")
async def get_food_transactions():
    query = select([
        food_transactions.c.id,
        food_transactions.c.order_id,
        food_transactions.c.food_id,
        food_transactions.c.total_item,
        food_transactions.c.total_price,
        ms_food.c.name.label("food_name"),
        order_and_payments.c.payment_status,
        order_and_payments.c.order_status,
        func.timezone(TIMEZONE, food_transactions.c.created_at).label("created_at"),
        func.timezone(TIMEZONE, food_transactions.c.updated_at).label("updated_at")
    ]).join(
        ms_food, food_transactions.c.food_id == ms_food.c.id
    ).join(
        order_and_payments, food_transactions.c.order_id == order_and_payments.c.id
    )
    result = await db.fetch_all(query)
    return result

@router.get("/{date}")
async def get_food_transactions_daily_report(date:date):
    query = select([
        food_transactions.c.id,
        food_transactions.c.order_id,
        food_transactions.c.food_id,
        food_transactions.c.total_item,
        food_transactions.c.total_price,
        ms_food.c.name.label("food_name"),
        order_and_payments.c.payment_status,
        order_and_payments.c.order_status,
        func.timezone(TIMEZONE, food_transactions.c.created_at).label("created_at"),
        func.timezone(TIMEZONE, food_transactions.c.updated_at).label("updated_at")
    ]).join(
        ms_food, food_transactions.c.food_id == ms_food.c.id
    ).join(
        order_and_payments, food_transactions.c.order_id == order_and_payments.c.id
    ).where(
        cast(func.timezone(TIMEZONE, food_transactions.c.created_at), Date) == date
    )
    result = await db.fetch_all(query)
    return result

