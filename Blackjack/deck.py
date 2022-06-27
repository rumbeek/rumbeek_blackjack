import random
from parameters import *


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit in ('club', 'diamond', 'heart', 'spade'):
            for rank in RANKS:
                self.cards.append({'suit': suit, 'rank': rank})

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(random.randrange(len(self.cards)))


class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.output = []
        self.value = 0

    def get_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        self.value = 0
        for card in self.cards:
            if card['rank'] in 'JQK':
                self.value += 10
            elif card['rank'] == 'A':
                if self.value <= 10:
                    self.value += 11
                elif self.value > 10:
                    self.value += 1
            else:
                self.value += int(card['rank'])

    def display_cards(self):
        for card_index, card in enumerate(self.cards):
            self.output.append(card['rank'] + card['suit'])
            return self.output
    

class Points:
    def __init__(self):
        self.point = 0
