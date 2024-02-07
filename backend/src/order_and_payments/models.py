from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey, ARRAY, Float, Integer
from sqlalchemy.sql import func
from src.user.models import ms_user
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import MetaData

metadata = MetaData()
order_and_payments = Table(
    "order_and_payments",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("user_id",GUID,ForeignKey(ms_user.c.id,ondelete="CASCADE"),nullable=True),
    Column("total_price",Float,nullable=False),
    Column("payment_status", Integer, nullable=False),
    Column("order_status", Integer, nullable=False),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)