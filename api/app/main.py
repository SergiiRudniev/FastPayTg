import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import config
from PaySystem import PaySystem
from WaitingPayment import WaitingPayment
from ApiDB import ApiDB

app = FastAPI()
pay_system = PaySystem()
waiting_payment = WaitingPayment()
secret_key = "zxjkckOKASodlzxkcl,(!@9lskadlZ<X>C'lqwpel9102okLZXKCl,m.kALWKE(IPXZC:k;as,dlkkX(ZI("
api_db = ApiDB()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SendDataRequest(BaseModel):
    PayerId: str
    Amount: int


class CheckCodeRequest(BaseModel):
    InputCode: str


@app.post("/api/send/{recipient_id}")
def send(recipient_id: str, SendData: SendDataRequest) -> dict:
    try:
        waiting_payment.AddPending(recipient_id, SendData.Amount, SendData.PayerId)
        requests.get(f"http://{config.codeservice_url}/create_code/{SendData.PayerId}")
        return {"status": f"ok"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail="Pay Error")

@app.get("/api/getbalance/{id}")
def get_balance(id: str) -> dict | None:
    return pay_system.GetBalance(id)


@app.post("/api/check_code/{id}")
def check_code(id: str, CheckCode: CheckCodeRequest) -> dict:
    data = {
        "input_code": CheckCode.InputCode
    }
    response = requests.post(f"http://{config.codeservice_url}/check_code/{id}", json=data)
    return response.json()

@app.get("/api/setmoney/{id}/{amount}")
def setmoney(id: str, amount: str):
    api_db.Set(id, amount)