FROM python:3.12-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn gunicorn redis requests pika

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
