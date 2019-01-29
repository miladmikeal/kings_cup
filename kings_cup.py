import random

# Empty deck list
deck = []
# Empty participants list
participants = []

# Participant class implemenation
class Participant:
	def __init__(self, name):
		self.name = name
		self.cards = []
	def drawCard(self):
		card = deck.pop()
		self.cards.append(card)
		print("{0} drew a {1}".format(self.name, self.cards[-1]))
		return card
	def getName(self):
		return self.name
	def showCards(self):
		print(self.name)
		print(self.cards)
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


# Card class implemenation
class Card:
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite
	def getValue(self):
		return self.value
	def getSuite(self):
		return self.suite
	def __str__(self):
		return ("{0} of {1}".format(self.value, self.suite))
	def __repr__(self):
		return ("{0} of {1}".format(self.value, self.suite))



# Function to shuffle deck
def shuffleDeck():
	# Loop through suits
	for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
		# Loop through values
		for num in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
			# Add Card to deck
			deck.append(Card(num, suit))
			# Shuffle deck
			random.shuffle(deck)
	return deck


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

shuffleDeck()

print("\n")
print("\n")

i = 0
numKings = 0
# Loop until deck is empty
while len(deck) != 0 and numKings != 4:
	input("Press Enter to continue...")
	# Call drawCard method for players continuously
	card = participants[i % numPlayers].drawCard()
	# Pour into kings cup if card is king
	if card.getValue() is "King":
		print("Pour into the Kings Cup!")
		numKings += 1
	# If 4th King drawn, player must drink Kings Cup
	if numKings == 4:
		print("{0}, DRINK THE KINGS CUP!".format(participants[i % numPlayers].getName()))

	i += 1
	print("\n")

# Show everyone's cards at the end
for j in range(numPlayers):
	participants[j].showCards()

