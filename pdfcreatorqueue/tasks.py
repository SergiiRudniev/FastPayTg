from celery_app import app
from pdfCreator import PdfCreator
import logging

@app.task
def add_to_queue(data):
    try:
        logging.info(f"Processing pdf create: recipient_id={data.get("recipient_id")}, amount={data.get("Amount")}, payer_id={data.get("Payerid")}")
        PdfCreator.generate_structured_receipt(data.get("recipient_id"), data.get("Payerid"), data.get("Amount"), "/tmp/receipt.pdf", "/logo.jpg")
    except Exception as e:
        logging.error(f"Error processing pdf create: {e}")
