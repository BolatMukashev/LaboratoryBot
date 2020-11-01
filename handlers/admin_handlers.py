from main import bot, dp
from config import admins_id
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import db_stat, change_state


async def send_message_from_admin(dp):
    print('Бот запущен...')
    for admin in admins_id:
        try:
            await bot.send_message(chat_id=admin, text='Бот активен')
        except:
            pass


@dp.message_handler(Command('statistics'))
async def show_statistics(message: Message):
    change_state(message.from_user.id, None)
    users_number, users_names = db_stat()
    users_list = '\n'.join(users_names)
    if message.chat.id in admins_id:
        text = f'Количество пользователей: {users_number}\nСписок пользователей:\n{users_list}'
    else:
        text = 'Информация доступна только администратору'
    await message.answer(text=text)
