import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint, shuffle
from deck import deck

class hand(QWidget):
    __inner_hand = []

    def __init__(self,deck):
        #set up widget
        super().__init__()
        self.__shapes = list()
        self.setGeometry(50, 50, 1000, 750)
        self.setWindowTitle('GrandmasGin')
        self.show()
        #draw 10 cards from the deck into your inner hand
        i=0
        while(i<10):
            self.__inner_hand.append(deck.draw())
            i+=1
        
    def get_hand(self):
        return self.__inner_hand

if __name__ == '__main__':
  app = QApplication(sys.argv)
  t_deck = deck()
  ex = hand(t_deck)
  sys.exit(app.exec_())