from singleton.singleton import Singleton
from model import db_helper, executioner
from model.parts import Card


#@Singleton
class Controller(Singleton):
    def __init__(self):
        super().__init__(self)
        self.dbh = db_helper.DBHelper(r".\Learnables")
        self.dbh.create_dummy_data()

    def on_startup(self):
        self.subjects: list = executioner.build_subjects(self.dbh.get_subjects())
        self.cards: list = executioner.build_cards(self.dbh.get_cards())
        self.decks: list = executioner.build_decks(self.dbh.get_decks())

    def get_cards(self) -> list:
        return self.cards

    def get_decks(self) -> list:
        return self.decks

    def get_subjects(self) -> list:
        return self.subjects

    # TODO: crashed wenn eine neue karte hinzugefügt wird! kommt vermutlich aus dbh
    def add_card(self, front: str, back: str) -> Card:
        new_card: tuple = self.dbh.create_card(front, back)
        new_card_object: Card = executioner.build_card(new_card)
        self.cards.append(new_card_object)

        return new_card_object
