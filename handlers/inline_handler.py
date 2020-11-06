from functions.beton import *
from functions.grunt import grunt_check_parameters, grunt_change_plotnost, grunt_change_v_ring
from functions.settings import main_settings_check_parameters, settings_change_dno_true
from functions.sheben import sheben_check_all_parameters, sheben_settings_reset_all
from keyboards.inline_keyboards.asfalt import asfalt_buttons, asfalt_zernovoi_buttons
from keyboards.inline_keyboards.beton import *
from keyboards.inline_keyboards.grunt import grunt_buttons, grunt_settings_buttons, grunt_sbros_choise
from keyboards.inline_keyboards.min_por import min_por_buttons
from keyboards.inline_keyboards.otsev import otsev_buttons
from keyboards.inline_keyboards.pgs import pgs_buttons
from keyboards.inline_keyboards.settings import settings_main_buttons, dno_switch_button, time_zone_buttons
from keyboards.inline_keyboards.sheben import *
from keyboards.standart_keyboards import grunt_random_button
from main import dp
from aiogram.types import CallbackQuery
from config import *
from keyboards.inline_keyboards.inline_keyboards import menu_callback
from loader import *
from keyboards.inline_keyboards.inline_keyboards import entry_buttons


# text_contains - не точное совпадение по тексту, а если есть частично в тексте


# асфальт:


@dp.callback_query_handler(menu_callback.filter(button_name='asfalt'))
async def asfalt_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=asfalt_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='asfalt_zernovoi'))
async def asfalt_zernovoi(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=asfalt_zernovoi_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='back_to_asfalt_main_menu'))
async def back_to_asfalt_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=asfalt_buttons)


# щебень:


# главное меню щебня
@dp.callback_query_handler(menu_callback.filter(button_name='sheben'))
async def sheben_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=sheben_buttons)


# испытание зернового состава, сделать выбор
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_zernovoi'))
async def sheben_zernovoi(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=sheben_zernovoi_buttons)


# назад
@dp.callback_query_handler(menu_callback.filter(button_name='back_to_sheben_main_menu'))
async def back_to_sheben_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=sheben_buttons)


# перейдти к меню настроек
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_settings'))
async def sheben_settings_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=sheben_settings_buttons)


# показать все массы имеющихся проб
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_all_view'))
async def sheben_all_view(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = sheben_check_all_parameters(call.from_user.id)
    await call.message.edit_text(text='\n'.join(text))
    await call.message.answer('Что будем испытывать?', reply_markup=sheben_settings_buttons)


# меняем массу у одной пробы на выбор
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_set_change'))
async def sheben_settings_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(text='Выберите для какой фракции нужно изменить массу пробы:')
    await call.message.edit_reply_markup(reply_markup=sheben_all_change)


# меню сброса настроек
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_settings_reset'))
async def sheben_settings_reset_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(text='Уверены что хотите установить значения масс проб по умолчанию?')
    await call.message.edit_reply_markup(reply_markup=sheben_settings_reset_switch_buttons)


# подтверждение сброса настроек
@dp.callback_query_handler(menu_callback.filter(button_name='sheben_set_reset_yes'))
async def sheben_settings_reset(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    sheben_settings_reset_all(call.from_user.id)
    await call.message.edit_text(text='Для масс проб щебня были установлены значения по умолчанию.')
    await call.message.answer('Что будем испытывать?', reply_markup=sheben_settings_buttons)


# назад
@dp.callback_query_handler(menu_callback.filter(button_name='back_to_sheben_set_menu'))
async def back_to_sheben_set_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(text='Что будем испытывать?')
    await call.message.edit_reply_markup(reply_markup=sheben_settings_buttons)


#  пгс


@dp.callback_query_handler(menu_callback.filter(button_name='pgs'))
async def sheben_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=pgs_buttons)


# отсев


@dp.callback_query_handler(menu_callback.filter(button_name='otsev'))
async def sheben_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=otsev_buttons)


# мин порошок


@dp.callback_query_handler(menu_callback.filter(button_name='min_por'))
async def sheben_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=min_por_buttons)


# грунт:


