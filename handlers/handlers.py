from functions.beton import is_date, beton_raschet_7and28, ispitanie_betona_prochnost
from functions.grunt import grunt_random_create, ispitanie_grunta
from keyboards.inline_keyboards.instructions import instructions_main_buttons
from keyboards.inline_keyboards.settings import settings_main_buttons
from main import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline_keyboards.inline_keyboards import entry_buttons
from aiogram.dispatcher.filters import Command
from loader import new_client, check_state, change_state
from config import main_admin


@dp.message_handler(Command('start'))
async def start_message(message: Message):
    await message.answer(f'Здравствуй, <b>{message.from_user.first_name}</b>!')
    text = [
        'Бот создан для того, чтобы облегчить жизнь лаборантов работающих в сфере строительства и дорожного '
        'строительства.',
        'Тут можно быстро посчитать зерновой состав, плотность грунта, определить марку бетона и т.д.'
    ]
    await message.answer('\n'.join(text))
    await message.answer('Что будем испытывать?', reply_markup=entry_buttons)
    new_client(message.from_user.id, message.from_user.full_name)


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    change_state(message.from_user.id, None)
    await message.answer('Что будем испытывать?', reply_markup=entry_buttons)


@dp.message_handler(Command('settings'))
async def show_setting(message: Message):
    change_state(message.from_user.id, None)
    await message.answer('Ниже представлены основные настройки', reply_markup=settings_main_buttons)


@dp.message_handler(Command('instructions'))
async def show_setting(message: Message):
    change_state(message.from_user.id, None)
    text = [
        'Инструкции пользователя.',
        'По задумке, это своего рода инциклопедия показывающая пользователям бота как собственно пользоваться ботом.',
        'Ниже указаны разделы, изучив которые Вы поймете в каком формате нужно отправлять сообщения боту, чтобы он их '
        'понимал.'
    ]
    await message.answer(text='\n'.join(text), reply_markup=instructions_main_buttons)


@dp.message_handler(Command('promotion'))
async def show_menu(message: Message):
    change_state(message.from_user.id, None)
    await message.answer('Функция в разработке...')


@dp.message_handler(Command('help'))
async def show_help(message: Message):
    change_state(message.from_user.id, None)
    text = [
        'Список команд:',
        '/menu - Главное меню',
        '/instructions - Инструкции пользователя',
        '/settings - Изменить настройки',
        '/help - Получить справку',
        '/statistics - Статистика бота',
        '/promotion - Заказать рекламу',
        'Если возникли вопросы, можете обратится к создателю этого бота:',
        f'<a href="https://t.me/RobertOpengamer">@Болат Мукашев</a>',
    ]
    help_text = '\n\n'.join(text)
    await message.answer(help_text)


@dp.message_handler(text='Показать текущие настройки')
async def settings_info(message: Message):
    await message.answer('')


@dp.message_handler(text='Изменить максимальную плотность')
async def settings_plotnost(message: Message):
    await message.answer('')


@dp.message_handler(text='Изменить объем кольца')
async def settings_ring(message: Message):
    await message.answer('')


@dp.message_handler(text='Мне повезёт!')
async def grunt_random(message: Message):
    text = grunt_random_create(message.from_user.id)
    await message.answer('\n'.join(text))


@dp.message_handler(text='Вернуться в главное меню')
async def cancel_and_go_to_menu(message: Message):
    change_state(message.from_user.id, None)
    await message.answer('Испытание грунта окончено', reply_markup=ReplyKeyboardRemove())
    await message.answer('Что будем испытывать?', reply_markup=entry_buttons)


@dp.message_handler(text='Отмена')
async def cancel_button(message: Message):
    await message.answer('Изменение не были внесены', reply_markup=ReplyKeyboardRemove())


# для обычных, не прописанных сообщений
@dp.message_handler()
async def echo(message: Message):
    if check_state(message.from_user.id) == 'grunt_plotnost':
        text = ispitanie_grunta(message.from_user.id, message.text)
        if text is False:
            text = 'Вы ввели данные не правильно! Посмотрите инструкцию /instruction и попробуйте еще раз'
            await message.answer(text=text)
        else:
            await message.answer(text='\n'.join(text))
    elif check_state(message.from_user.id) == '7and28sutok':
        create_date = is_date(message.text)
        if create_date is False:
            text = 'Вы ввели дату не правильно.\nПосмотрите инструкцию /instruction и попробуйте ввести дату еще раз.'
            await message.answer(text=text)
        else:
            text = beton_raschet_7and28(create_date)
            await message.answer(text='\n'.join(text))
    elif check_state(message.from_user.id) == 'beton_prochnost':
        text = ispitanie_betona_prochnost(message.from_user.id, message.text)
        if text is False:
            text = 'Вы ввели данные не правильно! Посмотрите инструкцию /instruction и попробуйте еще раз'
            await message.answer(text=text)
        else:
            await message.answer(text='\n'.join(text))
    else:
        text = f'Вы не выбрали испытание!\nНажми, чтобы сделать выбор: /menu'
        #  await bot.send_message(chat_id=message.from_user.id, text = text) - более сложная версия ответа
        await message.answer(text=text)