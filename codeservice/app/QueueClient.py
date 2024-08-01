import requests

class QueueClient:
    def __init__(self, url: str = "waiting_queue_money_transfer:80"):
        self.url = url

    def Confirmation(self, id):
        data = {
            "id": id
        }
        requests.post(f"https://{self.url}/confirmation", json=data)
