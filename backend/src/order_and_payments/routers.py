from fastapi import APIRouter,Depends
from src.database import db
from sqlalchemy import select, func, cast, Date
from uuid import UUID
from src.config import TIMEZONE
from src.food_transactions.models import food_transactions
from src.order_and_payments.models import order_and_payments
from src.user.models import ms_user
from datetime import date

router = APIRouter(
    prefix="/order_and_payments",
    tags=["order_and_payments"]
)  

@router.get("/")
async def get_order_and_payments():
    query = select([
        order_and_payments.c.id,
        order_and_payments.c.user_id,
        order_and_payments.c.total_price,
        order_and_payments.c.payment_status,
        order_and_payments.c.order_status,
        ms_user.c.name.label("user_name"),
        func.timezone(TIMEZONE, order_and_payments.c.created_at).label("created_at"),
        func.timezone(TIMEZONE, order_and_payments.c.updated_at).label("updated_at")
    ]).join(
        ms_user, order_and_payments.c.user_id == ms_user.c.id
    )
    result = await db.fetch_all(query)
    return result

@router.get("/{date}")
async def get_order_and_payments_daily_report(date:date):
    query = select([
        order_and_payments.c.id,
        order_and_payments.c.user_id,
        order_and_payments.c.total_price,
        order_and_payments.c.payment_status,
        order_and_payments.c.order_status,
        ms_user.c.name.label("user_name"),
        func.timezone(TIMEZONE, order_and_payments.c.created_at).label("created_at"),
        func.timezone(TIMEZONE, order_and_payments.c.updated_at).label("updated_at")
    ]).join(
        ms_user, order_and_payments.c.user_id == ms_user.c.id
    ).where(
        cast(func.timezone(TIMEZONE, order_and_payments.c.created_at), Date) == date
    )
    result = await db.fetch_all(query)
    return result
