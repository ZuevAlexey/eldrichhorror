class Deck(object):
    def __init__(self, cardBackType):
        super().__init__()
        self.cardBackType = cardBackType
        self.cards = []

    def add(self, card):
        self.cards.append(card)
