from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton  


regictration = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Зарегистрироваться", request_contact=True),
)

profile = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Профиль"),
)

