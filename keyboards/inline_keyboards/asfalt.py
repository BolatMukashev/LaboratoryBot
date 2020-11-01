from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline_keyboards.callbacks_data import menu_callback

asfalt_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зерновой состав',
                                 callback_data=menu_callback.new(button_name='asfalt_zernovoi', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Средняя плотность',
                                 callback_data=menu_callback.new(button_name='asfalt_plotnost', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Расчитать подбор',
                                 callback_data=menu_callback.new(button_name='asfalt_podbor', type='simple'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_entry_button', type='simple'))
        ]
    ]
)

asfalt_zernovoi_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='крупный, тип А',
                                 callback_data=menu_callback.new(button_name='асфальт', type='крупный, тип А')),
            InlineKeyboardButton(text='крупный, тип Б',
                                 callback_data=menu_callback.new(button_name='асфальт', type='крупный, тип Б'))
        ],
        [
            InlineKeyboardButton(text='мелкий, тип А',
                                 callback_data=menu_callback.new(button_name='асфальт', type='мелкий, тип А')),
            InlineKeyboardButton(text='мелкий, тип Б',
                                 callback_data=menu_callback.new(button_name='асфальт', type='мелкий, тип Б'))

        ],
        [
            InlineKeyboardButton(text='ЩМА 10',
                                 callback_data=menu_callback.new(button_name='асфальт', type='ЩМА 10')),
            InlineKeyboardButton(text='ЩМА 15',
                                 callback_data=menu_callback.new(button_name='асфальт', type='ЩМА 15')),
            InlineKeyboardButton(text='ЩМА 20',
                                 callback_data=menu_callback.new(button_name='асфальт', type='ЩМА 20'))
        ],
        [
            InlineKeyboardButton(text='тротуарный',
                                 callback_data=menu_callback.new(button_name='асфальт', type='тротуарный'))
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=menu_callback.new(button_name='back_to_asfalt_main_menu', type='simple'))
        ]
    ]
)
