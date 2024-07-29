import random
import string
import redis

class CodeManager:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='redis-service', port=6379, db=0)

    def GenerateUniqueCode(self, length=6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def SetCode(self, code):
        self.redis_client()
