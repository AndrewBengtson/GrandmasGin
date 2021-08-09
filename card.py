#This file includes the class card which represents each card in the deck
from suit import Suit
from face import Face
class card:
    #the private suit and face attributes
    __suit = Suit
    __face = Face
    #note that the isMeld attribute is marked by the deck
    __isMeld = False
    __face_to_value = {}
    
    #basic get methods for access to attributes
    def getSuit(self):
        return self.__suit

    def getFace(self):
        return self.__face

    def getScore(self):
        return self.__face_to_value[self.__face]

    def isMeld(self):
        return self.__isMeld
    #accessor method for isMeld
    def setMeld(self,ismeld):
        self.__isMeld= ismeld

    def __init__(self,suit,face):
        #setup using the provided face and suit
        self.__suit = suit
        self.__face = face

        for possible_face in Face:
            if(possible_face.value<=10):
                self.__face_to_value[possible_face] = possible_face.value
            else:
                self.__face_to_value[possible_face] = 10
