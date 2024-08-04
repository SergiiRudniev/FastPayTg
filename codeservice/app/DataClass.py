from pydantic import BaseModel


class CheckCodeRequest(BaseModel):
    input_code: str
