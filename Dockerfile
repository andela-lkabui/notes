FROM python:3.7.6-alpine3.11

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "manage.py", "runserver:8080"]