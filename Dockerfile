# base image  
FROM python:3.8.5-alpine

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD python manage.py collectstatic
CMD python manage.py runserver 0.0.0.0:8000 --insecure
