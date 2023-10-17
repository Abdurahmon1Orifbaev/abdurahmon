from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)

phone_number_back_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga", request_contact=True),
            KeyboardButton(text="☎️ Telefon raqamni jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lokatsiya jo'natish", request_location=True)
        ]
    ], resize_keyboard=True
)
