FROM python:3.6
MAINTAINER Opendata Stuttgart

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /opt/code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY devops/docker/web/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

WORKDIR /opt/code/feinstaub

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["gunicorn", "feinstaub.wsgi:application", "--log-level=info", "--bind", "0.0.0.0:8000", "-w", "3"]
