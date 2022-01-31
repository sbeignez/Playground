from agent import Player
from random import shuffle
from enum import Enum


class Cluedo():

    def __init__(self):
        self.players = None
        self.card_who = None
        self.card_where = None
        self.card_what = None

    def add_player(self):
        self.players.appends(Player())

    def deal_cards(self):
        pass

    


    def start(self):

        n_players = int(input("Number of players: ", ))
        if not n_players:
            n_players = 4

        deck = DeckOfCards()

        card_who, card_what, card_where, hands = deck.deal(n_players)

        print(hands[0])

        game_on = True

        while game_on:
            pass



class CardCategory(Enum):
    WHERE = 1
    WHO = 2
    WHAT = 3

class Card:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def __repr__(self):
        return f"[{self.name}]"
    

class DeckOfCards:
    def __init__(self):
        cards_who = [
            ("Miss Scarlett", CardCategory.WHO),
            ("Rev Green", CardCategory.WHO),
            ("Colonel Mustard", CardCategory.WHO),
            ("Professor Plum", CardCategory.WHO),
            ("Mrs. Peacock", CardCategory.WHO),
            ("Dr. Orchid", CardCategory.WHO),
            ]
        cards_what = [
            ("Candlestick", CardCategory.WHAT),
            ("Dagger", CardCategory.WHAT),
            ("Lead Pipe", CardCategory.WHAT),
            ("Revolver", CardCategory.WHAT),
            ("Rope", CardCategory.WHAT),
            ("Wrench", CardCategory.WHAT),
            ]
        cards_where = [
            ("Kitchen", CardCategory.WHERE),
            ("Ballroom", CardCategory.WHERE),
            ("Conservatory", CardCategory.WHERE),
            ("Dining Room", CardCategory.WHERE),
            ("Billiard Room", CardCategory.WHERE),
            ("Library", CardCategory.WHERE),
            ("Hall", CardCategory.WHERE),			
            ("Lounge", CardCategory.WHERE),
	        ("Study", CardCategory.WHERE),
            ]
        self.deck_who = [Card(c[0],c[1]) for c in cards_who]
        self.deck_what = [Card(c[0],c[1]) for c in cards_what]
        self.deck_where = [Card(c[0],c[1]) for c in cards_where]

    def deal(self, n_players):
        shuffle(self.deck_who)
        shuffle(self.deck_what)
        shuffle(self.deck_where)
        deck = self.deck_who[1:] + self.deck_what[1:] + self.deck_where[1:]
        hands = [deck[i::n_players] for i in range(0, n_players)]
        return self.deck_who[0], self.deck_what[0], self.deck_where[0], hands



game = Cluedo()
game.start()

# 6+ 6 + 9 = 18 = 2*2*3*2