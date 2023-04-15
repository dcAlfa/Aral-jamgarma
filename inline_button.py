from config import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# 1-usul.
link_button = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text=tarqat,switch_inline_query=f"\nOrol dengizini qutqaraylik\n"
                                                             f"Iloji boricha tarqating!\n"
                                                             f"{link}"),
    ],
])


Video = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text=" 👁 Orol dengizi haqida 👁",web_app = WebAppInfo(url = "https://www.youtube.com/watch?v=Kr9_2ep28g8&feature=youtu.be&ab_channel=KunUZ")),
    ],
])
