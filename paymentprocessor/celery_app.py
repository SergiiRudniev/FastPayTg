from celery import Celery

app = Celery('PaymentProcessor', broker='redis://payment-queue-redis:6379/0')

app.conf.update(
    result_backend='redis://payment-queue-redis:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
