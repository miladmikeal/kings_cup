from Deck import Deck
from Participant import Participant


class KingsCup:
    """Represents the game of Kings Cup. Gets user input and runs the game."""

    def __init__(self):
        self.participants = []
        self.numPlayers = 0
        self.name = "Game of Kings Cup"
        self.get_inputs()

    def get_inputs(self):
        """Gets user input for number of players and names of players."""

        players = input("Enter the number of players: ")

        self.numPlayers = int(players)

        # If num players less than 3
        if self.numPlayers < 3:
            print(players)
            print("Not enough players.")

        # If num players more than 12
        elif self.numPlayers > 12:
            print(players)
            print("That's too many players.")

        else:
            # Loop through number of players
            for player in range(self.numPlayers):
                player += 1
                # Input name $ gender for each player
                name = input("Player %s's Name: " % player)
                # Add participant to participants list
                self.participants.append(Participant(name))


    def run(self):
        """Runs the game."""
        deck = Deck()

        deck.shuffle_deck()

        print()
        print()

        i = 0
        numKings = 0

        # Loop until deck is empty
        while len(deck.get_deck()) != 0 and numKings != 4:
            input("Press Enter to continue...")

            # Call drawCard method for players continuously
            card = self.participants[i % self.numPlayers].draw_card(deck)
            # Pour into kings cup if card is king

            if card.get_value() is "King":
                print("Pour into the Kings Cup!")
                numKings += 1

            # If 4th King drawn, player must drink Kings Cup
            if numKings == 4:
                print("{0}, DRINK THE KINGS CUP!".format(self.participants[i % self.numPlayers].get_name()))

            i += 1
            print()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name