from singleton.singleton import Singleton
from model import db_helper, executioner


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
        return self.subjects

    def get_decks(self) -> list:
        return self.decks

    def get_subjects(self) -> list:
        return self.subjects
