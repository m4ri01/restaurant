from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey,Integer,Float
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from src.food.models import ms_food
from src.order_and_payments.models import order_and_payments
from sqlalchemy import MetaData

metadata = MetaData()
food_transactions = Table(
    "food_transactions",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("food_id",GUID,ForeignKey(ms_food.c.id,ondelete="CASCADE"),nullable=False),
    Column("order_id",GUID,ForeignKey(order_and_payments.c.id,ondelete="CASCADE"),nullable=False),
    Column("total_item",Integer,nullable=False),
    Column("total_price",Float,nullable=True),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)
