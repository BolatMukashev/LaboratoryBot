import os
import pymongo as pymongo
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import MongoDB_key, server_time_zone, bot_name, bot_url
from prettytable import PrettyTable
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from math import ceil

pt = PrettyTable()

storage = MemoryStorage()


class AllStates(StatesGroup):
    Asfalt: State = State()
    Sheben: State = State()
    Sheben_change_all: State = State()
    PGS: State = State()
    Grunt: State = State()
    Otsev: State = State()
    Min_poroshok: State = State()
    Zernovoi_to_all: State = State()
    Test_State: State = State()


client = pymongo.MongoClient(MongoDB_key)
db = client.test
users_data_base = db.laboratory_bot

base_commands = ['/menu', '/instructions', '/settings', '/help', '/statistics']


def id_seach(simple_user_id):
    id_collection = []
    for item in users_data_base.find():
        id_collection.append(item["_id"])
    if simple_user_id in id_collection:
        return True
    else:
        return False


def new_client(user_id, user_name):
    if id_seach(user_id):
        pass
    else:
        users_data_base.insert_one({
            "_id": user_id,
            "user_name": user_name,
            "state": None,
            "dno": 0,
            "time_zone": +3,
            "beton_metric": 'кН',  # кН Мпа кгс
            "beton_size": 100,  # 70, 100, 150
            "beton_type": 'tyazholii',
            "beton_w": 10,
            "max_pl": 1.72,
            "v_ring": 98.4,
            "ПГС_all": 1000,
            "отсев_зерновой:standart_all": 2500,
            "отсев_зерновой:mod_all": 2500,
            "мин_порошок_all": 50,
            "щебень:5-20_all": 5000,
            "щебень:5-10_all": 5000,
            "щебень:10-20_all": 5000,
            "щебень:20-40_all": 10000,
            "щебень:40-70_all": 10000,
        })
        try:
            os.mkdir(f'./users_files/{user_id}')
        except FileExistsError:
            pass


def files_delete(user_id):
    directory = (os.getcwd()).replace('\\', '/') + '/users_files/' + f'{user_id}'
    for file in os.scandir(directory):
        os.unlink(file.path)


def db_stat():
    all_date_base = users_data_base.find()
    id_collection = []
    user_name_collections = []
    for item in all_date_base:
        id_collection.append(item["_id"])
        user_name_collections.append(item['user_name'])
    return len(id_collection), user_name_collections


# как оперативная память, временно хранит состояния вместо того чтобы каждый раз обращаться в MongoDB
# test_state = {'user_id': {'state': None}}


test_state = {}


# функция добавляет/меняет статус в оперативной памяти и в постоянной памяти (MongoDB)
def change_state(user_id, new_state):
    if user_id in test_state:
        test_state[user_id]['state'] = new_state
    else:
        test_state.update({user_id: {'state': new_state}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'state': new_state}})


# проверяет временную память. Если есть значение - выдает значение,
# если нет - обращается к постоянной памяти и вписывает во временную
def check_state(user_id):
    if user_id in test_state:
        state = test_state[user_id]['state']
    else:
        state = users_data_base.find({'_id': user_id})[0]['state']
        test_state.update({user_id: {'state': state}})
    return state


# grunt_parameters = {'user_id': {'max_pl': 0, 'v_ring': 0}}
grunt_parameters = {}

# beton_parameters = {'user_id': {'beton_size': 0, 'beton_metric': 0, 'beton_type': 'tyazholii', 'beton_w': 1}}
# beton_size = 70, 100, 150, 200, 250, 300
# beton_metric = кН, МПа, кгс
# beton_type = tyazholii, yacheistii
# beton_w = 0, 5, 10, 15, 20, 25

beton_parameters = {}

beton_koeficients = {70: 0.85, 100: 0.95, 150: 1.0, 200: 1.05, 250: 1.08, 300: 1.1}
beton_yacheistii_w = {0: 0.8, 5: 0.9, 10: 1.0, 15: 1.05, 20: 1.1, 25: 1.15}


