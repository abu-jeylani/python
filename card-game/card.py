values = {'Two':2, 'Three': 3, 'Four':4, 'Five':5, 
          'Six': 6, 'Seven':7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Eleven':11,
          'Twelve': 12, 'Thirteen':13, 'Fourteen':14
           }


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) :
        return f"{self.rank} of {self.suit}"

two_hearts = Card("Hearts", "Two")

print(two_hearts)

print(two_hearts.suit)


print(values[two_hearts.rank])