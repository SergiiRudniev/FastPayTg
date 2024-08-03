import requests

class QueueClient:
    def __init__(self, url: str = "waiting_queue_money_transfer:999"):
        self.url = url

    def Confirmation(self, id):
        data = {
            "id": id
        }
        requests.post(f"http://{self.url}/confirmation", json=data)
