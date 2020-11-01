from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback


sheben_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='sheben_zernovoi', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Влажность',
                                 callback_data=menu_callback.new(button_name='sheben_vlaga', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Содержание пыли',
                                 callback_data=menu_callback.new(button_name='sheben_dust', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Настройки',
                                 callback_data=menu_callback.new(button_name='sheben_settings', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)


sheben_zernovoi_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='фр.5-20',
                                 callback_data=menu_callback.new(button_name='щебень', type='5-20'))
        ],
        [
            InlineKeyboardButton(text='фр.5-10',
                                 callback_data=menu_callback.new(button_name='щебень', type='5-10')),
            InlineKeyboardButton(text='фр.10-20',
                                 callback_data=menu_callback.new(button_name='щебень', type='10-20')),
            InlineKeyboardButton(text='фр.10-20(mod)',
                                 callback_data=menu_callback.new(button_name='щебень', type='10-20(mod)'))
        ],
        [
            InlineKeyboardButton(text='фр.20-40',
                                 callback_data=menu_callback.new(button_name='щебень', type='20-40')),
            InlineKeyboardButton(text='фр.40-70',
                                 callback_data=menu_callback.new(button_name='щебень', type='40-70')),
            InlineKeyboardButton(text='фр.40-70(mod)',
                                 callback_data=menu_callback.new(button_name='щебень', type='40-70(mod)'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_sheben_main_menu', type='simple'))
        ]
    ]
)


sheben_settings_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Показать массы у проб',
                                 callback_data=menu_callback.new(button_name='sheben_all_view', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить массу пробы',
                                 callback_data=menu_callback.new(button_name='sheben_set_change', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Сбросить настройки',
                                 callback_data=menu_callback.new(button_name='sheben_settings_reset', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_sheben_main_menu', type='simple'))
        ]
    ]
)


sheben_all_change = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='фр.5-20',
                                 callback_data=menu_callback.new(button_name='sheben_all_ch', type='щебень_5-20'))
        ],
        [
            InlineKeyboardButton(text='фр.5-10',
                                 callback_data=menu_callback.new(button_name='sheben_all_ch', type='щебень_5-10')),
            InlineKeyboardButton(text='фр.10-20',
                                 callback_data=menu_callback.new(button_name='sheben_all_ch', type='щебень_10-20'))
        ],
        [
            InlineKeyboardButton(text='фр.20-40',
                                 callback_data=menu_callback.new(button_name='sheben_all_ch', type='щебень_20-40')),
            InlineKeyboardButton(text='фр.40-70',
                                 callback_data=menu_callback.new(button_name='sheben_all_ch', type='щебень_40-70'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_sheben_set_menu', type='simple'))
        ]
    ]
)


sheben_settings_reset_switch_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сбросить',
                                 callback_data=menu_callback.new(button_name='sheben_set_reset_yes', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='back_to_sheben_set_menu', type='simple'))
        ]
    ]
)
