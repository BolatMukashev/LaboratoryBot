from loader import is_float_simple, beton_koeficients, beton_yacheistii_w, beton_parameters, users_data_base
from datetime import datetime, date, timedelta


def is_date(text):
    try:
        create_date = datetime.strptime(text, '%d.%m.%Y').date()
        return create_date
    except:
        return False


def days_names(n):
    n = str(n)
    lis = ["день", "дня", "дней"]

    if len(n) == 1 or (len(n) == 2 and n[0] != "1"):
        if n[-1] == "0":
            return lis[2]
        elif n[-1] == "1":
            return lis[0]
        elif n[-1] == "2" or n[-1] == "3" or n[-1] == "4":
            return lis[1]
        else:
            return lis[2]

    elif len(n) == 3 and n[-2] != "1":
        if n[-1] == "0":
            return lis[2]
        elif n[-1] == "1":
            return lis[0]
        elif n[-1] == "2" or n[-1] == "3" or n[-1] == "4":
            return lis[1]
        else:
            return lis[2]

    else:
        return lis[2]


# нельзя передавать обычную строку, её сначала нудно преобразовать в дату через функцию is_date()
def beton_raschet_7and28(create_date):
    # create_date_from_user = create_date.strftime('%d.%m.%Y')

    now = date.today()

    time7 = create_date + timedelta(days=+7)
    time28 = create_date + timedelta(days=+28)

    schet7 = time7 - now
    schet28 = time28 - now

    if schet7.days > 0:
        glagol7 = 'будет'
    elif schet7.days == 0:
        glagol7 = 'сегодня'
    else:
        glagol7 = 'было'

    if schet28.days > 0:
        glagol28 = 'будет'
    elif schet28.days == 0:
        glagol28 = 'сегодня'
    else:
        glagol28 = 'было'

    time7 = time7.strftime('%d.%m.%Y')
    time28 = time28.strftime('%d.%m.%Y')

    vremya_zhizhni = now - create_date
    day_name = days_names(vremya_zhizhni.days)
    if vremya_zhizhni.days < 0:
        future_date = -vremya_zhizhni.days
        finaly_text = [
            f'Кубик будет создан через <b>{future_date}</b> {day_name}',
            f'7 суток {glagol7} <b>{time7}</b>',
            f'28 суток {glagol28} <b>{time28}</b>'
        ]
    elif vremya_zhizhni.days == 0:
        finaly_text = [
            f'Кубик был сформован <b>сегодня</b>',
            f'7 суток {glagol7} <b>{time7}</b>',
            f'28 суток {glagol28} <b>{time28}</b>'
        ]
    else:
        finaly_text = [
            f'Кубик был сформован <b>{vremya_zhizhni.days}</b> {day_name} назад',
            f'7 суток {glagol7} <b>{time7}</b>',
            f'28 суток {glagol28} <b>{time28}</b>'
        ]
    return finaly_text


def ispitanie_betona_prochnost(user_id, text):
    number = is_float_simple(text)
    if number is False:
        return False
    else:
        beton_size, beton_metric, beton_type, beton_w = beton_parameters_check(user_id)
        kw_a = 0
        if beton_type == 'tyazholii':
            kw_a = beton_koeficients[beton_size]
        elif beton_type == 'yacheistii':
            kw_a = beton_yacheistii_w[beton_w]
        if beton_metric == 'кН':
            number_kN = number
            try:
                number_MPa = ((number * 1000) / beton_size ** 2) * kw_a
            except ZeroDivisionError:
                number_MPa = 0
            beton_class = beton_class_check(number_MPa)
            kgs = number_MPa * 10.197162
            text = [
                f'Прочность в кН: <b>{number_kN}</b>',
                f'Прочность в МПа: <b>{"{0:.2f}".format(number_MPa)}</b>',
                f'Прочность в кГс/см²: <b>{"{0:.2f}".format(kgs)}</b>',
                f'Марка бетона: <b>{beton_class}</b>'
            ]
        elif beton_metric == 'МПа':
            number_MPa = number
            try:
                number_kN = ((number_MPa * beton_size ** 2) / 1000) / kw_a
            except ZeroDivisionError:
                number_kN = 0
            beton_class = beton_class_check(number_MPa)
            kgs = number_MPa * 10.197162
            text = [
                f'Прочность в МПа: <b>{number_MPa}</b>',
                f'Прочность в кН: <b>{"{0:.2f}".format(number_kN)}</b>',
                f'Прочность в кГс/см²: <b>{"{0:.2f}".format(kgs)}</b>',
                f'Марка бетона: <b>{beton_class}</b>'
            ]
        else:  # кгс
            number_kGs = number
            number_MPa = number_kGs * 0.0980665
            try:
                number_kN = ((number_MPa * beton_size ** 2) / 1000) / kw_a
            except ZeroDivisionError:
                number_kN = 0
            beton_class = beton_class_check(number_MPa)
            text = [
                f'Прочность в кГс/см²: <b>{"{0:.2f}".format(number_kGs)}</b>',
                f'Прочность в МПа: <b>{"{0:.2f}".format(number_MPa)}</b>',
                f'Прочность в кН: <b>{"{0:.2f}".format(number_kN)}</b>',
                f'Марка бетона: <b>{beton_class}</b>'
            ]
        return text


