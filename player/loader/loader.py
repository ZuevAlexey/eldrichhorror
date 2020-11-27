import json
import os
from model.contact import Contact
from model.test import Test
from model.deck import Deck
from model.simpleContactCard import SimpleContactCard
from model.complexContactCard import ComplexContactCard
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
        CardBackType.ASIAN: _load_deck(contacts_directory_path, 'asian.json', CardBackType.EUROPEAN),
        CardBackType.EXPEDITION: _load_deck(contacts_directory_path, 'expedition.json', CardBackType.EXPEDITION, True),
        CardBackType.OTHER_WORLD: _load_deck(contacts_directory_path, 'otherWorld.json', CardBackType.OTHER_WORLD, True)
    }
    return result


def _load_deck(contacts_directory_path, deck_file_name, deck_card_back_type, is_complex=False):
    with open(os.path.join(contacts_directory_path, deck_file_name), encoding='utf-8') as json_file:
        common_contacts = json.load(json_file)
    result = Deck(deck_card_back_type)
    for card_data in common_contacts:
        if is_complex:
            result.add(_parse_complex_card(card_data))
        else:
            result.add(_parse_simple_card(card_data))
    return result


def _parse_simple_card(card_data):
    contacts = {}
    for location_type, contact in card_data['locations'].items():
        contacts[Location.from_str(location_type)] = parse_contact(contact)

    return SimpleContactCard(card_data['id'], card_data['version'], contacts)


def _parse_complex_card(card_data):
    contact = parse_contact(card_data, is_complex=True, result_parser=parse_contact)

    return ComplexContactCard(card_data['id'], card_data['version'], Location.from_str(card_data.get('location')), contact)


def _parse_contact(contact, is_complex=False, result_parser=None):
    test = parse_test(contact.get('test'), result_parser)
    return Contact(contact['step'], test, is_complex)


def _parse_test(test_data, result_parser=None):
    if test_data is None:
        test = None
    else:
        success = test_data.get('success')
        fail = test_data.get('fail')
        if result_parser is not None:
            success = result_parser(success)
            fail = result_parser(fail)

        test = Test(TestType.from_str(test_data['type']), test_data.get('modificator'), success, fail)
    return test


def _get_contacts_directory_path():
    path = os.getcwd()
    contacts_full_path = os.path.split(path)[0]
    return os.path.join(contacts_full_path, CONTACTS_RELATED_PATH)
