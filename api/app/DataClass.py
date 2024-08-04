from pydantic import BaseModel

class SendDataRequest(BaseModel):
    PayerId: str
    Amount: int


class CheckCodeRequest(BaseModel):
    InputCode: str