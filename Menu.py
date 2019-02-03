from KingsCup import KingsCup
import sys


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.game = KingsCup()


    def display_menu(self):
        print(
            """
Main Menu

1. Start Game
2. Quit            
"""
        )


    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter an option: "))
            if choice == 1:
                self.game.run()
            elif choice == 2:
                sys.exit(0)
            else:
                print(f"{choice} is not a valid choice.")
