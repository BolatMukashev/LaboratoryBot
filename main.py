import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from loader import storage

# создаем поток
loop = asyncio.get_event_loop()

# создаем бота
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)

# создаем обработчик событий
dp = Dispatcher(bot, loop=loop, storage=storage)

# запускаем бота
if __name__ == '__main__':
    from handlers.admin_handlers import send_message_from_admin
    from handlers import dp

    # executor делает запросы getUpdates
    # стартует и отправляет сообщение админу
    executor.start_polling(dp, on_startup=send_message_from_admin)
