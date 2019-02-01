import sys
from termcolor import cprint
from art import *

class Card:
	"""Represent a single card in a deck. Value and suite can be returned."""

	def __init__(self, value, suite):
		"""Initializes the value and suite of the card."""
		self.value = value
		self.suite = suite

	def display_card_art(self):
		"""Displays the card with ASCII art and changes color if necessary."""
		Art = ""
		color = ""

		if self.value == "Ace":
			Art = text2art("A", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "2":
			Art = text2art("2", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "3":
			Art = text2art("3", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "4":
			Art = text2art("4", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "5":
			Art = text2art("5", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "6":
			Art = text2art("6", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "7":
			Art = text2art("7", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "8":
			Art = text2art("8", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "9":
			Art = text2art("9", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "10":
			Art = text2art("T", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "Jack":
			Art = text2art("J", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "Queen":
			Art = text2art("Q", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"

		elif self.value == "King":
			Art = text2art("K", font='block', chr_ignore=True)
			if self.suite == "Diamonds" or self.suite == "Hearts":
				color = "red"


		if color == "red":
			cprint(Art, color, attrs=['bold'], file=sys.stderr)
		else:
			print(Art)


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