def is_float_simple(text):
    text = text.replace(',', '.').strip()
    test_text = text.replace('.', '', 1).isdigit()
    if test_text is False:
        return False
    else:
        return float(text)


def is_float(spisok: list):
    edited_spisok = list(map(lambda x: x.replace(',', '.').strip(), spisok))
    spisok_test = list(map(lambda x: x.replace('.', '', 1).isdigit(), edited_spisok))
    if False in spisok_test:
        return False
    else:
        edited_spisok = list(map(lambda x: float(x), edited_spisok))
        return edited_spisok


def is_integer_simple(text):
    text_test = text.isdigit()
    if text_test is False:
        return False
    else:
        return int(text)


dict_sheben = {
    'щебень_5-10': 'фр.5-10мм',
    'щебень_5-20': 'фр.5-20мм',
    'щебень_10-20': 'фр.10-20мм',
    'щебень_20-40': 'фр.20-40мм',
    'щебень_40-70': 'фр.40-70мм'
}

# изменить значение у дна range(0, 1) - поменять на допуски

dict_proverka = {'асфальт':
                     {'крупный, тип А':
                          {'фр.40': range(90, 101), 'фр.20': range(75, 101), 'фр.15': range(64, 101),
                           'фр.10': range(52, 89), 'фр.5': range(40, 61), 'фр.2,5': range(28, 61),
                           'фр.1,25': range(16, 61), 'фр.0,63': range(10, 61), 'фр.0,315': range(8, 38),
                           'фр.0,16': range(5, 21), 'фр.0,071': range(2, 9), 'фр.<0,071': range(0, 1)},
                      'крупный, тип Б':
                          {'фр.40': range(90, 101), 'фр.20': range(75, 101), 'фр.15': range(64, 101),
                           'фр.10': range(52, 89), 'фр.5': range(40, 61), 'фр.2,5': range(28, 61),
                           'фр.1,25': range(16, 61), 'фр.0,63': range(10, 61), 'фр.0,315': range(8, 38),
                           'фр.0,16': range(5, 21), 'фр.0,071': range(2, 9), 'фр.<0,071': range(0, 1)},
                      'мелкий, тип А':
                          {'фр.40': range(100, 101), 'фр.20': range(90, 101), 'фр.15': range(75, 101),
                           'фр.10': range(62, 89), 'фр.5': range(40, 50), 'фр.2,5': range(28, 39),
                           'фр.1,25': range(20, 29), 'фр.0,63': range(14, 21), 'фр.0,315': range(10, 17),
                           'фр.0,16': range(6, 13), 'фр.0,071': range(4, 11), 'фр.<0,071': range(0, 1)},
                      'мелкий, тип Б':
                          {'фр.40': range(100, 101), 'фр.20': range(90, 101), 'фр.15': range(80, 101),
                           'фр.10': range(70, 101), 'фр.5': range(50, 61), 'фр.2,5': range(38, 49),
                           'фр.1,25': range(28, 38), 'фр.0,63': range(20, 29), 'фр.0,315': range(14, 23),
                           'фр.0,16': range(10, 17), 'фр.0,071': range(6, 13), 'фр.<0,071': range(0, 1)},
                      'ЩМА 10':
                          {'фр.40': range(100, 101), 'фр.20': range(90, 101), 'фр.15': range(80, 101),
                           'фр.10': range(70, 101), 'фр.5': range(50, 61), 'фр.2,5': range(38, 49),
                           'фр.1,25': range(28, 38), 'фр.0,63': range(20, 29), 'фр.0,315': range(14, 23),
                           'фр.0,16': range(10, 17), 'фр.0,071': range(6, 13), 'фр.<0,071': range(0, 1)},
                      'ЩМА 15':
                          {'фр.40': range(100, 101), 'фр.20': range(100, 101), 'фр.15': range(90, 101),
                           'фр.10': range(40, 61), 'фр.5': range(25, 36), 'фр.2,5': range(18, 29),
                           'фр.1,25': range(15, 26), 'фр.0,63': range(12, 23), 'фр.0,315': range(10, 21),
                           'фр.0,16': range(9, 17), 'фр.0,071': range(9, 15), 'фр.<0,071': range(0, 1)},
                      'ЩМА 20':
                          {'фр.40': range(100, 101), 'фр.20': range(90, 101), 'фр.15': range(50, 71),
                           'фр.10': range(25, 43), 'фр.5': range(20, 31), 'фр.2,5': range(15, 26),
                           'фр.1,25': range(13, 25), 'фр.0,63': range(11, 22), 'фр.0,315': range(9, 20),
                           'фр.0,16': range(8, 16), 'фр.0,071': range(8, 14), 'фр.<0,071': range(0, 1)},
                      'тротуарный':
                          {'фр.40': range(100, 101), 'фр.20': range(100, 101), 'фр.15': range(70, 101),
                           'фр.10': range(56, 101), 'фр.5': range(30, 51), 'фр.2,5': range(24, 51),
                           'фр.1,25': range(18, 51), 'фр.0,63': range(13, 51), 'фр.0,315': range(12, 51),
                           'фр.0,16': range(11, 29), 'фр.0,071': range(10, 17), 'фр.<0,071': range(0, 1)},
                      },

                 'мин_порошок': {'фр.1,25': range(100, 101), 'фр.0,63': range(90, 101), 'фр.0,315': range(90, 101),
                                 'фр.0,16': range(80, 101), 'фр.0,071': range(80, 101), 'фр.<0,071': range(0, 6)},

                 'отсев_зерновой':
                     {'standart': ['фр.8', 'фр.4', 'фр.2', 'фр.1', 'фр.0,5',
                                   'фр.0,25', 'фр.0,125', 'фр.<0.125'],
                      'mod': ['фр.10', 'фр.5', 'фр.2,5', 'фр.1,25', 'фр.0,63',
                              'фр.0,315', 'фр.0,16', 'фр.0,05', 'фр.<0.05']
                      },

                 'щебень':
                     {'5-10':
                          {'фр.12,5': [0, 0.5], 'фр.10': [0, 10], 'фр.7,5': [30, 60], 'фр.5': [90, 100],
                           'фр.2,5': [95, 100], 'фр.1,25': [95, 100], 'фр.<1,25': [99, 100]},
                      '5-20':
                          {'фр.25': [0, 0.5], 'фр.20': [0, 10], 'фр.12,5': [30, 60], 'фр.5': [90, 100],
                           'фр.2,5': [95, 100], 'фр.1,25': [95, 100], 'фр.<1,25': [99, 100]},
                      '10-20':
                          {'фр.25': [0, 0.5], 'фр.20': [0, 10], 'фр.15': [30, 60], 'фр.10': [90, 100],
                           'фр.<10': [99, 100]},
                      '10-20(mod)':
                          {'фр.25': [0, 0.5], 'фр.20': [0, 10], 'фр.15': [30, 60], 'фр.10': [90, 100],
                           'фр.5': [90, 100], 'фр.<5': [99, 100]},
                      '20-40':
                          {'фр.50': [0, 0.5], 'фр.40': [0, 10], 'фр.30': [30, 60], 'фр.20': [90, 100],
                           'фр.<20': [99, 100]},
                      '40-70':
                          {'фр.87,5': [0, 0.5], 'фр.70': [0, 10], 'фр.55': [30, 60], 'фр.40': [90, 100],
                           'фр.<40': [99, 100]},
                      '40-70(mod)':
                          {'фр.80': [0, 0.5], 'фр.70': [0, 10], 'фр.60': [30, 60], 'фр.50': [30, 60],
                           'фр.40': [90, 100], 'фр.<40': [99, 100]}
                      }
                 }