@dp.callback_query_handler(menu_callback.filter(button_name='grunt'))
async def grunt_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=grunt_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='grunt_settings'))
async def grunt_settings_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=grunt_settings_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='back_to_grunt_main_menu'))
async def back_to_grunt_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=grunt_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='grunt_plotnost'))
async def grunt_plotnost_start(call: CallbackQuery):
    change_state(call.from_user.id, 'grunt_plotnost')
    await call.answer('Начато испытание грунта', cache_time=1)
    await call.message.edit_reply_markup()
    await call.message.answer('Начато испытание грунта', reply_markup=grunt_random_button)


# показать текущие настройки грунта
@dp.callback_query_handler(menu_callback.filter(button_name='grunt_settings_view'))
async def grunt_settings_view(call: CallbackQuery):
    await call.answer(cache_time=1)
    plotnost, v_ring = grunt_check_parameters(call.from_user.id)
    await call.message.edit_reply_markup()
    text = [
        'Сейчас установлены следующие параметры',
        f'Значение максимальной плотности: <b>{plotnost}</b>',
        f'Объем кольца: <b>{v_ring}</b>'
    ]
    await call.message.answer(text='\n'.join(text), reply_markup=grunt_settings_buttons)


# сбросить настройки грунта
@dp.callback_query_handler(menu_callback.filter(button_name='grunt_settings_sbros'))
async def grunt_sbros(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Значения максимальной плотности и объема кольца будут сброшены. Вы уверены?'
    await call.message.answer(text=text, reply_markup=grunt_sbros_choise)


# подвердить сброс настроек грунта
@dp.callback_query_handler(menu_callback.filter(button_name='grunt_sbros_yes'))
async def grunt_sbros_yes(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    grunt_change_plotnost(call.from_user.id, standart_max_pl)
    grunt_change_v_ring(call.from_user.id, standart_v_ring)
    text = [
        'Установлены следующие параметры',
        f'Значение максимальной плотности: <b>{standart_max_pl}</b>',
        f'Объем кольца: <b>{standart_v_ring}</b>'
    ]
    await call.message.edit_text(text='\n'.join(text), reply_markup=grunt_settings_buttons)


# вернуться к настройкам грунта
@dp.callback_query_handler(menu_callback.filter(button_name='grunt_back_to_settings_menu'))
async def grunt_sbros(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Сброс отменен.'
    await call.message.edit_text(text=text, reply_markup=grunt_settings_buttons)


# бетон:


# показать меню бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton'))
async def beton_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=beton_buttons)


# испытание на прочность
@dp.callback_query_handler(menu_callback.filter(button_name='beton_prochnost'))
async def beton_test_start(call: CallbackQuery):
    change_state(call.from_user.id, 'beton_prochnost')
    await call.answer('Начато испытание образцов бетона', cache_time=1)
    await call.message.edit_reply_markup()
    await call.message.answer('Начато испытание образцов бетона на прочность')


# испытание на определение даты 7 и 28 суток
@dp.callback_query_handler(menu_callback.filter(button_name='7and28sutok'))
async def beton_7and28(call: CallbackQuery):
    change_state(call.from_user.id, '7and28sutok')
    await call.answer('Подсчитываем даты для образцов бетона', cache_time=1)
    await call.message.edit_reply_markup()
    text = [
        'Начат расчет дат для образцов бетона (7 и 28 суток).',
        'Напишите дату, когда кубик был сформован, в формате \"<b>дата.месяц.год</b>\"'
    ]
    await call.message.answer(text='\n'.join(text))


@dp.callback_query_handler(menu_callback.filter(button_name='beton_settings'))
async def beton_main(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=beton_settings_buttons)


# показать текущие настройки бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_settings_view'))
async def beton_settings_view(call: CallbackQuery):
    await call.answer(cache_time=1)
    beton_size, beton_metric, beton_type, beton_w = beton_parameters_check(call.from_user.id)
    b_type = ""
    if beton_type == 'tyazholii':
        b_type = "Тяжелый бетон на граните"
    elif beton_type == 'yacheistii':
        b_type = 'Ячеистый'
    await call.message.edit_reply_markup()
    text = [
        'Сейчас установлены следующие параметры',
        f'Размер кубиков: <b>{beton_size}</b>x<b>{beton_size}</b>мм',
        f'Система счисления: <b>{beton_metric}</b>',
        f'Тип бетона: <b>{b_type}</b>',
        f'Влажность (для ячеистых бетонов): <b>{beton_w}%</b>'
    ]
    await call.message.answer(text='\n'.join(text), reply_markup=beton_settings_buttons)


# сбросить настройки бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_settings_sbros'))
async def beton_sbros(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Значения размера образцов бетона и системы счисления будут сброшены. Вы уверены?'
    await call.message.answer(text=text, reply_markup=beton_sbros_choise)


# подвердить сброс настроек бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_sbros_yes'))
async def beton_sbros_yes(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    beton_change_size(call.from_user.id, standart_beton_size)
    beton_change_metric(call.from_user.id, standart_beton_metric)
    beton_change_type(call.from_user.id, standart_beton_type)
    beton_change_w(call.from_user.id, standart_beton_w)
    text = [
        'Были установлены следующие параметры',
        f'Размер кубиков: <b>{standart_beton_size}</b>x<b>{standart_beton_size}</b>мм',
        f'Система счисления: <b>{standart_beton_metric}</b>',
        f'Тип бетона: <b>Тяжёлый бетон на граните</b>',
        f'Влажность для ячеистого бетона: <b>{standart_beton_w}%</b>'
    ]
    await call.message.edit_text(text='\n'.join(text), reply_markup=beton_settings_buttons)


# вернуться к настройкам бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_to_set_menu'))
async def beton_sbros_no(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = callback_data.get('type')
    await call.message.edit_text(text=text, reply_markup=beton_settings_buttons)


# меняем размер образцов бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_size'))
async def beton_change_size_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Выберите какой размер образцов бетона будет установлен для испытаний'
    await call.message.answer(text=text, reply_markup=beton_size_switch)


# выбираем размер для образца бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_size_true'))
async def beton_change_size_go(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    beton_size = callback_data.get('type')
    beton_change_size(call.from_user.id, beton_size)
    text = f'Размер образцов бетона для испытаний был изменен на <b>{beton_size}</b>x<b>{beton_size}</b>мм.'
    await call.message.edit_text(text=text, reply_markup=beton_settings_buttons)


# меняем систему счисления бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_metric'))
async def beton_change_metric_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Выберите какая система счисления будет установлена для испытаний образцов бетона'
    await call.message.answer(text=text, reply_markup=beton_metrics_switch)


# выбираем систему счисления бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_metric_true'))
async def beton_change_metric_go(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    beton_metric = callback_data.get('type')
    beton_change_metric(call.from_user.id, beton_metric)
    text = f'Система счистления для испытания образцов бетона была изменена на <b>{beton_metric}</b>.'
    await call.message.edit_text(text=text, reply_markup=beton_settings_buttons)


# меняем тип образцов бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_type'))
async def beton_change_type_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Выберите какой тип бетона будет установлен для испытаний'
    await call.message.answer(text=text, reply_markup=beton_types_buttons)


# выбираем тип для образца бетона
@dp.callback_query_handler(menu_callback.filter(button_name='beton_types'))
async def beton_change_type_go(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    beton_type = callback_data.get('type')
    beton_change_type(call.from_user.id, beton_type)
    b_type = ""
    if beton_type == 'tyazholii':
        b_type = "Тяжелый бетон на граните"
    elif beton_type == 'yacheistii':
        b_type = "Ячеистый"
    text = f'Тип образцов бетона для испытаний был изменен на <b>{b_type}</b>.'
    await call.message.edit_text(text=text, reply_markup=beton_settings_buttons)


# меняем влажность для ячеистых бетонов
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_w'))
async def beton_change_w_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    text = 'Выберите какая влажность у образцов ячеистого бетона будет установлена в испытаниях:'
    await call.message.answer(text=text, reply_markup=beton_yacheistii_change_w_keyboards)


# выбираем влажность для ячеистых бетонов
@dp.callback_query_handler(menu_callback.filter(button_name='beton_change_w_true'))
async def beton_change_w_go(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    beton_w = callback_data.get('type')
    beton_change_w(call.from_user.id, beton_w)
    text = f'Влажность для образцов ячеистого бетона была установлена на <b>{beton_w}%</b>'
    await call.message.edit_text(text=text, reply_markup=beton_settings_buttons)


# просто кнопка назад
@dp.callback_query_handler(menu_callback.filter(button_name='back_to_beton_main_menu'))
async def back_to_beton_main_menu(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=beton_buttons)


# общие команды:


# кнопка отмена
@dp.callback_query_handler(menu_callback.filter(button_name='cancel'))
async def cancel_all(call: CallbackQuery):
    await call.answer('Вы всё отменили', show_alert=True)  # показать уведомление в окошке
    await call.message.edit_reply_markup()  # закрыть инлайн клавиатуру


# кнопка назад первого уровня
@dp.callback_query_handler(menu_callback.filter(button_name='back_to_entry_button'))
async def nazad_button(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup(reply_markup=entry_buttons)


# настройки:


# дно:

# false to не учитывается
@dp.callback_query_handler(menu_callback.filter(button_name='main_setting_parameters_view'))
async def dno_setting_view(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    dno = main_settings_check_parameters(call.from_user.id)
    time_zone = check_time_zone(call.from_user.id)
    if dno is True:
        dno = 'учитывается'
    else:
        dno = 'не учитывается'
    await call.message.edit_text(
        f'Установлены следующие параметры:\nДно: <b>{dno}</b>\nЧасовой пояс: <b>{time_zone}</b>')
    await call.message.answer('Ниже представлены основные настройки', reply_markup=settings_main_buttons)


# задать вопрос да или нет
@dp.callback_query_handler(menu_callback.filter(button_name='dno_switch'))
async def dno_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    await call.message.edit_text('Учитывать дно сит в расчетах зернового состава?', reply_markup=dno_switch_button)


# если ответ да
@dp.callback_query_handler(menu_callback.filter(button_name='dno_true'))
async def dno_true(call: CallbackQuery):
    text = 'Значение дна в расчетах зернового состава щебня, пгс, отсева и минерального порошка теперь можно ' \
           'вводить вручную.'
    settings_change_dno_true(call.from_user.id, 1)
    await call.answer(text=text, show_alert=True, cache_time=1)
    await call.message.edit_text(text=text)
    await call.message.answer('Ниже представлены основные настройки', reply_markup=settings_main_buttons)


# если ответ нет
@dp.callback_query_handler(menu_callback.filter(button_name='dno_false'))
async def dno_false(call: CallbackQuery):
    text = 'Дно сита в расчетах зернового состава щебня, пгс, отсева и минерального порошка теперь расчитывается ' \
           'автоматически.'
    settings_change_dno_true(call.from_user.id, 0)
    await call.answer(text=text, show_alert=True, cache_time=1)
    await call.message.edit_text(text=text)
    await call.message.answer('Ниже представлены основные настройки', reply_markup=settings_main_buttons)


# выбрать часовой пояс
@dp.callback_query_handler(menu_callback.filter(button_name='time_zone'))
async def dno_setting(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    await call.message.edit_text('Выберите Вашу часовую зону:', reply_markup=time_zone_buttons)


# когда выбор часового пояса сделан
@dp.callback_query_handler(menu_callback.filter(button_name='choose_time_zone'))
async def dno_true(call: CallbackQuery, callback_data: dict):
    user_time_zone = callback_data.get('type')
    text = f'Значение часового пояса установлено на {user_time_zone}'
    change_time_zone(call.from_user.id, user_time_zone)
    await call.answer(text=text, show_alert=True, cache_time=1)
    await call.message.edit_text(text=text)
    await call.message.answer('Ниже представлены основные настройки', reply_markup=settings_main_buttons)


@dp.callback_query_handler(menu_callback.filter(button_name='back_to_settings_buttons'))
async def setting_main_back(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text('Ниже представлены основные настройки')
    await call.message.edit_reply_markup(reply_markup=settings_main_buttons)
