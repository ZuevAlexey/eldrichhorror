from tkinter import *
from loader import loader
from model.enums.cardBackType import CardBackType
from model.enums.location import Location
from model.enums.testType import TestType


def create_card_button(master, text, command):
    card_button = Button(master, text=text, width=20, height=2, font=('Arial', 30), command=command)
    card_button.pack(side=LEFT)


def create_main_window():
    window = Toplevel()
    window.title('Контакты')
    geometry_config(window, 1400, 350)

    deck_set = loader.load_decks()
    deck_set.shuffle()

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()

    create_card_button(frame1, 'Город', lambda: town_contact(deck_set))
    create_card_button(frame1, 'Глушь', lambda: town_contact(deck_set))
    create_card_button(frame1, 'Море', lambda: town_contact(deck_set))
    create_card_button(frame2, 'Арехэм', lambda: town_contact(deck_set))
    create_card_button(frame2, 'Сан-Франциско', lambda: town_contact(deck_set))
    create_card_button(frame2, 'Буйный Сайрес', lambda: town_contact(deck_set))
    create_card_button(frame3, 'Врата', lambda: town_contact(deck_set))
    create_card_button(frame3, 'Экспедиция', lambda: town_contact(deck_set))
    create_card_button(frame3, 'Улика', lambda: town_contact(deck_set))


def town_contact(deck_set):
    window = Toplevel()
    window.title('Город грехов')
    geometry_config(window, 380, 700)

    next_city_contact = deck_set.get_next_contact(CardBackType.COMMON, Location.CITY)

    text_form = Text(master=window, font=('Arial', 20), width=25, height=20, wrap=WORD)
    text_form.pack()
    text_form.insert(1.0, f'{next_city_contact.step}\n\n')

    if next_city_contact.has_test():
        text_form.insert(3.0, f'Пройдите проверку {test_type_translate(next_city_contact.test.type)}')

        if next_city_contact.test.has_modificator():
            text_form.insert(4.0, next_city_contact.test.modificator)

        button_success = Button(master=window, text='УСПЕХ', width=20, height=2, font=('Arial', 13))
        button_success.pack(side=LEFT)
        button_fail = Button(master=window, text='ПРОВАЛ', width=20, height=2, font=('Arial', 13))
        button_fail.pack(side=LEFT)

        button_success['command'] = lambda: check_button_event(text_form, button_success, button_fail,
                                                               next_city_contact.test.success)
        button_fail['command'] = lambda: check_button_event(text_form, button_success, button_fail,
                                                            next_city_contact.test.fail)


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
