from celery import Celery

app = Celery('WaitingQueueMoneyTransfer', broker='redis://pdfcreator-queue-redis:6379/0', backend='redis://payment-queue-redis:6379/0')

app.conf.update(
    result_backend='redis://pdfcreator-queue-redis:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
