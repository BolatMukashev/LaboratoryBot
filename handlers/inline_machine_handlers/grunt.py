from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from functions.grunt import grunt_change_plotnost, grunt_change_v_ring
from keyboards.inline_keyboards.grunt import grunt_settings_buttons
from loader import AllStates, check_state, change_state, is_float_simple
from main import dp


# грунт


@dp.callback_query_handler(text_contains='grunt_edit_max_pl', state=None)
async def grunt_max_pl_edit(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.answer('Напишите новое значение максимальной плотности:')
    change_state(call.from_user.id, 'edit_max_pl')
    await call.message.edit_reply_markup()
    await AllStates.Grunt.set()


@dp.callback_query_handler(text_contains='grunt_edit_v_ring', state=None)
async def grunt_max_pl_edit(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.answer('Напишите новое значение для объема кольца:')
    change_state(call.from_user.id, 'edit_v_ring')
    await call.message.edit_reply_markup()
    await AllStates.Grunt.set()


@dp.message_handler(state=AllStates.Grunt)
async def answer_grunt_parameters_edit(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    date = await state.get_data()
    answer1 = date.get('answer')
    user_text = is_float_simple(answer1)
    if user_text is False:
        await message.answer('Значене введено не правильно. Нужно ввести число.',
                             reply_markup=grunt_settings_buttons)
    else:
        if check_state(message.from_user.id) == 'edit_max_pl':
            grunt_change_plotnost(message.from_user.id, user_text)
            await message.answer(f'Значение максимальной плотности было изменено на <b>{user_text}</b>',
                                 reply_markup=grunt_settings_buttons)
        elif check_state(message.from_user.id) == 'edit_v_ring':
            grunt_change_v_ring(message.from_user.id, user_text)
            await message.answer(f'Значение для объема кольца было установлено на <b>{user_text}</b>',
                                 reply_markup=grunt_settings_buttons)
        else:
            await message.answer('Ошибка в статусе',
                                 reply_markup=grunt_settings_buttons)
    await state.finish()