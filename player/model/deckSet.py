from model.enums.cardBackType import CardBackType


class DeckSet(object):
    def __init__(self, decks={}):
        super().__init__()
        self._decks = decks

    def shuffle(self):
        for deck in self._decks.values():
            deck.shuffle()

    def get_next_contact(self, card_back_type, location=None):
        card = self._decks[card_back_type].get_top()
        if location is None:
            return card.get_contact()
        else:
            return card.get_contact(location)

    def get_next_expedition_location(self):
        return self._decks[CardBackType.EXPEDITION].get_next_location()

    def get_deck(self, card_back_type):
        return self._decks[card_back_type]
