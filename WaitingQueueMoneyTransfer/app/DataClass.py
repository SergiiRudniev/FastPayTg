from pydantic import BaseModel

class ConfirmationRequest(BaseModel):
    id: str