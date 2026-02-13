import os

from Captain import Captain
from Ship import Ship


def player_setup(
    console: bool,
    player_name: str = "Player",
    player_nationality: str = "French",
    player_ship: int = 1,
):
    """Creates a player based on user input."""

    # console:
    if console:
        player_name = input("Enter your name:\n")
        if player_name == "":
            player_name = "Player"
        player_nationality = ""
        while player_nationality == "":
            player_nationality = input(
                "Pick your nationality (1 - French, 2 - British, 3 - Dutch, 4 - Spanish):\n"
            )
            if player_nationality not in ["1", "2", "3", "4"]:
                print("Invalid input. Try again.")
                player_nationality = ""
    if player_nationality == "1":
        player_nationality = "French"
    elif player_nationality == "2":
        player_nationality = "British"
    elif player_nationality == "3":
        player_nationality = "Dutch"
    elif player_nationality == "4":
        player_nationality = "Spanish"
    return Captain(player_name, player_nationality, Ship(player_ship), False)


def game_init(player: Captain) -> list[Captain]:
    """Creates a list of players."""

    players = []
    players.append(player)
    players.append(Captain("Marine", "French", Ship(1), True))
    players.append(Captain("John", "British", Ship(2), True))
    players.append(Captain("Erik", "Dutch", Ship(3), True))
    players.append(Captain("Vanessa", "Spanish", Ship(4), True))
    players.append(Captain("Donald Truck", "American", Ship(5), True))
    return players


def manouver(captain: Captain):
    """Captain rolls self.sailing dice. If his ship's sails are destroyed, he rolls only one die."""

    if captain.ship.sails == 0:
        print(
            f"{captain.name}'s sails are shredded! {captain.name} rolls with only 1 die!"
        )
        captain_roll = captain.roll(1)
        print(captain.skulify_roll(captain_roll))
    else:
        print(f"{captain.name} is rolling for sailing:")
        captain_roll = captain.roll(captain.sailing)
        print(captain.skulify_roll(captain_roll))
    return captain_roll


def count_score(roll):
    """Counts the number of 5s and 6s in a roll."""
    score = 0
    for die in roll:
        if die == 5 or die == 6:
            score += 1
    return score


def battle(captain1: Captain, captain2: Captain):
    """Simulates a battle between two captains."""
    outcome = 0  # 1 if captain1 won, 2 if captain2 won, 3 if one of captains escapes and 4 if both captains' ships are destroyed.
    while outcome not in [1, 2, 3, 4]:
        os.system("clear")
        # Output the condition of ships
        print(f"{captain1.name}'s ship {captain1.ship}")
        print(f"{captain2.name}'s ship {captain2.ship}")

        # declaration phase - each captain decides what to do in the next turn:
        decision1 = captain1.battle_declaration()
        decision2 = captain2.battle_declaration()

        # manouvering phase - each Captain rolls for sailing:
        captain1_roll = manouver(captain1)
        captain2_roll = manouver(captain2)

        # who won?
        score1 = count_score(captain1_roll)
        score2 = count_score(captain2_roll)

        if score1 > score2:
            winner = captain1
            loser = captain2
            winner_decision = decision1
            loser_decision = decision2
            loser_score = score2
            print(f"{winner.name} outmanouvered {loser.name}!")
        elif score2 > score1:
            winner = captain2
            loser = captain1
            winner_decision = decision2
            loser_decision = decision1
            loser_score = score1
            print(f"{winner.name} outmanouvered {loser.name}!")
        else:
            print("Draw!")
            winner_decision = 0

        # the winner's action is being processed:
        # 1. If the winner chose fire canons - all his canons are fired (loser fires as many canons, as he had skulls in manouvering phase and only if his decision was to fire canons)
        # 2. If the winner chose boarding - crew fight begins
        # 3. If the winner chose fleeing he flees
        if winner_decision == 1:
            damage_to_loser = winner.fire_canons(winner.ship.canons)
            if loser_decision == 1 and loser_score != 0:
                damage_to_winner = loser.fire_canons(loser_score)

                print(f"{winner.name} fires canons:")
                print(winner.skulify_roll(damage_to_loser))
                print(f"{loser.name} fires canons:")
                print(loser.skulify_roll(damage_to_winner))

                loser.ship.receive_damage(damage_to_loser)
                winner.ship.receive_damage(damage_to_winner)

            else:
                print(f"{winner.name} fires canons:")
                print(winner.skulify_roll(damage_to_loser))
                loser.ship.receive_damage(damage_to_loser)

        elif winner_decision == 2:
            print("Crew fight begins!")
            outcome = crew_fight(captain1, captain2)

        elif winner_decision == 3:
            # check whether can escape
            if loser_score <= 0:
                print(f"{winner.name} managed to escape!")
                outcome = 3
            else:
                print(f"{captain1.name} did not manage to escape!")
                if loser_decision == 1 and loser_score != 0:
                    print(f"{loser.name} fires canons:")
                    winner.ship.receive_damage(loser.fire_canons(loser_score))
        else:
            # draw case
            pass

        # checking whether any ship is destroyed
        if captain2.ship.is_destroyed():
            outcome = 1
        if captain1.ship.is_destroyed():
            outcome = 2
        if captain1.ship.is_destroyed() and captain2.ship.is_destroyed():
            outcome = 4
        input("Press enter to continue\n")

    # TODO: Implement outcome handling
    return outcome


def crew_fight(captain1: Captain, captain2: Captain) -> int:
    """Captains fight until one of them loses all crew. Returns 1 if captain1 won, and 2 if captain2 won."""

    while captain1.ship.crew > 0 and captain2.ship.crew > 0:
        damage1 = captain1.crew_attack()
        damage2 = captain2.crew_attack()
        print(f"captain1 damage: {damage1}")
        print(f"captain2 damage: {damage2}")
        captain1.ship.crew -= damage2
        captain2.ship.crew -= damage1

    if captain2.ship.crew <= 0:
        print(f"{captain1.name} won the crew fight!")
        captain2.ship.hull = 0
        return 1
    elif captain1.ship.crew <= 0:
        print(f"{captain2.name} won the crew fight!")
        captain1.ship.hull = 0
        return 2
    else:
        return 4
