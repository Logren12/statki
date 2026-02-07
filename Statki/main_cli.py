import os

import game_utils


def game():
    while True:
        result = game_utils.battle(Player, players[1])
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


os.system("clear")
Player = game_utils.player_setup(True)
players = game_utils.game_init(Player)
os.system("clear")
print("Players:")
for player in players:
    print(player)
Player = players[0]

game()
