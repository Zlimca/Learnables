from model.parts import *


def build_cards(cards: list) -> list:
    card_objects = []
    for card in cards:
        card_objects.append(Card(card[0], card[1], card[2], card[3], card[4]))

    return card_objects


def build_subjects(subjects: list) -> list:
    subject_objects = []
    for subject in subjects:
        subject_objects.append(Subject(subject[0], subject[1]))

    return subject_objects


def build_decks(decks: list, decks_lookup: list, cards: list) -> list:
    deck_objects = []
    for deck in decks:
        lookups = []

        for lookup in decks_lookup:
            for card in cards:
                if card.c_id == lookup[2]:
                    lookups.append(card)

        deck_objects.append(Deck(deck[0], deck[1], deck[2], lookups))

    return deck_objects


def build_card(card: tuple) -> Card:
    return Card(card[0], card[1], card[2], card[3], card[4])
