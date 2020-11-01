from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback


pgs_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='pgs_zernovoi', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Влажность',
                                 callback_data=menu_callback.new(button_name='pgs_vlaga', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Содержание пыли',
                                 callback_data=menu_callback.new(button_name='pgs_dust', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)