from suit import Suit
from face import Face
from card import card
import random
class deck:
    __inner_deck = []

    #build a new deck
    def __init__(self):
        #fill the deck with all the possible cards
        for suit in Suit:
            for face in Face:
                self.__inner_deck.append(card(suit,face))
        #shuffle the deck
        random.shuffle(self.__inner_deck)

    #draw the last item from the deck
    def draw(self):
        return self.__inner_deck.pop()
    