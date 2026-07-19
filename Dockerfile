FROM python:3.14.6-alpine

RUN apk add --no-cache docker-cli docker-cli-compose

WORKDIR /tgws-web/app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN rm -rf /app/*
COPY . /tgws-web

# Запускаем скрипт
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
