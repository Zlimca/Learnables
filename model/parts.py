from PyQt5.QtWidgets import QLabel


class Subject:
    def __init__(self, s_id: int, subject: str):
        self.s_id = s_id
        self.subject = subject

    def __repr__(self):
        return self.subject


class Card(QLabel):
    def __init__(self, c_id: int, front: str, back: str, counter_r: int = 0, counter_w: int = 0):
        super().__init__()
        self.c_id = c_id
        self._is_front = True
        self.front = front
        self.back = back
        self.counter_r = counter_r
        self.counter_w = counter_w

    def __repr__(self):
        return f"id: {self.c_id} \nfront: {self.front} \nback: {self.back}"

    def swap_text(self):
        if self._is_front:
            self.setText(self.back)
        else:
            self.setText(self.front)


class Deck:
    def __init__(self, d_id: int, name: str, subject: Subject, cards: list):
        self.d_id = d_id
        self.name = name
        self.subject = subject
        self.cards = cards

    def __repr__(self):
        return self.name

    def get_card(self, c_id):
        for card in self.cards:
            if card.c_id == c_id:
                return card
        else:
            return None
