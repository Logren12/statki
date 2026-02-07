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
        ship: Ship,
        isbot: bool = True,
    ):
        self.name = name
        self.nationality = nationality
        self.sailing = sailing
        self.leadership = leadership
        self.ship = ship
        self.__isbot = isbot

    def __str__(self):
        return (
            f"Captain {self.name}\n"
            f"Nationality: {self.nationality}\n"
            f"Sailing: {self.sailing}\n"
            f"Leadership: {self.leadership}\n"
            f"Ship: {self.ship.ship_type}\n"
        )

    def roll(self, no_dice: int) -> list[int]:
        """Simulates rolling dice by generating random numbers from 1 to 6.
        no_dice: The number of dice to roll.
        returns: Empty list or a list of integers."""

        roll = []
        for i in range(no_dice):
            die = random.randint(1, 6)
            roll.append(die)
        return roll

    def skulify_roll(self, roll: list[int]):
        """Returns roll as a string, changing 5 and 6 to skulls."""
        output = "["
        for die in roll:
            if die in [5, 6]:
                output += " ☠️"
            else:
                output += " " + str(die)
        output += " ]"
        return output

    # battle interactions:
    def battle_declaration(self):
        """Declared manouver in next turn. Asks user for input: 1,2 or 3 and returns it as int."""

        # for bots:
        if self.__isbot:
            if self.ship.canons > 0:
                return 1
            elif self.ship.crew <= 0:
                return 3
            else:
                return 2

        # for humans:
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

    def crew_attack(self) -> int:
        """Determines damage dealt by crew members to enemy crew during one round of crew fight."""
        roll = self.roll(self.leadership)
        print(self.skulify_roll(roll))
        damage = 0
        for dice in roll:
            if dice in [5, 6] and damage < self.ship.crew:
                damage += 1
        return damage

    def fire_canons(self, number: int) -> list[int]:
        """Fires cannons - returns a list of dice rolls that represent the enemy locations hit."""
        roll = []
        if self.ship.canons >= number:
            roll = self.roll(number)  # fires no more than number cannons
        elif (self.ship.canons < number) and (self.ship.canons != 0):
            roll = self.roll(self.ship.canons)  # fires all available cannons
        else:
            return roll  # returns empty list if no cannons available

        locations = []
        for die in roll:
            if die in [1, 2, 3, 4]:
                locations.append(die)
            elif (
                die == 5 or die == 6
            ):  # for any skull (5 or 6) in enemy roll, damage is randomly asigned.
                location = random.randint(1, 4)
                locations.append(location)
            else:
                pass
        return locations
