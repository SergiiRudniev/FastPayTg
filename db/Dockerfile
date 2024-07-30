FROM python:3.12-alpine3.19

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn gunicorn pymongo redis requests

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
