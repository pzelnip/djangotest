FROM alpine:latest

WORKDIR /deploy/app/

RUN apk add --no-cache --update \
    python3 \
    nginx \
    supervisor \
    uwsgi-python3

# all needed for psycopg2
RUN apk add --no-cache --update \
    postgresql-dev \
    gcc \
    python3-dev \
    libc-dev

RUN python3 -m ensurepip
RUN pip3 install --upgrade pip

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

RUN apk del \
    gcc \
    python3-dev \
    libc-dev
