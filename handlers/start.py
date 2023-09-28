from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot
from const import START_TEXT
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard

async def start_button(message: types.Message):
    print(message.get_full_command())
    command = message.get_full_command()
    await bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT.format(
            username=message.from_user.username
        ),
        parse_mode=types.ParseMode.MARKDOWN,
        reply_markup=await start_keyboard()
    )

    if command[1]:
        print(command)
        existed_user = Database().sql_select_user_command(
            telegram_id=message.from_user.id
        )
        print(existed_user)
        link_generate = await _create_link(link_type="start", payload=command[1])
        print(link_generate)
        if not existed_user:
            owner = Database().sql_select_owner_by_link_command(
                link=link_generate
            )
            print(owner)
            Database().sql_insert_user_command(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
            )
            Database().sql_insert_reference_user_command(
                owner=owner[0]['telegram_id'],
                referral=message.from_user.id,
            )
    else:
        Database().sql_insert_user_command(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        print(message)
def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])