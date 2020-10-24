FROM python:3.8.6

MAINTAINER Opendata Stuttgart

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
  apt-get install -y postgresql-client

RUN apt-get clean && \
  rm -rf /var/cache/apt/lists/*

RUN pip install --no-cache-dir poetry

WORKDIR /opt/code

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
  poetry install --no-interaction

COPY . .

COPY devops/docker/app/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

WORKDIR /opt/code/feinstaub

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["gunicorn", "feinstaub.wsgi:application", "--log-level=info", "--bind", "0.0.0.0:8000", "-w", "3"]
