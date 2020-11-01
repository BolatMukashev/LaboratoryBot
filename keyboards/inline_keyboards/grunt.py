from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback


grunt_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Уплотнение грунта',
                                 callback_data=menu_callback.new(button_name='grunt_plotnost', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='grunt_zernovoi', type='simple'))
        ],
        [
            InlineKeyboardButton(text='ПСУ',
                                 callback_data=menu_callback.new(button_name='grunt_psu', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Проктор',
                                 callback_data=menu_callback.new(button_name='grunt_proctor', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить параметры',
                                 callback_data=menu_callback.new(button_name='grunt_settings', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)


grunt_settings_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Показать текущие настройки',
                                 callback_data=menu_callback.new(button_name='grunt_settings_view', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить значение максимальной плотности',
                                 callback_data=menu_callback.new(button_name='grunt_edit_max_pl', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить объем кольца',
                                 callback_data=menu_callback.new(button_name='grunt_edit_v_ring', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Установить значения по умолчанию',
                                 callback_data=menu_callback.new(button_name='grunt_settings_sbros', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_grunt_main_menu', type='simple'))
        ]
    ]
)


grunt_sbros_choise = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сбросить',
                                 callback_data=menu_callback.new(button_name='grunt_sbros_yes', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='grunt_back_to_settings_menu',
                                                                 type='simple'))
        ]
    ]
)