from deck import Deck
import copy
import random
from prettytable import PrettyTable, MARKDOWN


class Builder:
    def __init__(self,
                 starting_deck: dict,
                 rejected: list = [],
                 team_size: int = 5,
                 balance_range: int = 1):
        self.team_size = team_size
        self.starting_deck = Deck(starting_deck, rejected, team_size)
        self.current_deck = dict()
        self.balance_range = balance_range

    def get_deck_value(self) -> int:
        return self.current_deck.output_value

    def print_deck_cards(self) -> list:

        unique_cards = list(set(self.current_deck.output_deck))
        all_cards = self.current_deck.output_deck

        table = PrettyTable()

        data = []
        for card in unique_cards:
            value = self.starting_deck.available_cards[card]['value']
            row = [
                card, '{0:{1}}'.format(value, '+' if value else ''),
                all_cards.count(card)
            ]
            data.append(row)

        table.field_names = ['Card', 'Value', 'Quantity']
        table.align['Card'] = 'l'
        table.sortby = 'Quantity'
        table.reversesort = True
        table.set_style(MARKDOWN)
        table.add_rows(data)

        print(table)

    def add_random_card(self):
        card = random.choice(list(self.current_deck.available_cards.keys()))
        self.current_deck.add_card(card)

    def is_valid(self) -> bool:
        valid = True
        if not abs(self.current_deck.output_value) <= self.balance_range:
            valid = False

        if self.current_deck.output_deck.count('Mason') == 1:
            valid = False

        return valid

    def find_playeable_deck(self):
        accepted = False
        while not accepted:
            self.current_deck = copy.deepcopy(self.starting_deck)
            for i in range(self.team_size -
                           len(self.current_deck.output_deck)):

                mason_check = self.current_deck.check_masons()
                if mason_check:
                    # We just added our second mason
                    continue

                self.add_random_card()

            accepted = self.is_valid()