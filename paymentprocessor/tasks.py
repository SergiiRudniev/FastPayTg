from celery_app import app
from PaySystem import PaySystem
import logging
from Notificator import Notificator

pay_system = PaySystem()
notificator = Notificator()

@app.task
def add_to_queue(data):
    print(f"Worker processing data: {data}")
    try:
        logging.info(f"Processing payment: recipient_id={data.get("recipient_id")}, amount={data.get("Amount")}, payer_id={data.get("Payerid")}")
        response = pay_system.Send(str(data.get("recipient_id")), str(data.get("Payerid")), int(data.get("Amount")))
        if response != None:
            notificator.SendSuccessfullyMoneyTransfer(int(data.get("Payerid")), int(data.get("Amount")), int(data.get("recipient_id")))
            notificator.SendReceivingTheMoney(int(data.get("Payerid")), int(data.get("Amount")), int(data.get("recipient_id")))
        else:
            notificator.SendUnsuccessfullyMoneyTransfer(int(data.get("Payerid")), int(data.get("Amount")),
                                                        int(data.get("recipient_id")))
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
        notificator.SendUnsuccessfullyMoneyTransfer(int(data.get("Payerid")), int(data.get("Amount")),
                                                  int(data.get("recipient_id")))
