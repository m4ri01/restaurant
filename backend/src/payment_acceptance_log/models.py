from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey,Float, Integer
from sqlalchemy.sql import func
from src.user.models import ms_user
from src.order_and_payments.models import order_and_payments
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import MetaData

metadata = MetaData()
payment_acceptance_log = Table(
    "payment_acceptance_log",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("order_and_payments_id",GUID,ForeignKey(order_and_payments.c.id),nullable=False),
    Column("user_id",GUID,ForeignKey(ms_user.c.id),nullable=False),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)