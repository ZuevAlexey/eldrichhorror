import random


class Deck(object):
    DECK_ALREADY_SHUFFLED = 'The deck is already shuffled'
    DECK_NOT_SHUFFLED = "The deck isn't shuffled"
    DECK_NOT_REUSABLE = "The deck isn't reusable"

    def __init__(self, cardBackType, reusable=True):
        super().__init__()
        self.cardBackType = cardBackType
        self._cards = {}
        self._cardStack = []
        self._is_shuffled = False
        self._reusable = reusable

    def add(self, card):
        card_id = card.get_unique_id()
        self._cards[card_id] = card

    @property
    def capacity(self):
        return len(self._cards)

    @property
    def size(self):
        return len(self._cardStack)

    def shuffle(self):
        if self._is_shuffled:
            raise RuntimeError(DECK_ALREADY_SHUFFLED)
        self._shuffle()

    def get_top(self):
        self._reshuffle_if_need()

        return self._cards[self._cardStack.pop()]

    def _reshuffle_if_need(self):
        if not self._is_shuffled:
            raise RuntimeError(DECK_NOT_SHUFFLED)
        if self.size == 0:
            if self._reusable:
                self._shuffle()
            else:
                raise RuntimeError(DECK_NOT_REUSABLE)

    def _shuffle(self):
        self._cardStack = list(self._cards.keys())
        random.shuffle(self._cardStack)
        self._is_shuffled = True


