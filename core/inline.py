from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("YouTube", callback_data="menu_1"),
    InlineKeyboardButton("Instagram", callback_data="menu_2"),
    InlineKeyboardButton("Прочее ...", callback_data="menu_3"),
    InlineKeyboardButton("delete menu", callback_data="del")

)

other = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Telegram", callback_data="other_1"),
    InlineKeyboardButton("WhatsApp", callback_data="other_2"),
    InlineKeyboardButton("Menu", callback_data="menu_4"),
)

admin_b = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("users info", callback_data ="users")  #сигнал.звонок users
)

admin_push = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("add admin push", callback_data="add_p"),
    InlineKeyboardButton("delete admin push", callback_data="del_p"),
)
