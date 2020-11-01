from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback

min_por_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='мин_пор', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)
