from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import messagetext

app = FastAPI()
bot_ip = "tgbot"
class SendCodeRequest(BaseModel):
    chat_id: int
    code: str

@app.post("/send_code")
async def send_code(request: SendCodeRequest):
    url = f"http://{bot_ip}/send_message"
    data = {
        "chat_id": request.chat_id,
        "message": messagetext.SendCode(request.code)
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return "ok"
    else:
        raise HTTPException(status_code=500)