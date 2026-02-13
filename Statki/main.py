from tkinter import *
from tkinter import ttk

from GameGUI import GameGUI
from StartGUI import StartGUI


def game():
    root = Tk()
    init_info = StartGUI(root)
    root.mainloop()
    if init_info.isok_text.get() != "OK":
        print("Game canceled")
        return 0
    else:
        players = init_info.players
        Player = players[0]

    while True:
        result = 0
        while result == 0:
            if len(players) == 1:
                print("You won!")
                return 0
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
