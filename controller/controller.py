from singleton.singleton import Singleton
from model import db_helper, executioner
from model.parts import Card
import os


# @Singleton
class Controller(Singleton):
    def __init__(self):
        super().__init__(self)
        self.dbh = db_helper.DBHelper(r".\Learnables")
        self.dbh.create_dummy_data()
        self.selected_deck = None

    def on_startup(self):
        self.subjects: list = executioner.build_subjects(self.dbh.get_subjects())
        self.cards: list = executioner.build_cards(self.dbh.get_cards())
        decks, decks_lookup = self.dbh.get_decks()
        self.decks: list = executioner.build_decks(decks, decks_lookup, self.cards)

    def get_cards(self) -> list:
        return self.cards

    def get_decks(self):
        return self.decks

    def get_subjects(self) -> list:
        return self.subjects

    # FIXED by adding a reconnect function to the dbh
    def add_card(self, front: str, back: str) -> Card:
        self.dbh.reestablish_connection()

        new_card: tuple = self.dbh.create_card(front, back)
        new_card_object: Card = executioner.build_card(new_card)
        self.cards.append(new_card_object)

        return new_card_object

    def add_deck(self, card: Card):
        self.dbh.reestablish_connection()
        pass
