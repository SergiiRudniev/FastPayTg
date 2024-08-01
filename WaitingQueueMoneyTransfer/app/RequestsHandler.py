import json

import pika
import redis


class RequestsHandler:
    def __init__(self) -> None:
        self.redis_client = redis.StrictRedis(host='payment-request-redis', port=6379, db=0)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='ready_to_process')

    def __ParsePaymentData(self, data: str) -> dict:
        RawData = data.split("-")
        return {"recipient_id": RawData[0], "Amount": RawData[1], "Payerid": RawData[2]}

    def __SendDataToQueue(self, data: dict) -> None:
        message = json.dumps({
            "recipient_id": data.get("recipient_id"),
            "Amount": data.get("Amount"),
            "Payerid": data.get("Payerid")
        })
        self.channel.basic_publish(exchange='', routing_key='ready_to_process', body=message)

    def Confirmation(self, PayerId: str) -> dict:
        try:
            PayData = self.__ParsePaymentData(self.redis_client.get(PayerId))
            self.redis_client.delete(PayerId)
            self.__SendDataToQueue(PayData)
            return {"status": f"ok"}
        except Exception as e:
            return {"status": "error", "error": e}
