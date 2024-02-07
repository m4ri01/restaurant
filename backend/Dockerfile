FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app
COPY . .
RUN mkdir -p /app/alembic/versions
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt update && apt install -y postgresql-client
ARG PORT=80
EXPOSE ${PORT}

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
