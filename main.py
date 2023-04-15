import logging
import random
from config import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from button import *
from inline_button import *



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/rasm.jpg")
    await message.answer_photo(photo_file,caption=f"Assalomu alaykum\n{Tarif}",reply_markup=button)



@dp.message_handler(text = jamgarma)
async def send_jamgarma(message: types.Message):
    album = types.MediaGroup()
    visa = InputFile(path_or_bytesio="images/visa.jpg")
    humo = InputFile(path_or_bytesio="images/humo.jpg")
    uzcard = InputFile(path_or_bytesio="images/uzcard.png")
    card = InputFile(path_or_bytesio="images/card.jpg")
    album.attach_photo(photo=humo)
    album.attach_photo(photo=visa)
    album.attach_photo(photo=uzcard)
    album.attach_photo(photo=card)
    await message.answer_media_group(media=album)
    await message.answer(jam)


@dp.message_handler(text = orol)
async def send_jamgarma(message: types.Message):
    a = random.randint(1,6)
    rasm = InputFile(path_or_bytesio=f"photo/{a}.jpg")
    await message.answer_photo(rasm)


@dp.message_handler(text = about)
async def send_jamgarma(message: types.Message):
    await message.answer(abouts,reply_markup=Video)



@dp.message_handler(text = tarqat)
async def send_jamgarma(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/rasm.jpg")
    await message.answer_photo(photo_file,reply_markup=link_button)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)