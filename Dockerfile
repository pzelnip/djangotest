FROM alpine:latest

WORKDIR /deploy/app/

RUN apk add --no-cache --update \
    python3 \
    nginx \
    supervisor \
    uwsgi-python3

RUN python3 -m ensurepip
RUN pip3 install --upgrade pip

# Setup supervisor
RUN mkdir -p /var/log/supervisor/conf.d
COPY conf/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup nginx
RUN mkdir -p /run/nginx \
    && mkdir -p /etc/nginx/sites-available \
    && mkdir -p /etc/nginx/sites-enabled
COPY conf/nginx/djangotest.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/djangotest.conf /etc/nginx/sites-enabled/djangotest.conf
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf

# Setup uwsgi
COPY conf/uwsgi/djangotest.ini /etc/uwsgi/djangotest.ini

# all needed for psycopg2
RUN apk add --no-cache --update \
    postgresql-dev \
    gcc \
    python3-dev \
    libc-dev

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

RUN apk del \
    gcc \
    python3-dev \
    libc-dev

COPY djangotest /deploy/app/djangotest
COPY manage.py /deploy/app/

# Copy static assets
COPY djangotest/static /deploy/app/static

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
