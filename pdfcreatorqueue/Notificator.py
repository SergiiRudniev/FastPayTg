import requests


class Notificator:
    def __init__(self):
        self.url = "notificator:345"

    def SendPhoto(self, chat_id, photo):
        data = {
            "chat_id": chat_id,
            "amount": amount,
            "recipient_id": recipient_id

        }
        requests.post(f"http://{self.url}//receiving_the_money", json=data)
