from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline_keyboards.callbacks_data import menu_callback


cancel_button = InlineKeyboardButton(text='Отмена',
                                     callback_data='cancel', type='simple')

# main_menu

entry_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Асфальт',
                                 callback_data=menu_callback.new(button_name='asfalt', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Щебень',
                                 callback_data=menu_callback.new(button_name='sheben', type='simple'))
        ],
        [
            InlineKeyboardButton(text='ПГС',
                                 callback_data=menu_callback.new(button_name='pgs', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Грунт',
                                 callback_data=menu_callback.new(button_name='grunt', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Бетон',
                                 callback_data=menu_callback.new(button_name='beton', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Отсев',
                                 callback_data=menu_callback.new(button_name='otsev', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Минеральный порошок',
                                 callback_data=menu_callback.new(button_name='min_por', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструментарий',
                                 callback_data=menu_callback.new(button_name='instruments', type='simple'))
        ]
    ]
)