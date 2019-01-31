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