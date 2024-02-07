from sqlalchemy import Table,Column,String,DateTime,text, ForeignKey
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from src.role.models import ms_role
from sqlalchemy import MetaData

metadata = MetaData()
ms_user = Table(
    "ms_user",
    metadata,
    Column("id",GUID,primary_key=True,nullable=False,unique=True,server_default=GUID_SERVER_DEFAULT_POSTGRESQL),
    Column("name",String(256),nullable=False,unique=True),
    Column("email",String(256),nullable=False,unique=True),
    Column("password",String(256),nullable=False),
    Column("role_id",GUID,ForeignKey(ms_role.c.id,ondelete="CASCADE"),nullable=False),
    Column("created_at",DateTime(timezone=True),server_default=func.now()),
    Column("updated_at",DateTime(timezone=True),server_default=func.now(),onupdate=func.now()),
)