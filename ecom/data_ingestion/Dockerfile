FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

ARG MONGO_DB_URL

ENV MONGO_DB_URL $MONGO_DB_URL

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]