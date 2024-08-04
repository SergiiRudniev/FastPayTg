from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from RequestsHandler import RequestsHandler
import DataClass

app = FastAPI()
requests_handler = RequestsHandler()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/confirmation")
def confirmation(confirmation_data: DataClass.ConfirmationRequest) -> dict:
    requests_handler.confirmation(confirmation_data.id)
    return {"success": True}