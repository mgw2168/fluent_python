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
print(beer_card)

deck = FrenchDeck()

# 如果一个集合类型没有实现__contains__方法，那么in运算符就会按顺序做一次迭代搜索
# FrenchDeck是可迭代的
print(Card('Q', "hearts") in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

print(spades_high(card))
