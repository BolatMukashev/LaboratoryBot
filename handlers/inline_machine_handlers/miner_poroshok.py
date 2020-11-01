from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards.inline_keyboards import menu_callback
from loader import AllStates, check_state, change_state, zernovoi_testing_go, check_ves_all, \
    tech_usl, zernovoi_table_str, check_dno_state, \
    frakc_names, files_delete, base_commands, create_grafic, create_pdf
from main import dp

# минеральный порошок


@dp.callback_query_handler(menu_callback.filter(button_name='мин_пор'), state=None)
async def min_por_test_start(call: CallbackQuery, callback_data: dict):
    change_state(call.from_user.id, 'мин_порошок')
    dno_state = check_dno_state(call.from_user.id)
    kol_vo = len(frakc_names('мин_порошок')) - 1 + dno_state
    await call.answer('Начато испытание зернового состава минерального порошка', cache_time=1)
    await call.message.answer(f'Начато испытание зернового состава минерального порошка. Введите <b>{kol_vo}</b> цифр.')
    await call.message.edit_reply_markup()
    await AllStates.Zernovoi_to_all.set()


@dp.message_handler(state=AllStates.Zernovoi_to_all)
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
            # формируем тех.условия
            tech_usloviya = tech_usl(user_state, list_pp, list_names[1:])
            # формируем график
            create_grafic(user_id, list_pp, user_state, orientation='portrait')
            # создаем pdf
            file_name = create_pdf(user_id=user_id,
                                   title=user_state,
                                   table=zernovoi_table,
                                   tech_usloviya=tech_usloviya,
                                   orientation='portrait')
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