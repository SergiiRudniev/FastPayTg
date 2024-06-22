FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir pymongo redis

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
