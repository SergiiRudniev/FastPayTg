from tasks import add_to_queue
import redis
import logging

class RequestsHandler:
    def __init__(self) -> None:
        self.redis_client = redis.StrictRedis(host='payment-request-redis', port=6379, db=0)

    def _parse_payment_data(self, data: str) -> dict:
        raw_data = data.split("-")
        return {
            "recipient_id": raw_data[0],
            "Amount": raw_data[1],
            "Payerid": raw_data[2]
        }

    def _send_data_to_queue(self, data: dict) -> None:
        try:
            add_to_queue.delay(data)
        except Exception as e:
            logging.error(e)
    def confirmation(self, payer_id: str) -> dict:
        #pay_data = self._parse_payment_data(self.redis_client.get(payer_id).decode())
        pay_data = self._parse_payment_data("123123123-1600-399539593")
        self._send_data_to_queue(pay_data)
        #self.redis_client.delete(payer_id)
        return {"status": "ok"}