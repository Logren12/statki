from tkinter import *
from tkinter import ttk

from statki.game_gui import GameGUI
from statki.start_gui import StartGUI


def game():
    root = Tk()
    player_information = StartGUI(root)
    root.mainloop()
    if player_information.isok_text.get() != "OK":
        print("Game canceled")
        return 0
    else:
        players = player_information.players
        Player = players[0]

    while True:
        result = 0
        while result == 0:
            if len(players) == 1:
                print("Congratulations! You won!")
                return 0
            print("Starting new battle!")
            root = Tk()
            round = GameGUI(root, Player, players[1])
            root.mainloop()
            result = round.result.get()
        if result == 1:  # enemy defeated
            print(f"{Player.name} destroyed {players[1].name}'s ship!")
            players.remove(players[1])
            Player.ship.full_repair()
        elif result == 2:  # player defeated
            print(f"{players[1].name} destroyed Your ship! Game over!")
            return 0
        elif result == 3:  # player escaped
            Player.ship.full_repair()
        elif result == 4:  # player and enemy destroyed each other
            print("Both captains sunk! Game over!")
            return 0


if __name__ == "__main__":
    game()
