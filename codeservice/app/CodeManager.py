import random
import string

import redis

from Notificator import Notificator
from QueueClient import QueueClient


class CodeManager:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='payment-code-redis', port=6379, db=0)
        self.notificator = Notificator()
        self.QueueClient = QueueClient()

    def __GenerateUniqueCode(self, length=6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def __SetCode(self, id, code):
        try:
            self.redis_client.set(f"code_{id}", code, ex=60)
            self.redis_client.set(f"attempts_{id}", 0, ex=60)
            return {"status": "ok"}
        except Exception as e:
            return {"status": "error", "error": e}

    def __AddAttempts(self, id):
        self.redis_client.set(f"attempts_{id}", self.redis_client.get(f"attempts_{id}") + 1)

    def __GetCode(self, id):
        return self.redis_client.get(f"code_{id}"), self.redis_client.get(f"attempts_{id}")

    def __DeleteCode(self, id):
        self.redis_client.delete(f"code_{id}")
        self.redis_client.delete(f"attempts_{id}")

    def CreateCode(self, id):
        try:
            code = self.__GenerateUniqueCode()
            response = self.__SetCode(id, code)
            if response.get("status") == "ok":
                Notificator.SendCode(id, code)
        except Exception as e:
            return {"Status": "error", "error": e}

    def CheckCode(self, id, InputCode):
        code, attempts = self.__GetCode(id)
        if code == InputCode:
            self.__DeleteCode(id)
            self.QueueClient.Confirmation(id)
            return True

        self.__AddAttempts(id)
        if (attempts + 1) >= 3:
            self.__DeleteCode(id)
            return {"Status:": "warning", "warning": "The code has expired"}