def beton_parameters_check(user_id):
    if user_id in beton_parameters:
        beton_size = beton_parameters[user_id]['beton_size']
        beton_metric = beton_parameters[user_id]['beton_metric']
        beton_type = beton_parameters[user_id]['beton_type']
        beton_w = beton_parameters[user_id]['beton_w']
    else:
        beton_size = users_data_base.find({'_id': user_id})[0]['beton_size']
        beton_metric = users_data_base.find({'_id': user_id})[0]['beton_metric']
        beton_type = users_data_base.find({'_id': user_id})[0]['beton_type']
        beton_w = users_data_base.find({'_id': user_id})[0]['beton_w']
        beton_parameters.update({user_id: {'beton_size': beton_size, 'beton_metric': beton_metric,
                                           'beton_type': beton_type, 'beton_w': beton_w}})

    return beton_size, beton_metric, beton_type, beton_w


def beton_change_size(user_id: int, number):
    if user_id in beton_parameters:
        beton_parameters[user_id]['beton_size'] = int(number)
    else:
        beton_metric = users_data_base.find({'_id': user_id})[0]['beton_metric']
        beton_type = users_data_base.find({'_id': user_id})[0]['beton_type']
        beton_w = users_data_base.find({'_id': user_id})[0]['beton_w']
        beton_parameters.update({user_id: {'beton_size': int(number), 'beton_metric': beton_metric,
                                           'beton_type': beton_type, 'beton_w': beton_w}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'beton_size': int(number)}})


def beton_change_metric(user_id: int, metric: str):
    if user_id in beton_parameters:
        beton_parameters[user_id]['beton_metric'] = metric
    else:
        beton_size = users_data_base.find({'_id': user_id})[0]['beton_size']
        beton_type = users_data_base.find({'_id': user_id})[0]['beton_type']
        beton_w = users_data_base.find({'_id': user_id})[0]['beton_w']
        beton_parameters.update({user_id: {'beton_size': beton_size, 'beton_metric': metric,
                                           'beton_type': beton_type, 'beton_w': beton_w}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'beton_metric': metric}})


def beton_change_type(user_id: int, beton_type: str):
    if user_id in beton_parameters:
        beton_parameters[user_id]['beton_type'] = beton_type
    else:
        beton_size = users_data_base.find({'_id': user_id})[0]['beton_size']
        beton_metric = users_data_base.find({'_id': user_id})[0]['beton_metric']
        beton_w = users_data_base.find({'_id': user_id})[0]['beton_w']
        beton_parameters.update({user_id: {'beton_size': beton_size, 'beton_metric': beton_metric,
                                           'beton_type': beton_type, 'beton_w': beton_w}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'beton_type': beton_type}})


def beton_change_w(user_id: int, number):
    if user_id in beton_parameters:
        beton_parameters[user_id]['beton_w'] = int(number)
    else:
        beton_size = users_data_base.find({'_id': user_id})[0]['beton_size']
        beton_metric = users_data_base.find({'_id': user_id})[0]['beton_metric']
        beton_type = users_data_base.find({'_id': user_id})[0]['beton_type']
        beton_parameters.update({user_id: {'beton_size': beton_size, 'beton_metric': beton_metric,
                                           'beton_type': beton_type, 'beton_w': int(number)}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'beton_w': int(number)}})


def beton_class_check(g):
    if g > 102.7:
        text = "B80 M1000"
    elif g > 91.4:
        text = "B75 M1000"
    elif g > 89.9:
        text = "B70 M900"
    elif g > 83.4:
        text = "B65 M900"
    elif g > 77:
        text = "B60 M800"
    elif g > 70.6:
        text = "B55 M700"
    elif g > 64.2:
        text = "B50 M700"
    elif g > 57.8:
        text = "B45 M600"
    elif g > 51.3:
        text = "B40 M550"
    elif g > 44.9:
        text = "B35 M450"
    elif g > 38.5:
        text = "B30 M400"
    elif g > 35.3:
        text = "B27,5 M350"
    elif g > 32.1:
        text = "B25 M350"
    elif g > 28.9:
        text = "B22,5 M300"
    elif g > 25.7:
        text = "B20 M250"
    elif g > 19.3:
        text = "B15 M200"
    elif g > 16:
        text = "B12,5 M150"
    elif g > 12.8:
        text = "B10 M150"
    elif g > 9.6:
        text = "B7,5 M100"
    elif g > 6.4:
        text = "B5 M75"
    elif g > 4.5:
        text = "B3,5 M50"
    else:
        text = "B0 M0"
    return text
