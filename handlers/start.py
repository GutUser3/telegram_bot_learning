from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT
from database.sql_commands import Database

async def start_button(message):
    Database().sql_insert_user_command(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT.format(
            username=message.from_user.username
        ),
        parse_mode=types.ParseMode.MARKDOWN
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])