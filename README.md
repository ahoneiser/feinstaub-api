# feinstaub-api ![Continuous Integration](https://github.com/ahoneiser/feinstaub-api/workflows/Continuous%20Integration/badge.svg)

django webservice to store data from Feinstaub-Sensors (more info at [lufdaten.info])

## Notes

* checkout daily CSV dumps in the [lufdaten.info archive]

## Development Setup

### docker-compose

to use docker-compose for local development, follow these steps:

* make sure to have Docker & docker-compose installed on your Development Machine :wink:
* clone this [repository], and use `docker-compose up` to start a Development Environment
* docker-compose will start a postgres DB for you, django migrations will be executed on container startup :sunglasses:

## Production Setup

### docker

to run *feinstaub-api* on a Docker Host for production, follow these steps:

```
# build the app image
docker build -t feinstaub-api:${YOUR_TAG_NAME_HERE} devops/docker/app/app.Dockerfile

# create a dedicated docker network
docker network create feinstaub-api

# run a postgres db container
docker run --restart=unless-stopped --network feinstaub-api --name postgres -e POSTGRES_USER=${YOUR_DB_USERNAME_HERE} -e POSTGRES_PASSWORD=${YOUR_DB_PASSWORD_HERE} -e POSTGRES_DB=feinstaub -e PGDATA=/var/lib/postgresql/data/pgdata -v feinstaub-data:/var/lib/postgresql/data -p 5432:5432 -td postgres:9.6

# run the actual app container
docker run --network feinstaub-api --restart=unless-stopped --name app -v feinstaub-static-root:/opt/code/feinstaub/static-root -e DB_HOST=postgres -e DB_PORT=5432 -e DB_NAME=feinstaub -e DB_USER=${YOUR_DB_USERNAME_HERE} -e DB_PASSWORD=${YOUR_DB_PASSWORD_HERE} -e ALLOWED_HOSTS=${YOUR_ALLOWED_HOSTS_ENTRIES_HERE} -p 8000:8000 -td feinstaub-api:${YOUR_TAG_NAME_HERE}

# run a nginx container to serve assets
docker run --rm --restart=unless-stopped --name nginx --network feinstaub-api -v feinstaub-static-root:/var/www/htdocs/static-root:ro -v $(pwd)/devops/docker/nginx/vhost.conf:/etc/nginx/conf.d/default.conf -p 80:80 -td nginx:latest
```

> :exclamation: note that this will expose the webservice on port 80, use a reverse proxy to serve the application with HTTPS

[lufdaten.info]: https://luftdaten.info/
[luftdaten.info archive]: http://archive.luftdaten.info/
