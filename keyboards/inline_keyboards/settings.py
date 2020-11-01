from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback


settings_main_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Показать текущие значения',
                                 callback_data=menu_callback.new(button_name='main_setting_parameters_view',
                                                                 type='simple'))
        ],
        [
            InlineKeyboardButton(text='Дно сита',
                                 callback_data=menu_callback.new(button_name='dno_switch', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Часовой пояс',
                                 callback_data=menu_callback.new(button_name='time_zone', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)


dno_switch_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Учитывать',
                                 callback_data=menu_callback.new(button_name='dno_true', type='True')),
            InlineKeyboardButton(text='Не учитывать',
                                 callback_data=menu_callback.new(button_name='dno_false', type='False'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_settings_buttons', type='simple'))
        ]
    ]
)


time_zone_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-12',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-12')),
            InlineKeyboardButton(text='-11',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-11')),
            InlineKeyboardButton(text='-10',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-10')),
            InlineKeyboardButton(text='-9',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-9')),
            InlineKeyboardButton(text='-8',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-8')),
            InlineKeyboardButton(text='-7',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-7'))

        ],
        [
            InlineKeyboardButton(text='-6',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-6')),
            InlineKeyboardButton(text='-5',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-5')),
            InlineKeyboardButton(text='-4',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-4')),
            InlineKeyboardButton(text='-3',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-3')),
            InlineKeyboardButton(text='-2',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-2')),
            InlineKeyboardButton(text='-1',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='-1')),
        ],
        [
            InlineKeyboardButton(text='0',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='0')),
        ],
        [
            InlineKeyboardButton(text='+1',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='1')),
            InlineKeyboardButton(text='+2',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='2')),
            InlineKeyboardButton(text='+3',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='3')),
            InlineKeyboardButton(text='+4',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='4')),
            InlineKeyboardButton(text='+5',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='5')),
            InlineKeyboardButton(text='+6',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='6'))

        ],
        [
            InlineKeyboardButton(text='+7',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='7')),
            InlineKeyboardButton(text='+8',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='8')),
            InlineKeyboardButton(text='+9',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='9')),
            InlineKeyboardButton(text='+10',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='10')),
            InlineKeyboardButton(text='+11',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='11')),
            InlineKeyboardButton(text='+12',
                                 callback_data=menu_callback.new(button_name='choose_time_zone', type='12'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_settings_buttons', type='simple'))
        ]
    ]
)