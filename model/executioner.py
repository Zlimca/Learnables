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


def build_decks(deck: list) -> list:
    deck_objects = []
    for deck in deck:
        deck_objects.append(Deck(deck[0], deck[1], deck[2], deck[3]))

    return deck_objects


def build_card(card: tuple) -> Card:
    return Card(card[0], card[1], card[2], card[3], card[4])
