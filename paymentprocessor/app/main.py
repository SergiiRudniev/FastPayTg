import pika
import json
from PaySystem import PaySystem


pay_system = PaySystem()
def process_payment(ch, method, properties, body):
    message = json.loads(body.decode())
    recipient_id = message['recipient_id']
    Amount = message['Amount']
    Payerid = message["Payerid"]
    pay_system.Send(recipient_id, Payerid, Amount)




connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='ready_to_process')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='ready_to_process', on_message_callback=process_payment)

channel.start_consuming()
