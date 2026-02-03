import os
import time
from tkinter import *
from tkinter import ttk

import state
from battle_gui import Battle_GUI
from gui import startGUI

# console:
# os.system("clear")
# players = state.game_init(console=True)
# os.system("clear")

# gui:
root = Tk()
a = startGUI(root)
root.mainloop()
players = state.game_init(a.name.get(), a.nationality.get(), a.ship.get())

print("Players:")
for player in players:
    print(player)
Player = players[0]


def game():
    while True:
        search = Player.search()
        if not search:
            print("No ships found!")
            return 0
        print("Ship found!\n")
        decision = Player.attack_decision(players[1])
        if decision:
            root = Tk()
            Battle_GUI(root, Player, players[1])
            result = state.battle(Player, players[1])
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


while True:
    game()
