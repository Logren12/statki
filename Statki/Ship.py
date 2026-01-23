class Ship:
  def __init__(self, ship_type):
    self.ship_type = ship_type
    if ship_type == "Sloop":
      self.hull = 2
      self.hold = 1
      self.sails = 2
      self.canons = 1
      self.crew = 2
    elif ship_type == "Frigate":
      self.hull = 3
      self.hold = 3
      self.sails = 3
      self.canons = 3
      self.crew = 3
    elif ship_type == "Galleon":
      self.hull = 3
      self.hold = 5
      self.sails = 4
      self.canons = 3
      self.crew = 4
    elif ship_type == "Ship of the line":
      self.hull = 5
      self.hold = 5
      self.sails = 5
      self.canons = 5
      self.crew = 5
    else:
      self.ship_type = "Fluyt"
      self.hull = 2
      self.hold = 2
      self.sails = 1
      self.canons = 1
      self.crew = 2
  def __str__(self):
    return (
      f"Type: {self.ship_type}\n"
      f"   Hull:   {self.hull * "*"}\n"
      f" 1 Hold:   {self.hold * "*"}\n"
      f" 2 Sails:  {self.sails * "*"}\n"
      f" 3 Canons: {self.canons * "*"}\n"
      f" 4 Crew:   {self.crew * "*"}\n"
  )
