from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import *




button = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text=jamgarma),
            KeyboardButton(text=orol),
        ],
        [
            KeyboardButton(text=about),
            KeyboardButton(text=tarqat),
        ],
    ],
    resize_keyboard=True
)