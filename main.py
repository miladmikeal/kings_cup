from Deck import Deck
from Participant import Participant


def main():

	deck = Deck()

	participants = []

	players = input("Enter the number of players: ")

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


	deck.shuffle_deck()

	print()
	print()

	i = 0
	numKings = 0

	# Loop until deck is empty
	while len(deck.get_deck()) != 0 and numKings != 4:
		input("Press Enter to continue...")

		# Call drawCard method for players continuously
		card = participants[i % numPlayers].draw_card(deck)
		# Pour into kings cup if card is king

		if card.get_value() is "King":
			print("Pour into the Kings Cup!")
			numKings += 1

		# If 4th King drawn, player must drink Kings Cup
		if numKings == 4:
			print("{0}, DRINK THE KINGS CUP!".format(participants[i % numPlayers].get_name()))

		i += 1
		print()

	# Show everyone's cards at the end
	for j in range(numPlayers):
		participants[j].show_cards()


if __name__ == '__main__':
	main()