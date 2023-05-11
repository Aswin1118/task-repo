FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["gunicorn", "--bind", "0.0.0.0:80", "list:app"]