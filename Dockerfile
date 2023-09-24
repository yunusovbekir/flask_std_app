FROM python:3.10-slim

ENV FLASK_APP=src
WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
  build-essential \
  python3-all-dev \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get clean --dry-run

EXPOSE 5000

COPY ./uwsgi.ini /conf/uwsgi.ini
COPY . /code

# Start uWSGI
CMD [ "uwsgi", "--ini", "/conf/uwsgi.ini"]