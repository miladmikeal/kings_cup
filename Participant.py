from Card import Card

class Participant:
	"""Represent a participant in the game. Participants can
	draw cards, and show cards."""

	def __init__(self, name):
		"""Initializes the participants name and cards."""
		self.name = name
		self.cards = []


	def draw_card(self, deck):
		"""Returns a card from the deck and displays the card."""
		card = deck.get_deck().pop()
		self.cards.append(card)
		print("{0} drew a {1}".format(self.name, card))
		card.display_card_art()
		return card


	def get_name(self):
		"""Returns the name of the participant."""
		return self.name

	def show_cards(self):
		"""Shows the cards of the participant."""
		print(self.name)
		print(self.cards)

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