zaglavie = {'мин_порошок': 'минерального порошка',
            'отсев_зерновой:standart': 'песка из отсева дробления, фр.0-5мм',
            'отсев_зерновой:mod': 'песка из отсева дробления, фр.0-5мм',
            'асфальт:крупный, тип А': 'крупнозернистой асфальтобетонной смеси, тип А',
            'асфальт:крупный, тип Б': 'крупнозернистой асфальтобетонной смеси, тип Б',
            'асфальт:мелкий, тип А': 'мелкозернистой асфальтобетонной смеси, тип А',
            'асфальт:мелкий, тип Б': 'мелкозернистой асфальтобетонной смеси, тип Б',
            'асфальт:ЩМА 10': 'щебеночно-мастичной асфальтобетонной смеси(ЩМА 10)',
            'асфальт:ЩМА 15': 'щебеночно-мастичной асфальтобетонной смеси(ЩМА 15)',
            'асфальт:ЩМА 20': 'щебеночно-мастичной асфальтобетонной смеси(ЩМА 20)',
            'асфальт:тротуарный': 'тротуарной асфальтобетонной смеси',
            'щебень:5-20': 'щебня из плотных горных пород, фр.5-20мм',
            'щебень:5-10': 'щебня из плотных горных пород, фр.5-10мм',
            'щебень:10-20': 'щебня из плотных горных пород, фр.10-20мм',
            'щебень:10-20(mod)': 'щебня из плотных горных пород, фр.10-20мм',
            'щебень:20-40': 'щебня из плотных горных пород, фр.20-40мм',
            'щебень:40-70': 'щебня из плотных горных пород, фр.40-70мм',
            'щебень:40-70(mod)': 'щебня из плотных горных пород, фр.40-70мм'
            }


