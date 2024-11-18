FROM python:3.11.9-slim-bookworm AS app
LABEL maintainer="Maamoun Haj Najeeb <maamoun.haj.najeeb@gmail.com>"

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/app
