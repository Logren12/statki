import random
from Ship import Ship

class Captain:
  def __init__(self, name, nationality, sailing, leadership, reconnaissance, ship:Ship):
    self.name = name
    self.nationality = nationality
    self.sailing = sailing
    self.reconnaissance = reconnaissance
    self.leadership = leadership
    self.ship = ship
  def __str__(self):
    return (
      f"Captain {self.name}\n"
      f"Nationality: {self.nationality}\n"
      f"Sailing: {self.sailing}\n"
      f"Leadership: {self.leadership}\n"
      f"Reconnaissance: {self.reconnaissance}\n"
      f"Current ship: {self.ship.ship_type}\n"
    )
  def roll(self, dice):
    rolls = []
    for i in range(dice):
      roll = random.randint(1,6)
      rolls.append(roll)

    text = "["
    for roll in rolls:
      if roll in [5,6]:
        text += " ☠️"
      else:
        text += " " + str(roll)
    text += " ]"
    print(text)
    return rolls

  def search(self):
    print("Searching for ships!")
    roll = self.roll(self.reconnaissance)
    if (5 in roll) or (6 in roll):
      print("Ship found!\n")
      return True
    else:
      print("We found nothing!\n")
      return False

  def attack_decision(self, target):
    flag = True
    while flag:
      try:
        decision = int(input(f"You have found a {target.nationality} {target.ship.ship_type}. Do You want to attack it?\n(1 - yes, 2 - no)\n"))
        if decision in [1,2]:
          flag = False
        else:
          print("Wrong input, try again.")
      except ValueError:
        print("Wrong input, try again.")
    if decision == 1:
      return True
    else:
      return False
  # battle interactions:
  def battle_declaration(self):
    flag = True
    while flag:
      try:
        print(f"{self.name} declare intent:")
        decision = int(input(f"  1 - fire canons\n  2 - attempt boarding\n  3 - flee\n"))
        if decision in [1,2,3]:
         flag = False
        else:
          print("Wrong input, try again.")
      except ValueError:
        print("Wrong input, try again.")


    return decision

  def crew_fight(self):
    roll = self.roll(self.leadership)
    damage = 0
    for dice in roll:
      if dice in [5,6] and damage < self.ship.crew:
        damage += 1
    return damage

  def fire_canons(self, number):
    if self.ship.canons >= number:
      return self.roll(number)
    elif ((self.ship.canons < number) and (self.ship.canons != 0)):
      return self.roll(self.ship.canons)
    else:
      print("All canons destroyed!")
      return []

  def receive_damage(self, roll):
    locations = []
    for die in roll:
      if die in [1,2,3,4]:
        locations.append(die)
      elif die == 5 or die == 6:
        flag = True
        while flag:
          try:
            location = int(input(f"\r{self.name}, pick damage location:\n"))
            if location in [1,2,3,4]:
              flag = False
              locations.append(location)
            else:
              print(f"Wrong input, try again.")
          except ValueError:
            print("Wrong input, try again.")
    print(f"damage locations: {locations}")
    for location in locations:
      if location == 1:
        if self.ship.hold > 0:
          self.ship.hold -= 1
        else:
          self.ship.hull -= 1
      elif location == 2:
        if self.ship.sails > 0:
          self.ship.sails -= 1
        else:
          self.ship.hull -= 1
      elif location == 3:
        if self.ship.canons > 0:
          self.ship.canons -= 1
        else:
          self.ship.hull -= 1
      elif location == 4:
        if self.ship.crew > 0:
          self.ship.crew -= 1
        else:
          self.ship.hull -= 1

    if self.ship.hull <= 0:
      print(f"{self.name}'s ship is destroyed!")
      return False
    else:
      return True
