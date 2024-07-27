from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from PaySystem import PaySystem

app = FastAPI()
pay_system = PaySystem()
secret_key = "zxjkckOKASodlzxkcl,(!@9lskadlZ<X>C'lqwpel9102okLZXKCl,m.kALWKE(IPXZC:k;as,dlkkX(ZI("

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SendData(BaseModel):
    PayerId: str
    Amount: int

@app.post("/api/send/{recipient}")
def Send(recipient: str, SendData: SendData):
    response = pay_system.Send(recipient, SendData.PayerId, SendData.Amount)
    if response == True:
        return {"status": f"ok"}
    raise HTTPException(status_code=403, detail="Pay Error")


@app.get("/api/getbalance/{id}")
def GetBalance(id: str):
    return pay_system.GetBalance(id)

