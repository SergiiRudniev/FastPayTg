import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv
import sys
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

bot = None
dp = Dispatcher()

app = FastAPI()

class SendMessageRequest(BaseModel):
    chat_id: int
    message: str

@app.post("/send_message")
async def send_message(request: SendMessageRequest):
    try:
        await bot.send_message(chat_id=request.chat_id, text=request.message)
        return {"status": "success", "message": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    logger.info(f"Start Command user: {message.from_user.id}")
    await message.answer(f"Для запуска нажми \"FastPay\"")


async def main() -> None:
    global bot
    bot = Bot(token=getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    logger.info(f"Bot Started!")
    await dp.start_polling(bot)

asyncio.run(main())