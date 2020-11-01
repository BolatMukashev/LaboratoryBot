from loader import users_data_base, check_dno_state


def settings_change_dno_true(user_id: int, dno_status: int):
    users_data_base.update_one({'_id': user_id}, {'$set': {'dno': dno_status}})


# можно дополнить кол-во проверяемых пунктов в меню настроек
def main_settings_check_parameters(user_id):
    dno_check = check_dno_state(user_id)
    return dno_check