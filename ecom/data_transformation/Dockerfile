FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

CMD ["python3", "run.py"]