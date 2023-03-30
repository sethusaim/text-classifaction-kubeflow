FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

CMD ["python3", "run.py"]