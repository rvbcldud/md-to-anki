import os
import sys
import genanki
import re
from random import randrange

def create_model(model_num=0):
    # TODO in the future, have this be defined by the user with a system
    # argument
    # 0 -> Basic model
    # 1 -> Basic and reversed model
    # 2 -> Basic and optional reverse model
    # 3 -> Basic type in answer model
    # 4 -> Cloze model
    
    if model_num == 0:
        return genanki.BASIC_MODEL
    elif model_num == 1:
        return genanki.BASIC_AND_REVERSED_CARD_MODEL
    elif model_num == 2:
        return genanki.BASIC_OPTIONAL_REVERSED_CARD_MODEL
    elif model_num == 3:
        return genanki.BASIC_TYPE_IN_THE_ANSWER_MODEL
    elif model_num == 4:
        return genanki.CLOZE_MODEL

def create_deck(deck_title):
    deck_id = randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(
        deck_id,
        deck_title)

    return my_deck


def search_markdown(text):
    # Opens file in order to use a regular expression throughout it
    with open(text, 'r') as f:
        md_text = f.read()
        # Finds all card questions and answers
        card_list = re.findall('\## (.*)\n\n(.*(?:\r?\n(?!\r?\n).*)*)', md_text)
        # Finds the title
        deck_title = re.findall('(?<=# )(.*)', md_text)

        # TODO In the future, make the regex statement only match with headers
        # with one '#'
        # Removes all matches that are in the deck_title list that are also in
        # the card_list
        for i in card_list:
            for j in i:
                if j in deck_title:
                    deck_title.remove(j)

    return card_list, deck_title

def add_cards(cards, model, deck):
    for i in cards:
        note_question = i[0]
        note_answer = i[1].replace('\n', '<br>')
        note = genanki.Note(
            model=model,
            fields=[note_question, note_answer])
        deck.add_note(note)


def export_deck(file_name, pkg_name):

    cards, title = search_markdown(file_name)
    deck = create_deck(title[0])
    add_cards(cards, create_model(), deck)
    genanki.Package(deck).write_to_file(pkg_name)
