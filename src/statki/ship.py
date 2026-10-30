from typing import ClassVar

class Ship:
    SHIP_TYPES: ClassVar[dict[str, tuple[int, int, int, int, int]]] = {
        "Sloop": (2, 1, 2, 1, 2),  # Hull, Hold, Sails, Cannons, Crew
        "Fluyt": (2, 2, 1, 2, 2),
        "Frigate": (3, 3, 3, 3, 3),
        "Galleon": (4, 5, 3, 3, 4),
        "Ship of the line": (5, 5, 5, 5, 5),
    }

    SHIP_LEVELS = ("Sloop", "Fluyt", "Frigate", "Galleon", "Ship of the line")

    COMPARTMENTS: ClassVar[dict[int, str]] = {1: "hold", 2: "sails", 3: "cannons", 4: "crew"}

    def __init__(self, ship_type_on_create: int):
        if 1 <= ship_type_on_create <= len(self.SHIP_LEVELS):
            self.ship_type = self.SHIP_LEVELS[ship_type_on_create - 1]
        else:
            self.ship_type = "Sloop"
        self.full_repair()

    def __str__(self):
        return (
            f"type: {self.ship_type}\n"
            f"   Hull:   {self.hull * '♥'}\n"
            f" 1 Hold:   {self.hold * '♥'}\n"
            f" 2 Sails:  {self.sails * '♥'}\n"
            f" 3 Cannons: {self.cannons * '♥'}\n"
            f" 4 Crew:   {self.crew * '♥'}\n"
        )

    def determine_ship_level(self) -> int:
        if self.ship_type in self.SHIP_LEVELS:
            return self.SHIP_LEVELS.index(self.ship_type) + 1
        else:
            return 0

    def is_destroyed(self):
        return self.hull <= 0

    def receive_damage(self, locations: list[int]):
        """Distributes damage from enemy cannons."""

        for location in locations:
            if location not in self.COMPARTMENTS:
                raise ValueError(f"Invalid location: {location}")
            if self.is_destroyed():
                break
            loc_name: str = self.COMPARTMENTS[location]
            old_value = getattr(self, loc_name)
            if old_value > 0:
                setattr(self, loc_name, old_value - 1)
            else:
                self.hull -= 1

    def full_repair(self):
        """Checks the ship's type and sets its attributes accordingly."""
        stats = self.SHIP_TYPES.get(self.ship_type, self.SHIP_TYPES["Sloop"])
        self.hull, self.hold, self.sails, self.cannons, self.crew = stats
