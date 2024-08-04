from fastapi import HTTPException

class Bot:
    def __init__(self, logger):
        self.logger = logger

    async def CommandStartHandler(self, message):
        self.logger.info(f"Start Command user: {message.from_user.id}")
        await message.answer(f"Для запуска нажми \"FastPay\"")

    async def SendMessageFromApi(self, request, bot):
        try:
            await bot.send_message(chat_id=request.chat_id, text=request.message)
            return {"status": "success", "message": "Message sent"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))