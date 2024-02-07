from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(os.path.join(BASE_DIR,"src"))
SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DB = os.getenv("SQL_DB")
SQL_URL = f"postgresql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}"
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url",SQL_URL)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from src.role.models import metadata as role_metadata
from src.food_category.models import metadata as food_category_metadata
from src.restaurant.models import metadata as restaurant_metadata
from src.food.models import metadata as food_metadata
from src.user.models import metadata as user_metadata
from src.food_log.models import metadata as food_log_metadata
from src.order_and_payments.models import metadata as order_and_payments_metadata
from src.payment_acceptance_log.models import metadata as payment_acceptance_log_metadata
from src.food_transactions.models import metadata as food_transactions_metadata


target_metadata = [
    role_metadata,
    food_category_metadata,
    restaurant_metadata,
    food_metadata,
    user_metadata,
    food_log_metadata,
    order_and_payments_metadata,
    payment_acceptance_log_metadata,
    food_transactions_metadata
]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
