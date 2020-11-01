from loader import is_float, grunt_parameters, users_data_base
from random import uniform


# испытание грунта
# возвращает список
def ispitanie_grunta(user_id, text):
    obrabotannii_text = text.split(' ')
    if len(obrabotannii_text) == 1:
        double_obrabotannii_text = obrabotannii_text[0].splitlines()
        finish_text_list = is_float(double_obrabotannii_text)
        if finish_text_list is False:
            return False
        else:
            if len(finish_text_list) == 2:
                finish_text_list.insert(0, 0)
                result = grunt_testing(user_id, finish_text_list)
                return result
            elif len(finish_text_list) == 3:
                result = grunt_testing(user_id, finish_text_list)
                return result
            else:
                return False
    elif len(obrabotannii_text) == 2:
        finish_text_list = is_float(obrabotannii_text)
        if finish_text_list is False:
            return False
        else:
            finish_text_list.insert(0, 0)
            result = grunt_testing(user_id, finish_text_list)
            return result
    elif len(obrabotannii_text) == 3:
        finish_text_list = is_float(obrabotannii_text)
        if finish_text_list is False:
            return False
        else:
            result = grunt_testing(user_id, finish_text_list)
            return result
    else:
        return False


def grunt_testing(user_id, spisok):
    try:
        tara = spisok[0]
        massa1 = spisok[1] - tara
        massa2 = spisok[2] - tara
        max_pl, v_ring = grunt_check_parameters(user_id)
        a_plotn_vl = massa1 / v_ring
        b_vlazn = (massa1 - massa2) / massa2 * 100
        c_plotn_suh = a_plotn_vl / (1 + 0.01 * b_vlazn)
        d_koef_uplotn = c_plotn_suh / max_pl

        a_plotn_vl = '{0:.2f}'.format(a_plotn_vl).replace('.', ',')
        b_vlazn = '{0:.2f}'.format(b_vlazn).replace('.', ',')
        c_plotn_suh = '{0:.2f}'.format(c_plotn_suh).replace('.', ',')
        d_koef_uplotn_2 = '{0:.2f}'.format(d_koef_uplotn).replace('.', ',')

        text = [
            f'Влажность: <b>{b_vlazn}</b> %',
            f'Плотность влажного грунта: <b>{a_plotn_vl}</b>',
            f'Плотность сухого грунта: <b>{c_plotn_suh}</b>',
            f'Коэфициент уплотнения: <b>{d_koef_uplotn_2}</b>'
        ]
        if d_koef_uplotn >= 0.975:
            text.append('👍')
        else:
            text.append('👎')
        return text
    except:
        return False


def grunt_check_parameters(user_id):
    if user_id in grunt_parameters:
        plotnost = grunt_parameters[user_id]['max_pl']
        v_ring = grunt_parameters[user_id]['v_ring']
    else:
        plotnost = users_data_base.find({'_id': user_id})[0]['max_pl']
        v_ring = users_data_base.find({'_id': user_id})[0]['v_ring']
        grunt_parameters.update({user_id: {'max_pl': plotnost, 'v_ring': v_ring}})

    return plotnost, v_ring


def grunt_change_plotnost(user_id: int, number):
    if user_id in grunt_parameters:
        grunt_parameters[user_id]['max_pl'] = float(number)
    else:
        v_ring = users_data_base.find({'_id': user_id})[0]['v_ring']
        grunt_parameters.update({user_id: {'max_pl': float(number), 'v_ring': v_ring}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'max_pl': float(number)}})


def grunt_change_v_ring(user_id: int, number):
    if user_id in grunt_parameters:
        grunt_parameters[user_id]['v_ring'] = float(number)
    else:
        plotnost = users_data_base.find({'_id': user_id})[0]['max_pl']
        grunt_parameters.update({user_id: {'max_pl': plotnost, 'v_ring': float(number)}})

    users_data_base.update_one({'_id': user_id}, {'$set': {'v_ring': float(number)}})


def grunt_random_create(user_id: int):
    max_pl, v_ring = grunt_check_parameters(user_id)
    while True:
        massa2 = uniform(140, 170)
        massa1 = massa2 + uniform(5, 30)
        a_plotn_vl = massa1 / v_ring
        b_vlazn = (massa1 - massa2) / massa2 * 100
        c_plotn_suh = a_plotn_vl / (1 + 0.01 * b_vlazn)
        d_koef_uplotn = c_plotn_suh / max_pl

        if 0.975 <= d_koef_uplotn <= 1:
            massa1 = '{0:.2f}'.format(massa1).replace('.', ',')
            massa2 = '{0:.2f}'.format(massa2).replace('.', ',')
            a_plotn_vl = '{0:.2f}'.format(a_plotn_vl).replace('.', ',')
            b_vlazn = '{0:.2f}'.format(b_vlazn).replace('.', ',')
            c_plotn_suh = '{0:.2f}'.format(c_plotn_suh).replace('.', ',')
            d_koef_uplotn_2 = '{0:.2f}'.format(d_koef_uplotn).replace('.', ',')
            text = [
                f'Вес влажного грунта: <b>{massa1}</b> г',
                f'Вес сухого грунта: <b>{massa2}</b> г',
                f'Влажность: <b>{b_vlazn}</b> %',
                f'Плотность влажного грунта: <b>{a_plotn_vl}</b>',
                f'Плотность сухого грунта: <b>{c_plotn_suh}</b>',
                f'Коэфициент уплотнения: <b>{d_koef_uplotn_2}</b>'
            ]
            return text
            break
        else:
            continue
