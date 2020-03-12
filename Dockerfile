FROM python:3.7

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8080

RUN chown root:root /code/docker-entrypoint.sh && chmod 755 /code/docker-entrypoint.sh

ENTRYPOINT /code/docker-entrypoint.sh