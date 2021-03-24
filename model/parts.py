from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Subject:
    def __init__(self, s_id: int, subject: str):
        self.s_id = s_id
        self.subject = subject

    def __repr__(self):
        return self.subject


class Card(QLabel):
    clicked = pyqtSignal()

    def __init__(self, c_id: int, front: str, back: str, counter_r: int = 0, counter_w: int = 0):
        super().__init__(front)

        self.c_id = c_id
        self.is_front = True
        self.front = front
        self.back = back
        self.counter_r = counter_r
        self.counter_w = counter_w

        self.setStyleSheet("background-color: lightgray")
        self.setWordWrap(True)
        self.setContentsMargins(10, 5, 10, 5)

    def __repr__(self):
        return f"id: {self.c_id} \nfront: {self.front} \nback: {self.back} \nright: {self.counter_r} \nwrong: {self.counter_w}"

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


class Deck(QLabel):
    def __init__(self, d_id: int, name: str, subject: Subject, cards: list):
        super().__init__(f"{name}; {subject.subject}")

        self.d_id = d_id
        self.name = name
        self.subject = subject
        self.cards = cards

        self.setFixedWidth(425)
        self.setStyleSheet("background-color: lightgray")
        self.setWordWrap(True)
        self.setContentsMargins(10, 5, 10, 5)

    def __repr__(self):
        return self.name

    def get_card(self, c_id):
        for card in self.cards:
            if card.c_id == c_id:
                return card
        else:
            return None


class DeckRadioButton(QRadioButton):
    def __init__(self, text, deck: Deck):
        super().__init__(text)

        self.deck = deck
