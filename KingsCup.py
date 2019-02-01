from Deck import Deck
from Participant import Participant


class KingsCup:
    """Represents the game of Kings Cup. Gets user input and runs the game."""

    def __init__(self):
        """Initializes variables and calls function to get user inputs."""
        self.participants = []
        self.num_players = 0
        self.name = "Game of Kings Cup"
        self.get_inputs()

    def get_inputs(self):
        """Gets user input for number of players and names of players."""

        players = input("Enter the number of players: ")

        self.num_players = int(players)

        # If num players less than 3
        if self.num_players < 3:
            print(players)
            print("Not enough players. Please enter 3-12.")
            self.get_inputs()

        # If num players more than 12
        elif self.num_players > 12:
            print(players)
            print("That's too many players. Please enter 3-12.")
            self.get_inputs()

        else:
            # Loop through number of players
            for player in range(self.num_players):
                player += 1
                # Input name $ gender for each player
                name = input(f"Player {player}'s Name: ")
                # Add participant to participants list
                self.participants.append(Participant(name))


    def run(self):
        """Runs the game."""
        deck = Deck()

        deck.shuffle_deck()

        print()
        print()

        i = 0
        num_kings = 0

        # Loop until deck is empty
        while len(deck.get_deck()) != 0 and num_kings != 4:
            input("Press Enter to continue...")

            # Call drawCard method for players continuously
            card = self.participants[i % self.num_players].draw_card(deck)
            # Pour into kings cup if card is king

            if card.get_value() is "King":
                print("Pour into the Kings Cup!")
                num_kings += 1

            # If 4th King drawn, player must drink Kings Cup
            if num_kings == 4:
                print(f"{self.participants[i % self.num_players].get_name()}, DRINK THE KINGS CUP!")

            i += 1
            print()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name