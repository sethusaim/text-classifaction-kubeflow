FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

# RUN apt update -y && apt install awscli -y && pip install -r requirements.txt

RUN apt update -y && apt install awscli -y

CMD ["python3", "run.py"]