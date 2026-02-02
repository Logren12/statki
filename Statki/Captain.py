import random

from Ship import Ship


class Captain:
    """Class representing a captain (player or bot)."""

    def __init__(
        self,
        name: str,
        nationality: str,
        sailing: int,
        leadership: int,
        reconnaissance: int,
        ship: Ship,
    ):
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

    def roll(self, no_dice: int):
        """Simulates rolling dice by generating random numbers from 1 to 6.
        no_dice: The number of dice to roll.
        returns: Empty list or a list of integers."""

        roll = []
        for i in range(no_dice):
            die = random.randint(1, 6)
            roll.append(die)
        return roll

    def print_roll(self, roll):
        """Outputs rolls to console, changing 5 and 6 to skulls."""
        output = "["
        for die in roll:
            if die in [5, 6]:
                output += " ☠️"
            else:
                output += " " + str(die)
        output += " ]"
        print(output)

    def search(self) -> bool:
        """Captain rolls reconnaissance dice. If any skulls (5 or 6) are rolled, a ship is found."""

        print("Searching for ships!")
        roll = self.roll(self.reconnaissance)
        self.print_roll(roll)
        if (5 in roll) or (6 in roll):
            return True
        else:
            return False

    def attack_decision(self, target):
        decision = 0
        while decision not in [1, 2]:
            try:
                decision = int(
                    input(
                        f"You have found a {target.nationality} {target.ship.ship_type}. Do You want to attack it?\n(1 - yes, 2 - no)\n"
                    )
                )
                if decision not in [1, 2]:
                    print("Wrong input, try again.")
            except ValueError:
                print("Wrong input, try again.")
        if decision == 1:
            return True
        else:
            return False

    # battle interactions:
    def battle_declaration(self):
        decision = 0
        while decision not in [1, 2, 3]:
            try:
                print(f"{self.name} declare intent:")
                decision = int(
                    input(" 1 - fire canons\n 2 - attempt boarding\n 3 - flee\n")
                )
                if decision not in [1, 2, 3]:
                    print("Wrong input, try again.")
            except ValueError:
                print("Wrong input, try again.")

        return decision

    def crew_attack(self):
        roll = self.roll(self.leadership)
        self.print_roll(roll)
        damage = 0
        for dice in roll:
            if dice in [5, 6] and damage < self.ship.crew:
                damage += 1
        return damage

    def fire_canons(self, number: int):
        """Fires cannons - returns a list of dice rolls that represent the damage dealt."""

        if self.ship.canons >= number:
            roll = self.roll(number)
            return roll
        elif (self.ship.canons < number) and (self.ship.canons != 0):
            roll = self.roll(self.ship.canons)
            return roll
        else:
            return []

    def receive_damage(self, roll):
        """Distributes damage from enemy cannons. Returns True if ship is destroyed."""
        locations = []  # a list containing places that are hit

        for die in roll:
            if die in [1, 2, 3, 4]:
                locations.append(die)
            elif (
                die == 5 or die == 6
            ):  # for any skull (5 or 6) in enemy roll, captain may pick damage location herself
                flag = True
                while flag:
                    try:
                        location = int(
                            input(f"\r{self.name}, pick damage location (1-4):\n")
                        )
                        if location in [1, 2, 3, 4]:
                            flag = False
                            locations.append(location)
                        else:
                            print("Wrong input, try again.")
                    except ValueError:
                        print("Wrong input, try again.")

        print(f"\r{self.name} damage locations: {locations}")
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
