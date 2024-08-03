import ApiDB


class PaySystem:
    def __init__(self):
        self.__ApiDB = ApiDB.ApiDB()

    def GetBalance(self, Id: str) -> dict | None:
        response = self.__ApiDB.Get(Id)
        print("response: ", response)
        if response == None:
            print("creating")
            print(self.__ApiDB.Set(str(Id), str(0)))
            return self.__ApiDB.Get(Id)
        return response
