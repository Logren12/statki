from Captain import Captain
from Ship import Ship
import state
import os

while True:
  os.system('clear')
  Players_Galleon = Ship("Galleon")
  Player = Captain("Player_name", "French", 4,1,2, Players_Galleon)

  Johns_Frigate = Ship("Frigate")
  JohnAI = Captain("JohnAI", "British", 3,3,3, Johns_Frigate)

  # 1. Can search
  search = Player.search()
  # If succedeed can attack:
  if search:
    decision = Player.attack_decision(JohnAI)
    if decision:
      state.battle(Player, JohnAI)
