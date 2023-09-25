from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard

class FormStates(StatesGroup):
    username = State()

async def report_fsm(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Enter a username you want to report"
    )
    await FormStates.username.set()

async def load_username(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
        for_check_user_id = Database().sql_select_id(
            username=data['username']
        )
        if for_check_user_id:
            user_id = for_check_user_id[0][0]
            print(data)
            await bot.send_message(
                chat_id=user_id,
                text="You have been reported"
            )
            await message.reply(
                "User has been successfully reported"
            )
            await state.finish()
        else:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Make sure you typed name correctly",
                reply_markup=await start_keyboard()
            )
            await state.finish()

def register_report_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(report_fsm,
                                       lambda call: call.data == "report_user")
    dp.register_message_handler(load_username, state=FormStates.username,
                                content_types=['text'])
