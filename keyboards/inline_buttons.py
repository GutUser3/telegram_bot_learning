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
    form_start_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start_form"
    )
    report_button = InlineKeyboardButton(
        "Report user",
        callback_data="report_user"
    )
    markup.add(questionnaire_button).add(form_start_button).add(report_button)
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

async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )

    markup.add(
        profile_button
    )
    return markup