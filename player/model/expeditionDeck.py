from model.deck import Deck


class ExpeditionDeck(Deck):
    def __init__(self, cardBackType):
        super().__init__(cardBackType)

    def get_next_location(self):
        self._reshuffle_if_need()

        next_card_id = self._cardStack[len(self._cardStack) - 1]
        next_card = self._cards[next_card_id]
        return next_card.location
