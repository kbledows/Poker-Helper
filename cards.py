# cards

class Card(object):
    card_values = {
        'A': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def __init__(self, value, suit):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.value = value
        self.suit = suit
        self.points = self.card_values[value]

    def setValue(self, value):
        self.value = value

    def setSuit(self, suit):
        self.suit = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getPoints(self):
        return self.points

    def printCard(self):
        print("This card is a(n) %s of %s", self.value, self.suit)
