from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from src.food.models import ms_food
from src.user.models import ms_user
from src.role.models import ms_role
from sqlalchemy import MetaData

metadata = MetaData()
food_log = Table(
    "food_log",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("food_id",GUID,ForeignKey(ms_food.c.id,ondelete="CASCADE"),nullable=False),
    Column("user_id",GUID,ForeignKey(ms_user.c.id,ondelete="CASCADE"),nullable=False),
    Column("description",String(256),nullable=False),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)