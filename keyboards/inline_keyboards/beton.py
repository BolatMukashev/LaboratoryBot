from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback

beton_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Прочность',
                                 callback_data=menu_callback.new(button_name='beton_prochnost', type='simple'))
        ],
        [
            InlineKeyboardButton(text='7 и 28 суток',
                                 callback_data=menu_callback.new(button_name='7and28sutok', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Настройки',
                                 callback_data=menu_callback.new(button_name='beton_settings', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)


beton_settings_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Показать текущие значения',
                                 callback_data=menu_callback.new(button_name='beton_settings_view', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить размер кубиков',
                                 callback_data=menu_callback.new(button_name='beton_change_size', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить систему счисления',
                                 callback_data=menu_callback.new(button_name='beton_change_metric', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить тип бетона',
                                 callback_data=menu_callback.new(button_name='beton_change_type', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Изменить влажность (для ячеистых бетонов)',
                                 callback_data=menu_callback.new(button_name='beton_change_w', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Установить значения по умолчанию',
                                 callback_data=menu_callback.new(button_name='beton_settings_sbros', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_beton_main_menu', type='simple'))
        ]
    ]
)


beton_sbros_choise = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сбросить',
                                 callback_data=menu_callback.new(button_name='beton_sbros_yes', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='beton_to_set_menu',
                                                                 type='Сброс отменен.'))
        ]
    ]
)


beton_size_switch = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='70x70',
                                 callback_data=menu_callback.new(button_name='beton_change_size_true', type='70')),
            InlineKeyboardButton(text='100x100',
                                 callback_data=menu_callback.new(button_name='beton_change_size_true', type='100')),
            InlineKeyboardButton(text='150x150',
                                 callback_data=menu_callback.new(button_name='beton_change_size_true', type='150'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='beton_to_set_menu',
                                                                 type='Изменения не внесены'))
        ]
    ]
)


beton_metrics_switch = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='кН',
                                 callback_data=menu_callback.new(button_name='beton_change_metric_true', type='кН')),
            InlineKeyboardButton(text='МПа',
                                 callback_data=menu_callback.new(button_name='beton_change_metric_true', type='МПа')),
            InlineKeyboardButton(text='кГс',
                                 callback_data=menu_callback.new(button_name='beton_change_metric_true', type='кГс'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='beton_to_set_menu',
                                                                 type='Изменения не внесены'))
        ]
    ]
)


beton_types_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Тяжелый',
                                 callback_data=menu_callback.new(button_name='beton_types', type='tyazholii')),
            InlineKeyboardButton(text='Ячеистый',
                                 callback_data=menu_callback.new(button_name='beton_types', type='yacheistii'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='beton_to_set_menu',
                                                                 type='Изменения не внесены'))
        ]
    ]
)


beton_yacheistii_change_w_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='0',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='0')),
            InlineKeyboardButton(text='5',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='5')),
            InlineKeyboardButton(text='10',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='10')),
            InlineKeyboardButton(text='15',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='15')),
            InlineKeyboardButton(text='20',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='20')),
            InlineKeyboardButton(text='25 и более',
                                 callback_data=menu_callback.new(button_name='beton_change_w_true', type='25'))
        ],
        [
            InlineKeyboardButton(text='Отмена',
                                 callback_data=menu_callback.new(button_name='beton_to_set_menu',
                                                                 type='Изменения не внесены'))
        ]
    ]
)