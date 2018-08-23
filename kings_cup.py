import random

class Participant:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		self.cards = []
	def drawCard(self):
		self.cards += deck.pop()
	def showCards(self):
		print(self.name) 
		print(self.cards)
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


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

deck = []
participants = []

def shuffleDeck():
	for suite in ["Clubs", "Diamonds", "Hearts", "Spades"]:
		for num in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
			deck.append(Card(num, suite))
			random.shuffle(deck)
	return deck 


players = input("Enter the number of players: ")
numPlayers = int(players)
if numPlayers < 3:
	print(players)
	print("Not enough players.")
elif numPlayers > 12:
	print(players)
	print("That's too many players.")
else:
	for player in range(numPlayers):
		player += 1
		name = input("Player %s's Name: " %player) 
		gender = input("Player %s's Gender: " %player)
		participants.append(Participant(name, gender))

deck = shuffleDeck()

print(deck)
print(participants)