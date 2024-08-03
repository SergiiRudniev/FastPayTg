from celery_app import app
from PaySystem import PaySystem
import logging

pay_system = PaySystem()


@app.task
def add_to_queue(data):
    print(f"Worker processing data: {data}")
    try:
        logging.info(f"Processing payment: recipient_id={data.get("recipient_id")}, amount={data.get("Amount")}, payer_id={data.get("Payerid")}")
        pay_system.Send(str(data.get("recipient_id")), str(data.get("Payerid")), int(data.get("Amount")))
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
