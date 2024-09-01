FROM python:3.12

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn gunicorn aiogram python-dotenv python-multipart

CMD ["python", "main.py"]
