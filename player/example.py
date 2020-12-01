from loader import loader
from model.enums.testType import TestType
from model.enums.cardBackType import CardBackType
from model.enums.location import Location

# load a set of decks
deck_set = loader.load_decks()

# shuffle decks before a game
deck_set.shuffle()

# get specific contact for test
contact = deck_set.get_deck(CardBackType.COMMON)._cards.get('1').get_contact(Location.CITY)

# get next 'Common' contact in location 'Sea'
next_sea_contact = deck_set.get_next_contact(CardBackType.COMMON, Location.SEA)

# get next 'Other world" contact
next_other_world_contact = deck_set.get_next_contact(CardBackType.OTHER_WORLD)

# get a next location of expedition contact (a card with contacts will not be taken here)
# this feature needs for moving a expedition marker on the map
next_expedition_location = deck_set.get_next_expedition_location()
print(next_expedition_location)




