class Deck(object):
    def __init__(self, cardBackType):
        super().__init__()
        self.cardBackType = cardBackType
        self.cards = []
        self.remainedCards = []

    def add(self, card):
        self.cards.append(card)
        self.remainedCards.append(card.id)

    @property
    def capacity(self):
        return len(self.cards)

    @property
    def size(self):
        return len(self.remainedCards)
