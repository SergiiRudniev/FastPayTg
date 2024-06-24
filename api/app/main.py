from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PayerId(BaseModel):
    id: str

@app.post("/api/pay/{recipient}")
def set_value(recipient: int, PayerID: PayerId):
    payerId = PayerID.id
    return {"status": f"ok"}


@app.get("/api/getbalance/{id}")
def get_value(id: str):
    response = requests.get(f"http://db/get/{id}")
    if response.status_code == 404:
        response = requests.post(f"http://db/set/{id}", json={"value": 0}, headers={"Content-Type": "application/json"})
        response = requests.get(f"http://db/get/{id}")
        data = response.json()
        return data
    else:
        data = response.json()
        return data

