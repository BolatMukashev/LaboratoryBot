from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from functions.sheben import sheben_change_all
from keyboards.inline_keyboards.inline_keyboards import menu_callback
from keyboards.inline_keyboards.sheben import sheben_settings_buttons
from loader import *
from main import dp


# меняем массу пробы
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_all_ch'), state=None)
async def sheben_all_edit(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    fraction_type = callback_data.get('type')
    change_state(call.from_user.id, fraction_type)
    await call.message.edit_text('Напишите новое значение для массы пробы:')
    await AllStates.Sheben_change_all.set()


@dp.message_handler(state=AllStates.Sheben_change_all)
async def answer_sheben_all_edit(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    date = await state.get_data()
    answer1 = date.get('answer')
    user_text = is_integer_simple(answer1)
    if user_text is False:
        await message.answer('Значене введено не правильно. Нужно ввести целое число.',
                             reply_markup=sheben_settings_buttons)
    else:
        sheben_fraction = check_state(message.from_user.id)
        sheben_change_all(message.from_user.id, sheben_fraction, user_text)
        sheben_fraction = dict_sheben[sheben_fraction]
        sheben_change_all(message.from_user.id, sheben_fraction, user_text)
        await message.answer(f'Значение массы пробы у щебня {sheben_fraction} было изменено на '
                             f'<b>{user_text}</b> г.')
        await message.answer('Что будем испытывать?', reply_markup=sheben_settings_buttons)
    await state.finish()


# Испытание зернового состава


@dp.callback_query_handler(menu_callback.filter(button_name='щебень'), state=None)
async def min_por_test_start(call: CallbackQuery, callback_data: dict):
    asfalt_type = callback_data.get('button_name') + ':' + callback_data.get('type')
    change_state(call.from_user.id, asfalt_type)
    dno_state = check_dno_state(call.from_user.id)
    kol_vo = len(frakc_names(asfalt_type)) - 1 + dno_state
    await call.answer('Начато испытание зернового состава щебня', cache_time=1)
    await call.message.answer(f'Начато испытание зернового состава щебня. Введите <b>{kol_vo}</b> '
                              f'чисел.')
    await call.message.edit_reply_markup()
    await AllStates.Sheben.set()


@dp.message_handler(state=AllStates.Sheben)
async def answer_min_por(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    date = await state.get_data()
    answer1 = date.get('answer')
    if answer1 in base_commands:
        await state.finish()
        await message.answer('Испытание было прервано')
    else:
        user_id = message.from_user.id
        user_state = check_state(user_id)
        await message.answer('ожидайте...')
        ves_all = check_ves_all(user_id, user_state + '_all')
        text, list_names, list_ves, list_cho, list_po, list_pp, dno_state = zernovoi_testing_go(title=user_state,
                                                                                                user_text=answer1,
                                                                                                user_id=user_id,
                                                                                                ves_all=ves_all)
        if text == '<b>Подсчет окончен</b>. Вот ваш результат':
            # формируем таблицу
            zernovoi_table = zernovoi_table_str(list_names, list_ves, list_cho, list_po, list_pp, ves_all)
            # формируем тех.условия, где:
            tech_usloviya = standart_technical_specific(user_state, list_pp, list_names[1:])
            # формируем график
            create_grafic(user_id, list_pp, user_state, orientation='portrait')
            # создаем pdf
            file_name = create_pdf(user_id=user_id,
                                   title=user_state,
                                   table=zernovoi_table,
                                   technical_specific=tech_usloviya,
                                   page_orientation='portrait')
            try:
                with open(r'./users_files/' + f'{user_id}/' + file_name, 'rb') as document:
                    await message.answer(text)
                    await message.answer_document(document)
                files_delete(user_id)
                change_state(user_id, None)
            except:
                pass
            await state.finish()
        else:
            await message.answer(text)