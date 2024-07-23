import ApiDB


class PayError(BaseException):
    def __str__(self):
        return "Pay Error"


class PaySystem:
    def __init__(self):
        self.__ApiDB = ApiDB.ApiDB()

    def Send(self, recipientId: str, payerId: str, amount: int):
        try:
            SenderCurrentBalance = int(self.__ApiDB.Get(payerId).get("value"))
            RecipientCurrentBalance = int(self.__ApiDB.Get(recipientId).get("value"))
            if SenderCurrentBalance >= amount:
                try:
                    self.__ApiDB.Set(payerId, SenderCurrentBalance - amount)
                    self.__ApiDB.Set(recipientId, RecipientCurrentBalance + amount)
                    return True
                except:
                    self.__ApiDB.Set(payerId, SenderCurrentBalance)
                    self.__ApiDB.Set(recipientId, RecipientCurrentBalance)
                    raise PayError

        except:
            return None

    def GetBalance(self, Id: str):
        response = self.__ApiDB.Get(Id)
        if response is None:
            self.__ApiDB.Set(Id, 0)
            return self.__ApiDB.Get(Id)
        return response
