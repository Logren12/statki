class Ship:
    """Class representing a ship."""

    def __init__(self, ship_type_on_create: int):
        if ship_type_on_create == 1:
            self.ship_type = "Sloop"
            self.hull = 1
            self.hold = 1
            self.sails = 2
            self.canons = 1
            self.crew = 2
        elif ship_type_on_create == 2:
            self.ship_type = "Fluyt"
            self.hull = 2
            self.hold = 2
            self.sails = 1
            self.canons = 2
            self.crew = 2
        elif ship_type_on_create == 3:
            self.ship_type = "Frigate"
            self.hull = 3
            self.hold = 3
            self.sails = 3
            self.canons = 3
            self.crew = 3
        elif ship_type_on_create == 4:
            self.ship_type = "Galleon"
            self.hull = 4
            self.hold = 5
            self.sails = 3
            self.canons = 3
            self.crew = 4
        elif ship_type_on_create == 5:
            self.ship_type = "Ship of the line"
            self.hull = 5
            self.hold = 5
            self.sails = 5
            self.canons = 5
            self.crew = 5
        else:
            self.ship_type = "Sloop"
            self.hull = 2
            self.hold = 2
            self.sails = 1
            self.canons = 1
            self.crew = 2

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
        if self.ship_type == "Sloop":
            return 1
        elif self.ship_type == "Fluyt":
            return 2
        elif self.ship_type == "Frigate":
            return 3
        elif self.ship_type == "Galleon":
            return 4
        elif self.ship_type == "Ship of the line":
            return 5
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
        if self.ship_type == "Sloop":
            self.hull = 2
            self.hold = 1
            self.sails = 2
            self.canons = 1
            self.crew = 2
        elif self.ship_type == "Fluyt":
            self.hull = 2
            self.hold = 2
            self.sails = 1
            self.canons = 1
            self.crew = 2
        elif self.ship_type == "Frigate":
            self.hull = 3
            self.hold = 3
            self.sails = 3
            self.canons = 3
            self.crew = 3
        elif self.ship_type == "Galleon":
            self.hull = 3
            self.hold = 5
            self.sails = 4
            self.canons = 3
            self.crew = 4
        elif self.ship_type == "Ship of the line":
            self.hull = 5
            self.hold = 5
            self.sails = 5
            self.canons = 5
            self.crew = 5
