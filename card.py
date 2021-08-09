#This file includes the class card which represents each card in the deck
from suit import Suit
from face import Face
class card:
    #the private suit and face attributes
    __suit = Suit
    __face = Face
    #note that the isMeld attribute is marked by the deck
    __isMeld = False
    
    #basic get methods for access to attributes
    def getSuit(self):
        return self.__suit

    def getFace(self):
        return self.__face

    def getScore(self):
        if(self.__face.value<=10):
            return self.__face.value
        else:
            return 10

    def isMeld(self):
        return self.__isMeld
    #accessor method for isMeld
    def setMeld(self,ismeld):
        self.__isMeld= ismeld

    def __init__(self,suit,face):
        #setup using the provided face and suit
        self.__suit = suit
        self.__face = face