def check_dno_state(user_id):
    dno_state = users_data_base.find({'_id': user_id})[0]['dno']
    return dno_state


def check_ves_all(user_id, type_name):
    type_name = type_name.replace('(mod)', '')
    ves_all = users_data_base.find({'_id': user_id})[0][type_name]
    return ves_all


def check_time_zone(user_id):
    time_zone = users_data_base.find({'_id': user_id})[0]['time_zone']
    return time_zone


def change_time_zone(user_id: int, time_zone: int):
    users_data_base.update_one({'_id': user_id}, {'$set': {'time_zone': time_zone}})


def modul_krupnosti(list_pp: list):
    list_pp_srez = list_pp[2:7]
    mk = sum(list_pp_srez) / 100
    return mk


# доделать! сплит по переносу строки
def text_in_list(user_text):
    text = user_text.split(' ')
    return text


# orientation = 'landscape' or 'portrait'
def create_grafic(user_id: int, list_pp: list, title: str, orientation: str = 'landscape'):
    proverka = title.split(':')
    maximums = []
    minimums = []

    if len(proverka) == 1:
        list_names = list(dict_proverka[title].keys())

        # максимумы
        for x in dict_proverka[title]:
            n = max(dict_proverka[title][x])
            maximums.append(n)

        # минимумы
        for x in dict_proverka[title]:
            n = min(dict_proverka[title][x])
            minimums.append(n)

    elif len(proverka) == 2:
        list_names = list(dict_proverka[proverka[0]][proverka[1]].keys())

        # максимумы
        for x in dict_proverka[proverka[0]][proverka[1]]:
            n = max(dict_proverka[proverka[0]][proverka[1]][x])
            maximums.append(n)

        # минимумы
        for x in dict_proverka[proverka[0]][proverka[1]]:
            n = min(dict_proverka[proverka[0]][proverka[1]][x])
            minimums.append(n)

    list_names = list(map(lambda name: name.replace('фр.', ''), list_names))

    if orientation == 'landscape':
        col_size = 8.2
        row_size = 3.8
    else:
        col_size = 8
        row_size = 4

    fig, ax = plt.subplots(figsize=(col_size, row_size), dpi=300)

    ax.set(xlabel='Фракции', ylabel='Значения')

    ax.plot(list_names, maximums, color='#f54768', label='max', linestyle='--')
    ax.plot(list_names, minimums, color="#f54768", label='min', linestyle='--')
    ax.plot(list_names, list_pp, 'o-b', alpha=1, label="полный проход",
            color='#41436a', linewidth=2,  # цвет и размер линии
            markerfacecolor='#ffffff', markersize=7,  # цвет и размер кружка
            markeredgecolor='#41436a', markeredgewidth=1.5  # цвет и размер обводки кружка
            )

    #  Добавляем линии основной сетки:
    ax.grid(which='major', color='k')

    #  Включаем видимость вспомогательных делений:
    ax.minorticks_on()

    #  Теперь можем отдельно задавать внешний вид вспомогательной сетки:
    ax.grid(which='minor',
            color='gray',
            linestyle=':')

    # подпись для линий
    ax.legend()

    # plt.show()

    # размер шрифта для боковых title в графике
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
        item.set_fontsize(10)

    # размер шрифта для фракций и процентов в графике
    for item in (ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(9)

    # ax.set_facecolor('#2a3950') - цвет фона

    # сохраняем график
    fig.savefig(f'./users_files/{user_id}/grafic.png', bbox_inches='tight')
    plt.close(fig)


def frakc_names(title: str):
    proverka = title.split(':')
    if len(proverka) == 1:
        list_names = list(dict_proverka[title].keys())
    elif len(proverka) == 2:
        try:
            list_names = list(dict_proverka[proverka[0]][proverka[1]].keys())
        except:
            list_names = list(dict_proverka[proverka[0]][proverka[1]])
    return list_names


def check_title(title: str):
    proverka = title.split(':')
    if len(proverka) == 1:
        directory = dict_proverka[title]
    elif len(proverka) == 2:
        directory = dict_proverka[proverka[0]][proverka[1]]
    return directory


# проверка тех. условий
def tech_usl(title: str, list_pp: list, list_names: list):
    znacheniya = []
    keys_dir = check_title(title)
    for x in list_names:
        x = keys_dir[x]
        znacheniya.append(x)
    list_tech_usl = []
    for pos, el in enumerate(list_pp):
        if el > max(znacheniya[pos]):
            razriv = el - max(znacheniya[pos])
            razriv = '{0:.2f}'.format(razriv)
            text = f'{list_names[pos]}: больше на {razriv}'
        elif min(znacheniya[pos]) <= el <= max(znacheniya[pos]):
            text = f'{list_names[pos]}: +'
        else:
            razriv = min(znacheniya[pos]) - el
            razriv = '{0:.2f}'.format(razriv)
            text = f'{list_names[pos]}: меньше на {razriv}'
        list_tech_usl.append(text)
    return list_tech_usl


def update_tech_usl_old(tu_list: list):
    list_f = [[], [], [], [], [], []]
    if len(tu_list) > 6:
        for pos, el in enumerate(tu_list):
            if pos <= 5:
                list_f[pos].append(el)
            else:
                list_f[pos - 6].append(el)
    else:
        list_f = list(map(lambda x: [x], tu_list))
    return list_f


def update_tech_usl(tu_list: list):
    fin_list = []
    list_f = tu_list.copy()
    list1_len = ceil(len(list_f) / 2)
    for _ in range(list1_len):
        fin_list.append([list_f.pop(0)])
    for _ in range(len(list_f)):
        fin_list[_].append(list_f.pop(0))
    return fin_list


def error_log(func):
    def some():
        print(f'Начало {func.__name__}')
        func()
        print(f'Конец {func.__name__}')

    return some()


def create_pdf(user_id: int,
               title: str,
               table: list,
               tech_usloviya: list,
               orientation: str = 'portrait',
               modified_tech_usl: bool = False):
    directory = (os.getcwd()).replace('\\', '/') + '/users_files/' + f'{user_id}/'

    if orientation == 'portrait':
        orientation = A4
        col_size = 560
        row_size = 310
    else:
        orientation = landscape(A4)
        col_size = 800
        row_size = 400

    # дата и время
    time_on_server = datetime.now()
    user_time_zone = check_time_zone(user_id)
    time_on_user = time_on_server + timedelta(hours=int(user_time_zone) - int(server_time_zone))

    # пути к шрифтам и регистрация шрифтов
    fonts_directory = (os.getcwd()).replace('\\', '/') + '/fonts/'
    reportlab.rl_config.TTFSearchPath = fonts_directory
    pdfmetrics.registerFont(TTFont('NotoSansRegular', fonts_directory + 'NotoSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('NotoSansBold', fonts_directory + 'NotoSans-Bold.ttf'))

    # применяем стили
    styles = getSampleStyleSheet()  # дефолтовые стили
    styles.add(ParagraphStyle(fontName='NotoSansBold', name='FontBold', leading=30, fontSize=24, alignment=TA_CENTER))
    styles.add(
        ParagraphStyle(fontName='NotoSansBold', name='FontBoldSimple', leading=24, fontSize=16, alignment=TA_CENTER,
                       spaceBefore=8))
    styles.add(ParagraphStyle(fontName='NotoSansRegular', name='FontRegular', leading=20, fontSize=12))
    styles.add(ParagraphStyle(fontName='NotoSansRegular', name='FontRegularRIGHT', leading=20, fontSize=12,
                              alignment=TA_RIGHT))
    styles.add(ParagraphStyle(fontName='NotoSansRegular', name='FontRegularRIGHTsimple', leading=20, fontSize=10,
                              alignment=TA_RIGHT, spaceBefore=15))

    # создаем объект документа с размером страницы A4
    title2: str = title.replace(':', ', ')
    file_name = f'{title2}.pdf'
    doc = SimpleDocTemplate(directory + file_name,
                            pagesize=orientation,
                            title='Испытание зернового состава',
                            author='LabyLab Inc',
                            leftMargin=20,
                            rightMargin=20,
                            topMargin=5,
                            bottomMargin=5)

    text_in_doc = []  # словарь документа

    # заглавие
    text_in_doc.append(Paragraph('Испытание зернового состава', styles['FontBold']))
    simple_title = zaglavie[title]
    text_in_doc.append(Paragraph(simple_title, styles['FontBoldSimple']))

    # дата и время
    time_in_document = time_on_user.strftime('%d.%m.%Y, время %H:%M')
    text_in_doc.append(Paragraph(time_in_document, styles['FontRegularRIGHT']))

    # таблица
    kol_vo_elements = len(table[0])
    shirina_yacheiki = col_size / kol_vo_elements
    t = Table(table, colWidths=shirina_yacheiki, rowHeights=36)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Общие настройки
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black),

                           ('TEXTCOLOR', (0, 0), (0, 0), '#f54768'),  # Вес
                           ('BACKGROUND', (0, 0), (0, 0), '#41436a'),
                           ('FONTNAME', (0, 0), (0, 0), 'NotoSansBold'),
                           ('FONTSIZE', (0, 0), (0, 0), 16),

                           ('TEXTCOLOR', (1, 0), (-1, 0), colors.white),  # Горизонтальная линия
                           ('BACKGROUND', (1, 0), (-1, 0), '#41436a'),
                           ('FONTNAME', (1, 0), (-1, 0), 'NotoSansRegular'),
                           ('FONTSIZE', (1, 0), (-1, 0), 12),

                           ('TEXTCOLOR', (0, 1), (0, -1), colors.white),  # Вертикальная линия
                           ('BACKGROUND', (0, 1), (0, -1), '#41436a'),
                           ('FONTNAME', (0, 1), (0, -1), 'NotoSansRegular'),
                           ('FONTSIZE', (0, 1), (0, -1), 13),

                           ('TEXTCOLOR', (1, 1), (-1, -1), colors.black),  # Основной текст
                           ('BACKGROUND', (1, 1), (-1, -1), colors.white),
                           ('FONTNAME', (1, 1), (-1, -1), 'NotoSansRegular'),
                           ('FONTSIZE', (1, 1), (-1, -1), 12)
                           ]))
    text_in_doc.append(t)

    # тех условия
    text_in_doc.append(Paragraph('Тех. условия', styles['FontBoldSimple']))
    if modified_tech_usl:
        t_u = Table(tech_usloviya, colWidths=col_size, rowHeights=36)
    else:
        tech_usloviya = update_tech_usl(tech_usloviya)
        t_u = Table(tech_usloviya, colWidths=col_size / 2, rowHeights=26)
    t_u.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'NotoSansRegular'),
                             ('FONTSIZE', (0, 0), (-1, -1), 12)]))
    text_in_doc.append(t_u)
    text_in_doc.append(Paragraph('_', styles['FontBoldSimple']))

    # картинка
    for file in os.scandir(directory):
        if file.name.endswith(".png"):
            img = Image(directory + file.name, width=col_size, height=row_size)
            text_in_doc.append(img)

    # ссылка на бота
    address = '<link href="' + bot_url + '">' + f'Создано в телеграм боте @{bot_name}' + '</link>'
    text_in_doc.append(Paragraph(address, styles['FontRegularRIGHTsimple']))

    doc.build(text_in_doc)

    return file_name


