class CreatePDF(object):

    def __init__(self, user_id, user_state, ves_all, text, list_names):
        self.user_id = user_id
        self.user_state = user_state
        self.ves_all = ves_all
        self.text = text
        self.list_names = list_names
        self.ves_all = ves_all
        self.user_id = user_id
        self.user_state = user_state
        self.ves_all = ves_all

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"



    user_id = message.from_user.id
    user_state = check_state(user_id)
    await message.answer('ожидайте...')
    # ves_all = check_ves_all(user_id, user_state + '_all')
    ves_all = 2500
    text, list_names, list_ves, list_cho, list_po, list_pp, dno_state = zernovoi_testing_go(title=user_state,
                                                                                            user_text=answer1,
                                                                                            user_id=user_id,
                                                                                            ves_all=ves_all)
    if text == '<b>Подсчет окончен</b>. Вот ваш результат':
        zernovoi_table = zernovoi_table_str(list_names, list_ves, list_cho, list_po, list_pp, ves_all)
        tech_usloviya = standart_technical_specific(user_state, list_pp, list_names[1:])
        create_grafic(user_id, list_pp, user_state, orientation='landscape')
        file_name = create_pdf(user_id=user_id,
                               title=user_state,
                               table=zernovoi_table,
                               technical_specific=tech_usloviya,
                               page_orientation='landscape')
