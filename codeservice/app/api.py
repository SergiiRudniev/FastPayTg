from fastapi import FastAPI, HTTPException
import redis
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from CodeManager import CodeManager
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
code_manager = CodeManager()

class CheckCode(BaseModel):
    input_code: str

@app.post("/check_code/{id}")
def check_code(id: str, check_code: CheckCode):
    code_manager.CheckCode(id, check_code)


@app.get("/create_code/{id}")
def create_code(id: str):
    code_manager.CreateCode(id)


