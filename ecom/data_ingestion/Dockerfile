FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

ARG MONGODB_URL

ENV MONGODB_URL $MONGODB_URL

RUN apt update -y && apt install awscli -y && pip install -r requirements.txt

CMD ["python3", "run.py"]