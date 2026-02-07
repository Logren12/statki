from tkinter import *
from tkinter import ttk

import game_utils
from GameGUI import GameGUI
from StartGUI import StartGUI


def game():
    root = Tk()
    a = StartGUI(root)
    root.mainloop()
    if a.isok_text.get() != "OK":
        print("Game canceled")
        return 0
    else:
        Player = game_utils.player_setup(
            False, a.name.get(), str(a.nationality.get()), a.ship.get()
        )
    players = game_utils.game_init(Player)
    Player = players[0]

    while True:
        result = 0
        while result == 0:
            print("Staring new battle!")
            root = Tk()
            round = GameGUI(root, Player, players[1])
            root.mainloop()
            result = round.result.get()
        if result == 1:
            print(f"{Player.name} destroyed {players[1].name}'s ship!")
            players.remove(players[1])
            Player.ship.repair()
        elif result == 2:
            print(f"{players[1].name} destroyed Your ship! Game over!")
            return 0
        elif result == 3:
            pass
        elif result == 4:
            print("Both captains sunk! Game over!")
            return 0


game()
