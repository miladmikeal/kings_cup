import random

class Participant(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		self.cards = []
	def show_cards(self):
		print self.name 
		print self.cards 


class Deck(object):
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite
	def getvalue(self):
		return self.value
	def getsuite(self):
		return self.suite
	def __str__(self):
		return ("{0} of {1}".format(self.value, self.suite))

def shuffled_deck():
	deck = []
	for suite in ["Clubs", "Diamonds", "Hearts", "Spades"]:
		for num in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
			deck.append(Deck(num, suite))
	random.shuffle(deck)
	return deck 


players = raw_input("Enter the number of players: ")
players = int(players)
if players < 3:
	print players
	print type(players)
	print "Not enough players."
elif players > 12:
	print players
	print type(players)
	print "That's too many players."
else:
	for i in range(players):
		i = i + 1
		participants = {}
		name = raw_input("Player %s's Name: " %i) 
		gender = raw_input("Player %s's Gender: " %i)
		name_gender = name + gender
		participants.append(name_gender)