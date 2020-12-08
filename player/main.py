from tkinter import *
from loader import loader
from model.enums.cardBackType import CardBackType
from model.enums.location import Location
from model.enums.testType import TestType


def create_main_window():
    window = Toplevel()
    window.title('Контакты')
    geometry_config(window, 1400, 350)

    deck_set = loader.load_decks()
    deck_set.shuffle()

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    frame4 = Frame(window)
    frame5 = Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()

    card_button_town = Button(master=frame1, text='Общие: Город', width=20, height=2, font=('Arial', 30))
    card_button_town.pack(side=LEFT)
    card_button_wilderness = Button(master=frame1, text='Общие: Глушь', width=20, height=2, font=('Arial', 30))
    card_button_wilderness.pack(side=LEFT)
    card_button_sea = Button(master=frame1, text='Общие: Море', width=20, height=2, font=('Arial', 30))
    card_button_sea.pack(side=LEFT)
    card_button_arkham = Button(master=frame2, text='Арехэм', width=20, height=2, font=('Arial', 30))
    card_button_arkham.pack(side=LEFT)
    card_button_san_francisco = Button(master=frame2, text='Сан-Франциско', width=20, height=2, font=('Arial', 30))
    card_button_san_francisco.pack(side=LEFT)
    card_button_buenos_aires = Button(master=frame2, text='Буйный Сайрес', width=20, height=2, font=('Arial', 30))
    card_button_buenos_aires.pack(side=LEFT)

    button_name_list = [card_button_town, card_button_wilderness, card_button_sea, card_button_arkham, card_button_san_francisco, card_button_buenos_aires]

    card_button_town['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.COMMON, Location.CITY,
                                                       button_name_list)
    card_button_wilderness['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.COMMON,
                                                             Location.WILDERNESS, button_name_list)
    card_button_sea['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.COMMON, Location.SEA,
                                                      button_name_list)
    card_button_arkham['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.AMERICAN,
                                                         Location.ARKHAM, button_name_list)
    card_button_san_francisco['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.AMERICAN,
                                                                Location.SAN_FRANCISCO, button_name_list)
    card_button_buenos_aires['command'] = lambda: play_contact(window, frame1, frame2, deck_set, CardBackType.AMERICAN,
                                                               Location.BUENOS_AIRES, button_name_list)

    # create_card_button(frame1, 'Общие: Город', lambda: play_contact(deck_set, CardBackType.COMMON, Location.CITY))
    # create_card_button(frame1, 'Общие: Глушь', lambda: play_contact(deck_set, CardBackType.COMMON, Location.WILDERNESS))
    # create_card_button(frame1, 'Общие: Море', lambda: play_contact(deck_set, CardBackType.COMMON, Location.SEA))
    # create_card_button(frame2, 'Арехэм', lambda: play_contact(deck_set, CardBackType.AMERICAN, Location.ARKHAM))
    # create_card_button(frame2, 'Сан-Франциско', lambda: play_contact(deck_set, CardBackType.AMERICAN, Location.SAN_FRANCISCO))
    # create_card_button(frame2, 'Буйный Сайрес', lambda: play_contact(deck_set, CardBackType.AMERICAN, Location.BUENOS_AIRES))
    # create_card_button(frame3, 'Токио', lambda: play_contact(deck_set, CardBackType.ASIAN, Location.TOKYO))
    # create_card_button(frame3, 'Сидней', lambda: play_contact(deck_set, CardBackType.ASIAN, Location.SYDNEY))
    # create_card_button(frame3, 'Шанхай', lambda: play_contact(deck_set, CardBackType.ASIAN, Location.ZANHAE))
    # create_card_button(frame4, 'Лондон', lambda: play_contact(deck_set, CardBackType.EUROPEAN, Location.LONDON))
    # create_card_button(frame4, 'Рим', lambda: play_contact(deck_set, CardBackType.EUROPEAN, Location.ROME))
    # create_card_button(frame4, 'Стамбул', lambda: play_contact(deck_set, CardBackType.EUROPEAN, Location.ISTANBUL))
    # create_card_button(frame5, 'Улика: Город', lambda: play_contact(deck_set, CardBackType.RESEARCH, Location.CITY))
    # create_card_button(frame5, 'Улика: Глушь', lambda: play_contact(deck_set, CardBackType.RESEARCH, Location.WILDERNESS))
    # create_card_button(frame5, 'Улика: Море', lambda: play_contact(deck_set, CardBackType.RESEARCH, Location.SEA))


def play_contact(window, text_frame, button_frame, deck_set, card_back_type, location, button_name_list):
    for button_name in button_name_list:
        button_name.pack_forget()

    geometry_config(window, 380, 700)

    contact = deck_set.get_next_contact(card_back_type, location)

    text_form = Text(master=text_frame, font=('Arial', 20), width=25, height=20, wrap=WORD)
    text_form.pack()
    text_form.insert(1.0, f'{contact.step}\n\n')

    if contact.has_test():
        text_form.insert(3.0, f'Пройдите проверку {test_type_translate(contact.test.type)}')

        if contact.test.has_modificator():
            text_form.insert(4.0, contact.test.modificator)

        button_success = Button(master=button_frame, text='УСПЕХ', width=20, height=2, font=('Arial', 13))
        button_success['command'] = lambda: check_button_event(text_form, button_success, button_fail,
                                                               contact.test.success)
        button_success.pack(side=LEFT)

        button_fail = Button(master=button_frame, text='ПРОВАЛ', width=20, height=2, font=('Arial', 13))
        button_fail['command'] = lambda: check_button_event(text_form, button_success, button_fail,
                                                            contact.test.fail)
        button_fail.pack(side=LEFT)

    button_exit = Button(master=button_frame, text='НАЗАД', width=20, height=2, font=('Arial', 13))
    button_exit['command'] = lambda: button_exit_event(window, text_form, button_exit, button_name_list)
    button_exit.pack()


def geometry_config(master, master_width, master_height):
    width = master.winfo_screenwidth()
    height = master.winfo_screenheight()
    width = (width - master_width) // 2
    height = (height - master_height) // 2
    master.geometry(f'{master_width}x{master_height}+{width}+{height}')


def check_button_event(text_form, button_success, button_fail, text):
    button_success.pack_forget()
    button_fail.pack_forget()
    text_form.insert(5.0, '\n\nНичего не произошло' if text is None else f'\n\n{text}')


def button_exit_event(window, text_form, button_exit, button_name_list):
    text_form.pack_forget()
    button_exit.pack_forget()

    for button_name in button_name_list:
        button_name.pack(side=LEFT)

    geometry_config(window, 1400, 350)


def test_type_translate(test_type):
    if test_type == TestType.LORE:
        return 'ЗНАНИЕ'
    elif test_type == TestType.COMMUNICATION:
        return 'ОБЩЕНИЕ'
    elif test_type == TestType.ATTENTION:
        return 'ВНИМАНИЕ'
    elif test_type == TestType.STRENGTH:
        return 'СИЛА'
    elif test_type == TestType.WILL:
        return 'ВОЛЯ'
    elif test_type == TestType.DECISION:
        return 'РЕШЕНИЕ'
    elif test_type == TestType.FIGHT:
        return 'ФАЙТ'


def main():
    root = Tk()
    root.title('Древний ужас')
    geometry_config(root, 400, 400)

    button_start = Button(text='Начать игру', width=10, height=5, font=('Arial', 50), command=create_main_window)
    button_start.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
