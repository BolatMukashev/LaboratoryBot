from loader import users_data_base


def sheben_check_all_parameters(user_id: int):
    all_all = users_data_base.find({'_id': user_id})[0]
    all_parameters_text = [
        'Сейчас установлены следующие массы проб:',
        f'Масса пробы для щебня фр.5-20мм: <b>{all_all["щебень:5-20_all"]}</b> г',
        f'Масса пробы для щебня фр.5-10мм: <b>{all_all["щебень:5-10_all"]}</b> г',
        f'Масса пробы для щебня фр.10-20мм: <b>{all_all["щебень:10-20_all"]}</b> г',
        f'Масса пробы для щебня фр.20-40мм: <b>{all_all["щебень:20-40_all"]}</b> г',
        f'Масса пробы для щебня фр.40-70мм: <b>{all_all["щебень:40-70_all"]}</b> г'
    ]
    return all_parameters_text


def sheben_change_all(user_id: int, fraction: str, user_text: int):
    fraction = fraction.replace('_', ':')
    users_data_base.update_one({'_id': user_id}, {'$set': {fraction + '_all': user_text}})


def sheben_settings_reset_all(user_id: int):
    users_data_base.update_one({'_id': user_id}, {'$set': {'щебень:5-20_all': 5000}})
    users_data_base.update_one({'_id': user_id}, {'$set': {'щебень:5-10_all': 5000}})
    users_data_base.update_one({'_id': user_id}, {'$set': {'щебень:10-20_all': 5000}})
    users_data_base.update_one({'_id': user_id}, {'$set': {'щебень:20-40_all': 10000}})
    users_data_base.update_one({'_id': user_id}, {'$set': {'щебень:40-70_all': 10000}})
