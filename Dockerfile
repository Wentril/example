# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

ENV AM_I_IN_A_DOCKER_CONTAINER Yes
ENV FASTAPI_HOST "0.0.0.0"
ENV FASTAPI_PORT 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
