from fastapi import FastAPI
import DataClass
from BotApi import BotApi
import config
import messagetext

app = FastAPI()
bot_api = BotApi(config.bot_ip)

@app.post("/send_code")
async def send_code(request: DataClass.SendCodeRequest):
    return bot_api.SendMessage(request, messagetext.SendCode(request.code))

@app.post("/successfully_money_transfer")
async def successfully_money_transfer(request: DataClass.SuccessfullyMoneyTransferRequest):
    return bot_api.SendMessage(request, messagetext.SuccessfullyMoneyTransfer(request.recipient_id, request.amount))

@app.post("/unsuccessfully_money_transfer")
async def unsuccessfully_money_transfer(request: DataClass.UnsuccessfullyMoneyTransferRequest):
    return bot_api.SendMessage(request, messagetext.UnsuccessfullyMoneyTransfer(request.recipient_id, request.amount))


@app.post("/receiving_the_money")
async def receiving_the_money(request: DataClass.ReceivingTheMoneyRequest):
    return bot_api.SendMessage(request, messagetext.ReceivingTheMoney(request.amount, request.recipient_id))