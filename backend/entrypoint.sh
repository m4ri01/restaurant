#!/usr/bin/env bash
sleep 10
alembic revision --autogenerate
alembic upgrade head
python src/main.py