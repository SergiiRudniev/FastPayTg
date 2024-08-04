from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import DataClass
import config
from ApiDB import ApiDB
from CodeApi import CodeApi
from PaySystem import PaySystem
from WaitingPayment import WaitingPayment

app = FastAPI()
pay_system = PaySystem()
waiting_payment = WaitingPayment()
api_db = ApiDB()
code_api = CodeApi(config.codeservice_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/send/{recipient_id}")
def send(recipient_id: str, SendData: DataClass.SendDataRequest) -> dict:
    print("____send_requests____")
    try:
        print("_____add__pending_____")
        waiting_payment.AddPending(recipient_id, SendData.Amount, SendData.PayerId)
        print("_____Create_Code_____")
        code_api.CreateCode(SendData.PayerId)
        print("____return____")
        return {"status": f"ok"}
    except Exception as e:
        print("____error____")
        print(e)
        raise HTTPException(status_code=403, detail="Pay Error")


@app.get("/api/getbalance/{id}")
def get_balance(id: str) -> dict | None:
    return pay_system.GetBalance(id)


@app.post("/api/check_code/{id}")
def check_code(id: str, CheckCode: DataClass.CheckCodeRequest) -> dict:
    return code_api.CheckCode(id, CheckCode.InputCode).json()


@app.get("/api/setmoney/{id}/{amount}")  # For Test
def setmoney(id: str, amount: str):
    api_db.Set(id, amount)
