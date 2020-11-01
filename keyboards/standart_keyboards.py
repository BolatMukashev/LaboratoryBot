from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

get_phone_number = KeyboardButton('Отправить номер', request_contact=True)
get_location = KeyboardButton('Отправить месторасположение', request_location=True)


settings_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True,  # уменьшить размер клавиатуры
    one_time_keyboard=True,  # скрыть после нажатия
    keyboard=[
        ['Показать текущие настройки'],
        ['Изменить максимальную плотность'],
        ['Изменить объем кольца'],
        ['Отмена']
    ]
)

grunt_random_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        ['Мне повезёт!'],
        ['Вернуться в главное меню']
    ]
)