def zernovoi_testing_go(title: str,
                        user_text: str,
                        user_id: int,
                        ves_all: int):
    dno_state = check_dno_state(user_id)

    # list_names - название фракции
    list_names = frakc_names(title)

    # list_ves - масса материала на ситах
    list_ves = is_float(text_in_list(user_text))

    if list_ves is False:
        text = '<b>Неудача</b> с расчетом зернового состава.\nВводимые данные не явяются числами. Попробуйте снова.'
        list_names = False
        list_ves = False
        list_cho = False
        list_po = False
        list_pp = False
    elif len(list_ves) != len(list_names) - 1 + dno_state:
        text = '<b>Неудача</b> с расчетом зернового состава.\nКоличество введенных цифр больше или меньше нормы. ' \
               'Попробуйте снова. '
        list_names = False
        list_ves = False
        list_cho = False
        list_po = False
        list_pp = False
    else:
        text = '<b>Подсчет окончен</b>. Вот ваш результат'

        if dno_state == 0:
            dno = ves_all - sum(list_ves)
            list_ves.append(dno)

        # list_cho - частные остатки
        list_cho = list(map(lambda num: num * 100 / ves_all, list_ves))

        # list_po - полные остатки
        list_po = []
        for x in list_cho:
            try:
                list_po.append(x + list_po[-1])
            except IndexError:
                list_po.append(x)

        # list_pp - полный проход
        list_pp = list(map(lambda num: 100 - num, list_po))

    return text, list_names, list_ves, list_cho, list_po, list_pp, dno_state


def list_formatting(raw_list):
    finally_list = []
    for _ in raw_list:
        if int(_) == float(_):
            finally_list.append(str(int(_)))
        else:
            finally_list.append("{0:.2f}".format(_))
    return finally_list


# формируем таблицу в строковой форме
def zernovoi_table_str(list_names: list,
                       list_ves: list,
                       list_cho: list,
                       list_po: list,
                       list_pp: list,
                       ves_all: float):
    list_ves = list_formatting(list_ves)
    list_cho = list_formatting(list_cho)
    list_po = list_formatting(list_po)
    list_pp = list_formatting(list_pp)

    list_names.insert(0, "Вес")
    list_ves.insert(0, str(ves_all))
    list_cho.insert(0, "ч.о.")
    list_po.insert(0, "п.о.")
    list_pp.insert(0, "п.п.")

    zernovoi_table = [list_names,
                      list_ves,
                      list_cho,
                      list_po,
                      list_pp]

    return zernovoi_table
