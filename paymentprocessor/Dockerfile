FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir redis celery requests

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
