from tkinter import *
from loader import loader
from model.enums.cardBackType import CardBackType
from model.enums.location import Location
from model.enums.testType import TestType


MAIN_WINDOW_WIDTH = 1400
MAIN_WINDOW_HEIGHT = 740
CONTACT_WINDOW_WIDTH = 500
CONTACT_WINDOW_HEIGHT = 900


def create_main_window():
    window = Toplevel()
    window.title('Контакты')
    geometry_config(window, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)

    deck_set = loader.load_decks()
    deck_set.shuffle()

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    frame4 = Frame(window)
    frame5 = Frame(window)
    frame6 = Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()
    frame6.pack()

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
    card_button_tokyo = Button(master=frame3, text='Токио', width=20, height=2, font=('Arial', 30))
    card_button_tokyo.pack(side=LEFT)
    card_button_sydney = Button(master=frame3, text='Сидней', width=20, height=2, font=('Arial', 30))
    card_button_sydney.pack(side=LEFT)
    card_button_zanhae = Button(master=frame3, text='Шанхай', width=20, height=2, font=('Arial', 30))
    card_button_zanhae.pack(side=LEFT)
    card_button_london = Button(master=frame4, text='Лондон', width=20, height=2, font=('Arial', 30))
    card_button_london.pack(side=LEFT)
    card_button_rome = Button(master=frame4, text='Рим', width=20, height=2, font=('Arial', 30))
    card_button_rome.pack(side=LEFT)
    card_button_istambul = Button(master=frame4, text='Стамбул', width=20, height=2, font=('Arial', 30))
    card_button_istambul.pack(side=LEFT)
    card_button_research_city = Button(master=frame5, text='Улика: Город', width=20, height=2, font=('Arial', 30))
    card_button_research_city.pack(side=LEFT)
    card_button_research_wilderness = Button(master=frame5, text='Улика: Глушь', width=20, height=2, font=('Arial', 30))
    card_button_research_wilderness.pack(side=LEFT)
    card_button_research_sea = Button(master=frame5, text='Улика: Море', width=20, height=2, font=('Arial', 30))
    card_button_research_sea.pack(side=LEFT)
    card_button_expedition = Button(master=frame6, text='Экспедиция', width=20, height=2, font=('Arial', 30))
    card_button_expedition.pack(side=LEFT)
    card_button_other_world = Button(master=frame6, text='Врата', width=20, height=2, font=('Arial', 30))
    card_button_other_world.pack(side=LEFT)

    button_name_list = [card_button_town, card_button_wilderness, card_button_sea, card_button_arkham,
                        card_button_san_francisco, card_button_buenos_aires, card_button_tokyo, card_button_sydney,
                        card_button_zanhae, card_button_london, card_button_rome, card_button_istambul,
                        card_button_research_city, card_button_research_wilderness, card_button_research_sea,
                        card_button_expedition, card_button_other_world]

    card_button_town['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list,
                                                       CardBackType.COMMON, Location.CITY)
    card_button_wilderness['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.COMMON,
                                                             Location.WILDERNESS)
    card_button_sea['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.COMMON, Location.SEA)
    card_button_arkham['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.AMERICAN,
                                                         Location.ARKHAM)
    card_button_san_francisco['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.AMERICAN,
                                                                Location.SAN_FRANCISCO)
    card_button_buenos_aires['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.AMERICAN,
                                                               Location.BUENOS_AIRES)
    card_button_tokyo['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.ASIAN,
                                                               Location.TOKYO)
    card_button_sydney['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.ASIAN,
                                                               Location.SYDNEY)
    card_button_zanhae['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.ASIAN,
                                                               Location.ZANHAE)
    card_button_london['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.EUROPEAN,
                                                               Location.LONDON)
    card_button_rome['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.EUROPEAN,
                                                               Location.ROME)
    card_button_istambul['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.EUROPEAN,
                                                               Location.ISTANBUL)
    card_button_research_city['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.RESEARCH,
                                                               Location.CITY)
    card_button_research_wilderness['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.RESEARCH,
                                                               Location.WILDERNESS)
    card_button_research_sea['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.RESEARCH,
                                                               Location.SEA)
    card_button_expedition['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.OTHER_WORLD)
    card_button_other_world['command'] = lambda: play_contact(window, frame1, frame2, deck_set, button_name_list, CardBackType.OTHER_WORLD)


def play_contact(window, text_frame, button_frame, deck_set, button_name_list, card_back_type, location=None):
    for button_name in button_name_list:
        button_name.pack_forget()

    geometry_config(window, CONTACT_WINDOW_WIDTH, CONTACT_WINDOW_HEIGHT)

    contact = deck_set.get_next_contact(card_back_type, location)

    text_form = Text(master=text_frame, font=('Arial', 20), width=33, height=26, wrap=WORD)
    text_form.pack()

    text_form.insert(1.0, f'{contact.step}\n\n')

    if contact.has_test():
        button_success = Button(master=button_frame, text='УСПЕХ', width=27, height=3, font=('Arial', 13))
        button_fail = Button(master=button_frame, text='ПРОВАЛ', width=27, height=3, font=('Arial', 13))
        button_success.pack(side=LEFT)
        button_fail.pack(side=LEFT)

        text_form.insert(3.0, f'Пройдите проверку {test_type_translate(contact.test.type)}')

        if contact.test.has_modificator():
            text_form.insert(4.0, contact.test.modificator)

        if contact.is_complex:
            button_success['command'] = lambda: check_button_event_complex(text_form, button_success, button_fail,
                                                                           contact, True)
            button_fail['command'] = lambda: check_button_event_complex(text_form, button_success, button_fail,
                                                                        contact, False)
        else:
            button_success['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail,
                                                                          contact.test.success)
            button_fail['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail, contact.test.fail)

    button_exit = Button(master=button_frame, text='НАЗАД', width=20, height=3, font=('Arial', 13))
    button_exit['command'] = lambda: button_exit_event(window, text_form, button_exit, button_name_list)
    button_exit.pack()


def geometry_config(master, master_width, master_height):
    width = master.winfo_screenwidth()
    height = master.winfo_screenheight()
    width = (width - master_width) // 2
    height = (height - master_height) // 2
    master.geometry(f'{master_width}x{master_height}+{width}+{height}')


def check_button_event_simple(text_form, button_success, button_fail, text):
    text_form.insert(8.0, '\n\nНичего не произошло' if text is None else f'\n\n{text}')
    button_success.pack_forget()
    button_fail.pack_forget()


def check_button_event_complex(text_form, button_success, button_fail, contact, event_is_success):
    if event_is_success:
        text_form.insert(5.0, f'\n\n{contact.test.success.step}\n\n')
        if contact.test.success.has_test():
            text_form.insert(7.0, f'Пройдите проверку {test_type_translate(contact.test.success.test.type)}')
            if contact.test.success.test.has_modificator():
                text_form.insert(8.0, contact.test.success.test.modificator)
            button_success['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail,
                                                                          contact.test.success.test.success)
            button_fail['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail,
                                                                       contact.test.success.test.fail)
        else:
            button_success.pack_forget()
            button_fail.pack_forget()

    else:
        text_form.insert(5.0, f'\n\n{contact.test.fail.step}\n\n')
        if contact.test.fail.has_test():
            text_form.insert(7.0, f'Пройдите проверку {test_type_translate(contact.test.fail.test.type)}')
            if contact.test.fail.test.has_modificator():
                text_form.insert(8.0, contact.test.fail.test.modificator)
            button_success['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail,
                                                                          contact.test.fail.test.success)
            button_fail['command'] = lambda: check_button_event_simple(text_form, button_success, button_fail,
                                                                       contact.test.fail.test.fail)
        else:
            button_success.pack_forget()
            button_fail.pack_forget()


def button_exit_event(window, text_form, button_exit, button_name_list):
    text_form.pack_forget()
    button_exit.pack_forget()

    for button_name in button_name_list:
        button_name.pack(side=LEFT)

    geometry_config(window, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)


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
