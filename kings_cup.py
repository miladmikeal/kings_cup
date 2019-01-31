import random


# Empty participants list
participants = []


class Participant:
	"""Represent a participant in the game. Participants can
	draw cards, and show cards."""

	def __init__(self, name):
		"""Initializes the participants name and cards."""
		self.name = name
		self.cards = []

	def draw_card(self):
		"""Returns a card from the deck and displays the card."""
		card = deck.get_deck().pop()
		self.cards.append(card)
		print("{0} drew a {1}".format(self.name, self.cards[-1]))
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




# Get number of players
players = input("Enter the number of players: ")
# Convert to integer
numPlayers = int(players)

# If num players less than 3
if numPlayers < 3:
	print(players)
	print("Not enough players.")
# If num players more than 12
elif numPlayers > 12:
	print(players)
	print("That's too many players.")
else:
	# Loop through number of players
	for player in range(numPlayers):
		player += 1
		# Input name $ gender for each player
		name = input("Player %s's Name: " %player)
		# Add participant to participants list
		participants.append(Participant(name))

# Initialize and shuffle deck
deck = Deck()
deck.shuffle_deck()

print("\n")
print("\n")

i = 0
numKings = 0
# Loop until deck is empty
while len(deck.get_deck()) != 0 and numKings != 4:
	input("Press Enter to continue...")
	# Call drawCard method for players continuously
	card = participants[i % numPlayers].draw_card()
	# Pour into kings cup if card is king
	if card.get_value() is "King":
		print("Pour into the Kings Cup!")
		numKings += 1
	# If 4th King drawn, player must drink Kings Cup
	if numKings == 4:
		print("{0}, DRINK THE KINGS CUP!".format(participants[i % numPlayers].get_name()))

	i += 1
	print("\n")

# Show everyone's cards at the end
for j in range(numPlayers):
	participants[j].show_cards()

