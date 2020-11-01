from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback


instructions_main_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Инструкции для асфальта',
                                 callback_data=menu_callback.new(button_name='instruction_asphalt', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для щебня',
                                 callback_data=menu_callback.new(button_name='instruction_sheben', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для ПГС',
                                 callback_data=menu_callback.new(button_name='instruction_pgs', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для грунта',
                                 callback_data=menu_callback.new(button_name='instruction_grunt', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для бетона',
                                 callback_data=menu_callback.new(button_name='instruction_beton', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для отсева',
                                 callback_data=menu_callback.new(button_name='instruction_otsev', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Инструкции для минерального порошка',
                                 callback_data=menu_callback.new(button_name='instruction_mp', type='simple'))
        ]
    ]
)