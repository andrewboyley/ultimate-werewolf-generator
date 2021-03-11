from deck_builder import Builder
import json

starting_deck = json.load(open('ultimate_werewolf.json'))

team_size = int(input('Enter team size: '))

rejected = ['Vampire']

if not 5 <= team_size:
    print('Teams need to be between 5 and 22')
    exit()

deck_builder = Builder(starting_deck=starting_deck,
                       rejected=rejected,
                       team_size=team_size,
                       balance_range=0)
deck_builder.find_playeable_deck()

print()
deck_builder.print_deck_cards()
print()
print(f'Deck Balance: {deck_builder.get_deck_value()}')