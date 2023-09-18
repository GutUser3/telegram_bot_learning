from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

GROUP_ID = -4045867533
MY_DIRECTORY = "\\Users\Silicon Machine\Desktop\Puro\Telegram_bot\media"
