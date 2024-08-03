import redis

class WaitingPayment:
    def __init__(self):
        self.__redis_client = redis.StrictRedis(host='payment-request-redis', port=6379, db=0)

    def AddPending(self, recipient_id: str, Amount: int, Payerid: str) -> None:
        self.__redis_client.set(Payerid, f"{recipient_id}-{Amount}-{Payerid}", ex=700)