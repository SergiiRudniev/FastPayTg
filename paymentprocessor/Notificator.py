import requests


class Notificator:
    def __init__(self):
        self.url = "notificator:345"

    def SendSuccessfullyMoneyTransfer(self, chat_id, amount, recipient_id):
        data = {
            "chat_id": chat_id,
            "amount": amount,
            "recipient_id": recipient_id,
        }
        requests.post(f"http://{self.url}/successfully_money_transfer", json=data)

    def SendUnsuccessfullyMoneyTransfer(self, chat_id, amount, recipient_id):
        data = {
            "chat_id": chat_id,
            "amount": amount,
            "recipient_id": recipient_id
        }
        requests.post(f"http://{self.url}/unsuccessfully_money_transfer", json=data)

    def SendReceivingTheMoney(self, chat_id, amount, recipient_id):
        data = {
            "chat_id": chat_id,
            "amount": amount,
            "recipient_id": recipient_id

        }
        requests.post(f"http://{self.url}//receiving_the_money", json=data)
