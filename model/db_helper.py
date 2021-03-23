import sqlite3


class DBHelper:
    def __init__(self, path: str):
        # self._path = path
        self._name = "learnables.db"
        # self._full_path = self._path + "/" + self._name
        self._connection = sqlite3.connect(self._name)
        self._cursor = self._connection.cursor()

        self.create_db()

    def reestablish_connection(self):
        self._connection.close()
        self._connection = sqlite3.connect(self._name)
        self._cursor = self._connection.cursor()

    def create_db(self):
        create_cards = """
                    CREATE TABLE IF NOT EXISTS cards
                        (C_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                        Front TEXT,
                        Back TEXT,
                        Counter_C INTEGER DEFAULT 0,
                        Counter_F INTEGER DEFAULT 0);
                    """

        create_decks = """
                    CREATE TABLE IF NOT EXISTS decks
                        (D_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                        Name TEXT NOT NULL,
                        S_ID INTEGER NOT NULL,
                        FOREIGN KEY (S_ID)
                            REFERENCES subjects (S_ID));
                        """

        create_subjects = """
                    CREATE TABLE IF NOT EXISTS subjects
                        (S_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                        subject TEXT NOT NULL UNIQUE);
                            """

        create_deck_lookup = """
                            CREATE TABLE IF NOT EXISTS deck_lookup
                            (Pare_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                            D_ID INTEGER NOT NULL,
                            C_ID INTEGER NOT NULL,
                            FOREIGN KEY (D_ID)
                                REFERENCES decks (D_ID)
                            FOREIGN KEY (C_ID)
                                REFERENCES cards (C_ID));
                            """

        self._cursor.execute(create_cards)
        self._cursor.execute(create_decks)
        self._cursor.execute(create_subjects)
        self._cursor.execute(create_deck_lookup)

    def get_cards(self):
        return list(self._cursor.execute("SELECT * FROM cards;"))

    def get_card_by_id(self, c_id: int):
        val = list(self._cursor.execute(f"SELECT * FROM cards WHERE C_ID == {c_id}"))[0]
        return val

    def get_card(self, front: str, back: str):
        query = f"SELECT * FROM cards WHERE (Front == '{front}') and (Back == '{back}')"
        val = self._cursor.execute(query).fetchall()[0]
        return val

    def get_decks(self):
        decks = self._cursor.execute("SELECT * FROM decks;").fetchall()
        decks_connections = self._cursor.execute("SELECT * FROM deck_lookup").fetchall()
        #print(decks, "\n")
        #print(decks_connections)

        return decks, decks_connections

    def _get_deck_id(self, name: str):
        return list(self._cursor.execute(f"SELECT id FROM decks WHERE Name == '{name}'"))[0]

    def get_subjects(self):
        return list(self._cursor.execute("SELECT * FROM subjects;"))

    def get_subject(self, subject: str = None, s_id: str = None):
        if subject is None:
            return list(self._cursor.execute(f"SELECT Language from languages WHERE S_ID == {s_id}"))

        elif s_id is None:
            return list(self._cursor.execute(f"SELECT Language from languages WHERE Subject == '{subject}'"))

        else:
            raise AttributeError

    def create_card(self, front: str, back: str) -> tuple:
        query = f"INSERT INTO cards (Front, Back) VALUES ('{front}', '{back}');"
        #print(query)
        self._cursor.execute(query)
        self._connection.commit()

        return self.get_card_by_id(self.get_card(front, back)[0])

    def create_deck(self, name: str, subject: str, cards: list):
        ids = [card.c_id for card in cards]

        query = f"""
                INSERT INTO decks (Name, S_ID)
                VALUES ('{name}', '{self.get_subject(subject=subject)}';
                """

        self._cursor.execute(query)

        for c_id in ids:
            self._cursor.execute(f"INSERT INTO deck_lookup (D_ID, C_ID VALUES ('{self._get_deck_id(name)}', '{c_id}'")

        self._connection.commit()

    def close_connection(self):
        self._connection.commit()
        self._connection.close()

    def create_dummy_data(self):
        test1 = self.get_subjects()
        test2 = self.get_cards()
        test3 = self.get_decks()
        test4 = self._cursor.execute("SELECT * FROM deck_lookup").fetchall()

        if len(test1) != 0 and len(test2) != 0 and len(test3) != 0 and len(test4) != 0:
            return

        dummy_subjects = """
                INSERT INTO subjects (subject)
                VALUES
                    ("Mathe"),
                    ("InfT"),
                    ("Deutsch"),
                    ("Politik"),
                    ("Informatik");
                """

        dummy_cards = """
                INSERT INTO cards (Front, Back)
                VALUES
                    ("Front1", "Back1"),
                    ("Front2", "Back2"),
                    ("Front3", "Back3"),
                    ("Front4", "Back4"),
                    ("Front5", "Back5"),
                    ("Front6", "Back6");
                """

        dummy_decks = """
                    INSERT INTO decks (Name, S_ID)
                    VALUES 
                        ('deck1', 1),
                        ('deck2', 2),
                        ('deck3', 3),
                        ('deck4', 4),
                        ('deck5', 5);
                    """

        dummy_deck_lookup = """
                            INSERT INTO deck_lookup (D_ID, C_ID)
                            VALUES 
                                (1, 1),
                                (1, 2),
                                (1, 3);
                            """

        self._cursor.execute(dummy_subjects)
        self._cursor.execute(dummy_cards)
        self._cursor.execute(dummy_decks)
        self._cursor.execute(dummy_deck_lookup)

        if len(self.get_subjects()) != 0 and len(self.get_cards()) != 0:
            self._connection.commit()
            return True
        else:
            return False

# dbh = DBHelper(r"C:\Users\joshu\Desktop\Learnables")
# dbh.create_dummy_data()
