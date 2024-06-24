import asyncio


class PaySystem:
    def __init__(self):
        self.PaymentQueue = PaymentQueue()
        self.IsPaymentQueueWork = False

    def Pay(self, payerId: int, recipientId: int, amount: float):
        self.PaymentQueue.Append(payerId, recipientId, amount)

    def StartQueue(self):
        asyncio.run()

    def StopQueue(self):
        ...



class PaymentQueue:
    def __init__(self):
        self.__PaymentQueue = []

    def Append(self, payerId: int, recipientId: int, amount: float):
        self.__PaymentQueue.append({"payerId": payerId, "recipientId": recipientId, "amount": amount})

    def NowOperation(self):
        return self.__PaymentQueue[0]

