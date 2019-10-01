from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

# python3中隐式的继承了object
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


beer_card = Card('7', 'diamonds')
print(beer_card.suit)
print(beer_card.rank)
print(beer_card)

deck = FrenchDeck()
print(deck)

print(deck[:3])