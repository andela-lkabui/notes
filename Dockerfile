FROM python:3.7

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8080

# pg_ready command is installed through this package.
# The command will be used to poll the "db" container to check if postgres is
# ready to accept connections. When ready, migrations will be run.
RUN apt-get update && apt-get install -f -y postgresql-client

RUN chown root:root /code/docker-entrypoint.sh && chmod 755 /code/docker-entrypoint.sh

ENTRYPOINT /code/docker-entrypoint.sh