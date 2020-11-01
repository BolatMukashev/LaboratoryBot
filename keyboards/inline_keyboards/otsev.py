from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline_keyboards.callbacks_data import menu_callback


otsev_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='отсев_зерновой', type='standart'))
        ],
        [
            InlineKeyboardButton(text='Зерновой состав, Mod',
                                 callback_data=menu_callback.new(button_name='отсев_зерновой', type='mod'))
        ],
        [
            InlineKeyboardButton(text='Влажность',
                                 callback_data=menu_callback.new(button_name='otsev_vlaga', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Содержание пыли',
                                 callback_data=menu_callback.new(button_name='otsev_dust', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Настройки',
                                 callback_data=menu_callback.new(button_name='otsev_settings', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)