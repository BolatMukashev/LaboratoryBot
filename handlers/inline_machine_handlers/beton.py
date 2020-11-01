from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from functions.grunt import grunt_change_plotnost, grunt_change_v_ring
from functions.otsev import tech_usl_otsev
from functions.sheben import sheben_change_all
from keyboards.inline_keyboards.grunt import grunt_settings_buttons
from keyboards.inline_keyboards.inline_keyboards import menu_callback
from keyboards.inline_keyboards.sheben import sheben_settings_buttons
from loader import AllStates, check_state, change_state, is_float_simple, zernovoi_testing_go, check_ves_all, \
    create_grafic, tech_usl, zernovoi_table_str, dict_sheben, is_integer_simple, check_dno_state, \
    frakc_names, files_delete, base_commands
from main import dp