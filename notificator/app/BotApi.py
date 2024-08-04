import requests
import messagetext
from fastapi import HTTPException
class BotApi:
    def __init__(self, url: str = "tgbot:222"):
        self.url = url

    def SendMessage(self, request, message):
        print('New Requests')
        url = f"http://{self.url}/send_message"
        data = {
            "chat_id": request.chat_id,
            "message": message
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            return "ok"
        else:
            raise HTTPException(status_code=500)