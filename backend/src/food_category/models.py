from sqlalchemy import Table,Column,String,DateTime,text
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import MetaData

metadata = MetaData()

ms_food_category = Table(
    "ms_food_category",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("name",String(256),nullable=False,unique=True),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)