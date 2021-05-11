FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1

COPY . /api
WORKDIR /api

RUN pip3 install --upgrade pip==20.3.4
RUN pip3 install -r requirements.txt