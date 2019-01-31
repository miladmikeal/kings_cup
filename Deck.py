import random

class Deck:
	"""Represent a standard deck of cards, A-King, with all 4 suites.
	Deck can be shuffled and returned."""

	def __init__(self):
		"""Initializes an array of cards."""
		self.deck = []
		# Loop through suits
		for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
			# Loop through values
			for num in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
				# Add Card to deck
				self.deck.append(Card(num, suit))

	def shuffle_deck(self):
		"""Shuffles the deck of cards."""
		random.shuffle(self.deck)
		return self.deck

	def get_deck(self):
		"""Returns the deck of cards."""
		return self.deck


class Card:
	"""Represent a single card in a deck. Value and suite can be returned."""

	def __init__(self, value, suite):
		"""Initializes the value and suite of the card."""
		self.value = value
		self.suite = suite

	def get_value(self):
		"""Returns the value of the card."""
		return self.value

	def get_suite(self):
		"""Returns the suite of the card."""
		return self.suite

	def __str__(self):
		return ("{0} of {1}".format(self.value, self.suite))

	def __repr__(self):
		return ("{0} of {1}".format(self.value, self.suite))