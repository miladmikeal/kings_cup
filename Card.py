import sys
from termcolor import cprint

class Card:
	"""Represent a single card in a deck. Value and suite can be returned."""

	def __init__(self, value, suite):
		"""Initialize the value and suite of the card."""
		self.value = value
		self.suite = suite

	def print_card(self):
		"""Display the card with unicode and formatting."""
		color = ""
		suit = ""
		if self.suite == "Diamonds":
			suit = str(u'\u2666')
			color = "red"

		elif self.suite == "Hearts":
			suit = str(u'\u2665')
			color = "red"

		elif self.suite == "Spades":
			suit = str(u'\u2660')

		elif self.suite == "Clubs":
			suit = str(u'\u2663')

		if color == "red":
			cprint('┌───────┐', color, file=sys.stderr)
			cprint(f'| {self.value[0]:<2}    |', color, attrs=['bold'], file=sys.stderr)
			cprint('|       |', color, file=sys.stderr)
			cprint(f'|   {suit}   |', color, attrs=['bold'], file=sys.stderr)
			cprint('|       |', color, file=sys.stderr)
			cprint(f'|    {self.value[0]:>2} |', color, attrs=['bold'], file=sys.stderr)
			cprint('└───────┘', color, file=sys.stderr)
		else:
			print('┌───────┐')
			print(f'| {self.value[0]:<2}    |')
			print('|       |')
			print(f'|   {suit}   |')
			print('|       |')
			print(f'|    {self.value[0]:>2} |')
			print('└───────┘')


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