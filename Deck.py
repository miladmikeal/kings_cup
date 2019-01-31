import random
from Card import Card

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


