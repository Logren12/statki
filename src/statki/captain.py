import random

from statki.ship import Ship

FACTIONS = {
    "British": ["🇬🇧",4,1],
    "French": ["🇫🇷",1,4],
    "Dutch": ["🇳🇱",3,2],
    "Spanish": ["🇪🇸",2,3]
}

class Captain:
    """Class representing a captain (player or bot)."""

    def __init__(
        self,
        name: str,
        faction: str,
        ship: Ship,
        isbot: bool = True,
    ):
        self.name = name
        self.ship = ship
        self.__isbot = isbot
        faction_data = FACTIONS.get(faction, ["🏳️", 1, 6])
        self.faction = faction_data[0]
        self.sailing = faction_data[1]
        self.leadership = faction_data[2]

    def __str__(self):
        return (
            f"Captain {self.name}\n"
            f"Faction: {self.faction}\n"
            f"Sailing: {self.sailing * '⎈'}\n"
            f"Leadership: {self.leadership * '⚔'}\n"
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

    def crew_attack(self) -> int:
        """Determines damage dealt by crew members to enemy crew during one round of crew fight."""
        roll = self.roll(self.leadership)
        damage = 0
        for dice in roll:
            if dice in [5, 6] and damage < self.ship.crew:
                damage += 1
        return damage

    def fire_cannons(self, number: int) -> list[int]:
        """Returns a list representing enemy locations hit by cannon fire."""
        roll = []
        if self.ship.cannons >= number:
            roll = self.roll(number)  # fires no more than number cannons
        elif (self.ship.cannons < number) and (self.ship.cannons != 0):
            roll = self.roll(self.ship.cannons)  # fires all available cannons
        else:
            return roll  # returns empty list if no cannons available

        locations = []
        for die in roll:
            if die in [1, 2, 3, 4]:
                locations.append(die)
            elif (
                die == 5 or die == 6
            ):  # for any skull (5 or 6) in enemy roll, damage is randomly asigned.
                locations.append(random.randint(1, 4))
            else:
                pass
        return locations
