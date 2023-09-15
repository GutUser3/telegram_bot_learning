from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def question_first_keyboard():
    markup = InlineKeyboardMarkup()
    male_button = InlineKeyboardButton(
        "Male",
        callback_data="answered_male"
    )
    female_button = InlineKeyboardButton(
        "Female",
        callback_data="answered_female"
    )
    markup.add(male_button).add(female_button)
    return markup