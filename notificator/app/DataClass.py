from pydantic import BaseModel

class SendCodeRequest(BaseModel):
    chat_id: int
    code: str

class SuccessfullyMoneyTransferRequest(BaseModel):
    chat_id: int
    amount: int
    recipient_id: int

class UnsuccessfullyMoneyTransferRequest(BaseModel):
    chat_id: int
    amount: int
    recipient_id: int