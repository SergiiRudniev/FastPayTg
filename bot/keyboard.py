from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import WebAppInfo
import config

def Start():
    global StartKeyBoards
    StartKey = KeyboardButton(text="Start", web_app=WebAppInfo(url=config.ngrok_link))
    StartKeyBoards = ReplyKeyboardMarkup(keyboard=[[StartKey]], resize_keyboard=True)