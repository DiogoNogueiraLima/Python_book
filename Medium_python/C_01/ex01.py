import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    c = [1]
    
    def __init__(self):
        self._cards = []
        self.n = 'a'
        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(rank, suit))


    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __str__(self) -> str:
        return str(self.n)
    
    def __gardison(self):
        print(self)

def gard(obj):
    obj.__gardison()


beer_card = Card('7', 'diamonds')
beer_card
deck = FrenchDeck()
gard(deck)
deck.__gardison()
deck_1 = FrenchDeck()
print(f'deck.c = {deck.c}')
print(f'deck_1.c = {deck_1.c}')
#deck.c.append(4)
deck.c = [7,8]
FrenchDeck.c = [11]
print(f'deck.c = {deck.c}')
print(f'deck_1.c = {deck_1.c}')
len(deck)
deck[1]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high): 
    print(card)
