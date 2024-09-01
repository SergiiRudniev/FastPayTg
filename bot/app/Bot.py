from fastapi import HTTPException, UploadFile, File

class Bot:
    def __init__(self, logger, bot):
        self.logger = logger
        self.bot = bot
    async def CommandStartHandler(self, message):
        self.logger.info(f"Start Command user: {message.from_user.id}")
        await message.answer(f"Для запуска нажми \"FastPay\"")

    async def SendMessageFromApi(self, request, bot):
        try:
            await bot.send_message(chat_id=request.chat_id, text=request.message)
            return {"status": "success", "message": "Message sent"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def SendFile(self,chat_id, file: UploadFile = File(...)):
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())
        await self.send_pdf_to_user(file_location, chat_id)

        return {"info": f"file '{file.filename}' saved"}

    async def send_pdf_to_user(self, file_path: str, chat_id):
        with open(file_path, 'rb') as file:
            await self.bot.send_document(chat_id=chat_id, document=file)