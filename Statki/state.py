import os

from Captain import Captain
from Ship import Ship


def game_init(
    player_name: str = "",
    nationality: str = "",
    ship: int = 1,
    console: bool = False,  # if True allows to enter player's info via console
) -> list[Captain]:
    """Initializes the game by asking for player's name, nationality, and ship type and creating list of players."""
    if console:
        player = input("Enter your name:\n")
        nationality = ""
        while nationality == "":
            nationality = input(
                "Pick your nationality (1 - French, 2 - English, 3 - Dutch, 4 - Spanish):\n"
            )
            if nationality not in ["1", "2", "3", "4"]:
                print("Invalid input. Try again.")
                nationality = ""
            else:
                if nationality == "1":
                    nationality = "French"
                elif nationality == "2":
                    nationality = "English"
                elif nationality == "3":
                    nationality = "Dutch"
                elif nationality == "4":
                    nationality = "Spanish"

    players = []
    players.append(Captain(player_name, nationality, 4, 1, 2, Ship(ship), False))
    players.append(Captain("John", "English", 3, 3, 3, Ship(3), True))
    players.append(Captain("Marine", "French", 4, 3, 3, Ship(2), True))
    players.append(Captain("Erik", "Dutch", 5, 4, 3, Ship(3), True))
    players.append(Captain("Vanessa", "Spanish", 4, 5, 3, Ship(4), True))
    return players


def battle(captain1: Captain, captain2: Captain):
    """Simulates a battle between two captains."""
    outcome = 0  # 1 if captain1 won, 2 if captain2 won, 3 if one of captains escapes and 4 if both captains' ships are destroyed.
    while outcome not in [1, 2, 3, 4]:
        os.system("clear")
        # Output the condition of ships
        print(captain1.ship)
        print(captain2.ship)

        # declaration phase - each captain decides what to do in the next turn:
        decision1 = captain1.battle_declaration()
        decision2 = captain2.battle_declaration()

        # manouvering phase - each Captain rolls for sailing:
        print(f"{captain1.name} is rolling for sailing:")
        if captain1.ship.sails == 0:
            print(
                f"{captain1.name}'s sails are shredded! {captain1.name} rolls with only 1 die!"
            )
            captain1_roll = captain1.roll(1)
            captain1.print_roll(captain1_roll)
        else:
            captain1_roll = captain1.roll(captain1.sailing)
            captain1.print_roll(captain1_roll)

        print(f"{captain2.name} is rolling for sailing:")
        if captain2.ship.sails == 0:
            print(
                f"{captain2.name}'s sails are shredded! {captain2.name} rolls with only 1 die!"
            )
            captain2_roll = captain2.roll(1)
            captain2.print_roll(captain2_roll)
        else:
            captain2_roll = captain2.roll(captain2.sailing)
            captain2.print_roll(captain2_roll)

        # who won?
        score1 = 0
        score2 = 0
        for die in captain1_roll:
            if die == 5 or die == 6:
                score1 += 1
        for die in captain2_roll:
            if die == 5 or die == 6:
                score2 += 1

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
                winner.print_roll(damage_to_loser)
                print(f"{loser.name} fires canons:")
                loser.print_roll(damage_to_winner)

                loser.receive_damage(damage_to_loser)
                winner.receive_damage(damage_to_winner)

            else:
                print(f"{winner.name} fires canons:")
                winner.print_roll(damage_to_loser)
                loser.receive_damage(damage_to_loser)

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
                    winner.receive_damage(loser.fire_canons(loser_score))
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


def crew_fight(captain1: Captain, captain2: Captain):
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
        return 1
    if captain1.ship.crew <= 0:
        print(f"{captain2.name} won the crew fight!")
        return 2
