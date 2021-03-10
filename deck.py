import copy
import random


class Deck:
    def __init__(self, starting_deck: dict, rejected=[], size: int = 5):
        self.output_deck = []
        self.output_value = 0
        self.rejected = rejected
        self.team_size = size
        self.available_cards: dict = self.deck_clone(starting_deck)

        self.remove_rejected()
        self.add_werewolves()

    def deck_clone(self, deck):
        return copy.deepcopy(deck)

    def remove_rejected(self):
        for card_name in self.rejected:
            try:
                del self.available_cards[card_name]
            except KeyError:
                continue

    def add_card(self, card_name: str):
        self.output_value += self.available_cards[card_name]['value']
        self.output_deck.append(card_name)

        self.available_cards[card_name]['quantity'] -= 1

        if self.available_cards[card_name]['quantity'] == 0:
            del self.available_cards[card_name]

    def add_werewolves(self):
        number_of_werewolves = self.team_size // 3
        for _ in range(number_of_werewolves):
            self.add_card('Werewolf')

    # Returns whether we added the second mason or not
    def check_masons(self) -> bool:
        if self.output_deck.count('Mason') == 1:
            if not 'Mason' in self.available_cards.keys():
                return False

            self.add_card('Mason')
            return True
