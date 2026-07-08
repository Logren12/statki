class Ship:
    SHIP_TYPES = {
        "Sloop": (2, 1, 2, 1, 2),
        "Fluyt": (2, 2, 1, 2, 2),
        "Frigate": (3, 3, 3, 3, 3),
        "Galleon": (4, 5, 3, 3, 4),
        "Ship of the line": (5, 5, 5, 5, 5)
    }

    SHIP_LEVELS = ["Sloop", "Fluyt", "Frigate", "Galleon", "Ship of the line"]

    def __init__(self, ship_type_on_create: int):
        if 1 <= ship_type_on_create <= len(self.SHIP_LEVELS):
            self.ship_type = self.SHIP_LEVELS[ship_type_on_create - 1]
        else:
            self.ship_type = "Sloop"
        self.repair()

    def __str__(self):
        return (
            f"type: {self.ship_type}\n"
            f"   Hull:   {self.hull * '♥'}\n"
            f" 1 Hold:   {self.hold * '♥'}\n"
            f" 2 Sails:  {self.sails * '♥'}\n"
            f" 3 Canons: {self.canons * '♥'}\n"
            f" 4 Crew:   {self.crew * '♥'}\n"
        )

    def determine_ship_level(self) -> int:
        if self.ship_type in self.SHIP_LEVELS:
            return self.SHIP_LEVELS.index(self.ship_type) + 1
        else:
            return 0

    def receive_damage(self, locations: list[int]):
        """Distributes damage from enemy cannons."""
        for location in locations:
            if location == 1:
                if self.hold > 0:
                    self.hold -= 1
                else:
                    self.hull -= 1
            elif location == 2:
                if self.sails > 0:
                    self.sails -= 1
                else:
                    self.hull -= 1
            elif location == 3:
                if self.canons > 0:
                    self.canons -= 1
                else:
                    self.hull -= 1
            elif location == 4:
                if self.crew > 0:
                    self.crew -= 1
                else:
                    self.hull -= 1
            else:
                pass

    def is_destroyed(self):
        if self.hull <= 0:
            return True
        else:
            return False

    def repair(self):
        """Checks the ship's type and sets its attributes accordingly."""
        stats = self.SHIP_TYPES.get(self.ship_type, self.SHIP_TYPES["Sloop"])
        self.hull, self.hold, self.sails, self.canons, self.crew = stats
