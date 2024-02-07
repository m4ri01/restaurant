from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey, Float,Integer
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from src.restaurant.models import ms_restaurant
from src.food_category.models import ms_food_category
from src.role.models import ms_role
from sqlalchemy import MetaData

metadata = MetaData()
ms_food = Table(
    "ms_food",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("name",String(256),nullable=False,unique=True),
    Column("category_id",GUID,ForeignKey(ms_food_category.c.id,ondelete="CASCADE"),nullable=False),
    Column("restaurant_id",GUID,ForeignKey(ms_restaurant.c.id,ondelete="CASCADE"),nullable=False),
    Column("description",String(256),nullable=False),
    Column("status",Integer,nullable=False),
    Column("price",Float,nullable=False),
    Column("food_image",String(256),nullable=False),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)