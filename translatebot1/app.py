from googletrans import Translator
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6933219269:AAG43sSwhUEOxndWdkG0j0qcND946c9agbs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
transaltor = Translator()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum va rahmatillohu va barakatuh.\nTarjimon botimizga hush kelibsiz")



@dp.message_handler()
async def get_data(message: types.Message):

    translation = transaltor.translate(message.text, dest='en')
    translated_text = translation.text
    await message.reply(translated_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
