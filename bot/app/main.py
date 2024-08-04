import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv
import sys
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from Bot import Bot as AnswerBot
import DataClass

load_dotenv()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

bot = None
dp = Dispatcher()
app = FastAPI()
answer_bot = AnswerBot(logger)

@app.post("/send_message")
async def send_message(request: DataClass.SendMessageRequest):
    try:
        await answer_bot.SendMessageFromApi(request, bot)
    except BaseException as e:
        print(e)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await answer_bot.CommandStartHandler(message)

async def start_bot():
    global bot
    bot = Bot(token=getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    logger.info("Bot Started!")
    await dp.start_polling(bot)

async def start_api():
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=222, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    bot_task = asyncio.create_task(start_bot())
    api_task = asyncio.create_task(start_api())
    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(main())
