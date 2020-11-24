import json
import os
from model.contact import Contact
from model.test import Test
from model.deck import Deck
from model.simpleContactCard import SimpleContactCard
from model.enums.cardBackType import CardBackType
from model.enums.testType import TestType
from model.enums.location import Location


CONTACTS_RELATED_PATH = 'data\\contacts'


def load_decks():
    contacts_directory_path = _get_contacts_directory_path()
    result = {
        CardBackType.COMMON: _load_deck(contacts_directory_path, 'common.json', CardBackType.COMMON),
        CardBackType.AMERICAN: _load_deck(contacts_directory_path, 'american.json', CardBackType.AMERICAN),
        CardBackType.EUROPEAN: _load_deck(contacts_directory_path, 'european.json', CardBackType.EUROPEAN),
        CardBackType.ASIAN: _load_deck(contacts_directory_path, 'asian.json', CardBackType.EUROPEAN)
    }
    return result


def _load_deck(contacts_directory_path, deck_file_name, deck_card_back_type):
    with open(os.path.join(contacts_directory_path, deck_file_name), encoding='utf-8') as json_file:
        common_contacts = json.load(json_file)
    result = Deck(deck_card_back_type)
    for card_data in common_contacts:
        contacts = {}
        for location_type, contact in card_data['locations'].items():
            test_data = contact.get('test')
            if test_data is None:
                test = None
            else:
                test = Test(TestType.from_str(test_data['type']), test_data.get('modificator'), test_data.get('success'),
                            test_data.get('fail'))
            contacts[Location.from_str(location_type)] = Contact(contact['step'], test)

        card = SimpleContactCard(card_data['id'], card_data['version'], contacts)
        result.add(card)
    return result


def _get_contacts_directory_path():
    path = os.getcwd()
    contacts_full_path = os.path.split(path)[0]
    return os.path.join(contacts_full_path, CONTACTS_RELATED_PATH)
