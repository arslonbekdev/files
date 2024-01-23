import wikipedia
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6644151680:AAFcbvpWmy-cSC-4c0J9F0VScbPPhBQaVO8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#wikipedia.set_lang("uz")


@dp.message_handler(commands=['start', 'help'])
async def hello(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum \nWikippedia botimizga xush kelibsiz.\nMatningizni yuboring.")



@dp.message_handler()
async def get_data(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:

        matn = message.text
        await message.answer(wikipedia.summary(matn))
    except:
        await message.answer("Bunday ma'lumot mavjud emas")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
