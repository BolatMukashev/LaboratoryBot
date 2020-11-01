from loader import modul_krupnosti


def tech_usl_otsev(list_po: list, list_ves: list):
    mk = modul_krupnosti(list_po)
    ostatok_na_05 = list_po[4]
    soderzhanie_8 = list_ves[0]
    soderzhanie_4 = list_ves[1]
    soderzhanie_menee_0125 = sum(list_ves[7:])

    # модуль крупности
    if mk > 3.8:
        mk_text = 'Очень крупный'
    elif 3.3 < mk <= 3.8:
        mk_text = 'Повышенной крупности'
    elif 2.8 < mk <= 3.3:
        mk_text = 'Крупный'
    elif 2.3 < mk <= 2.8:
        mk_text = 'Средний'
    elif 1.8 < mk <= 2.3:
        mk_text = 'Мелкий'
    else:
        mk_text = 'Слишком мелкий'

    # остаток на сите 0,5 мм
    if ostatok_na_05 > 85:
        ostatok_na_05_text = 'Очень крупный'
    elif 75 < ostatok_na_05 <= 85:
        ostatok_na_05_text = 'Повышенной крупности'
    elif 55 < ostatok_na_05 <= 75:
        ostatok_na_05_text = 'Крупный'
    elif 40 < ostatok_na_05 <= 55:
        ostatok_na_05_text = 'Средний'
    elif 20 < ostatok_na_05 <= 40:
        ostatok_na_05_text = 'Мелкий'
    else:
        ostatok_na_05_text = 'Слишком мелкий'

    #  Содержание зерен крупностью св. 8, 4 и менее 0,125 мм I класс
    if soderzhanie_8 <= 0.5 and soderzhanie_4 <= 5 and soderzhanie_menee_0125 <= 7:
        soderzhanie1_text = 'Мелкий'
    elif soderzhanie_8 <= 0.5 and soderzhanie_4 <= 5 and soderzhanie_menee_0125 <= 3.5:
        soderzhanie1_text = 'Повышенной крупности, крупный и средний'
    elif soderzhanie_8 <= 2 and soderzhanie_4 <= 10 and soderzhanie_menee_0125 <= 2:
        soderzhanie1_text = 'Очень крупный '
    else:
        soderzhanie1_text = 'Не относится к I классу'

    #  Содержание зерен крупностью св. 8, 4 и менее 0,125 мм II класс
    if soderzhanie_8 <= 0.5 and soderzhanie_4 <= 10 and soderzhanie_menee_0125 <= 14:
        soderzhanie2_text = 'Мелкий'
    elif soderzhanie_8 <= 2 and soderzhanie_4 <= 12 and soderzhanie_menee_0125 <= 10:
        soderzhanie2_text = 'Повышенной крупности, крупный и средний'
    elif soderzhanie_8 <= 5 and soderzhanie_4 <= 15 and soderzhanie_menee_0125 <= 7:
        soderzhanie2_text = 'Очень крупный '
    else:
        soderzhanie2_text = 'Не относится ко II классу'

    mk = '{0:.3f}'.format(mk)
    finally_text = [[f'Модуль крупности = {mk} - {mk_text}'],
                    [f'По остатку на сите 0,5 мм - {ostatok_na_05_text}'],
                    [f'По содержанию зерен крупностью свыше 8, 4 мм \nи менее 0,125 мм, для I класса - {soderzhanie1_text}'],
                    [f'По содержанию зерен крупностью свыше 8, 4 мм \nи менее 0,125 мм, для II класса - {soderzhanie2_text}']]
    return finally_text
