from Captain import Captain
import os

def battle(captain1: Captain, captain2: Captain):
  flag = True
  while flag:
    os.system('clear')
    # determing ships state:
    print(captain1.ship)
    print(captain2.ship)

    #declaration phase - each captain decides what to do in the next turn:
    decision1 = captain1.battle_declaration()
    decision2 = captain2.battle_declaration()

    #manouvering phase - each Captain rolls for sailing:
    print(f"{captain1.name} is rolling for sailing:")
    if captain1.ship.sails == 0:
      print(f"{captain1.name}'s sails are shredded! {captain1.name} rolls with only 1 die!")
      captain1_roll = captain1.roll(1)
    else:
      captain1_roll = captain1.roll(captain1.sailing)

    print(f"{captain2.name} is rolling for sailing:")
    if captain2.ship.sails == 0:
      print(f"{captain2.name}'s sails are shredded! {captain2.name} rolls with only 1 die!")
      captain2_roll = captain2.roll(1)
    else:
      captain2_roll = captain2.roll(captain2.sailing)

    # who won?
    score1 = 0
    score2 = 0
    for die in captain1_roll:
      if die == 5 or die ==6:
        score1 += 1
    for die in captain2_roll:
      if die == 5 or die ==6:
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
      print(f"Draw!")
      winner_decision = 0

    # the winner's action is being processed:
    # 1. If the winner chose fire canons - all canons are fired
    # 2. If the winner chose boarding - crew fight begins
    # 3. If the winner chose fleeing he flees
    if winner_decision == 1:
      #fire all canons
      print(f"{winner.name} fires canons:")
      damage_to_loser = winner.fire_canons(winner.ship.canons)
      if loser_decision == 1 and loser_score !=0:
        flag = loser.receive_damage(damage_to_loser)
        damage_to_winner = loser.fire_canons(loser_score)
        print(f"{loser.name} fires canons:")
        flag = winner.receive_damage(damage_to_winner)
      else:
        flag = loser.receive_damage(damage_to_loser)
    elif winner_decision == 2:
      #start boarding
      result = crew_fight(captain1, captain2)
      if result == 1:
        #cap1 won. What now?
      if result == 2:
        #cap2 won. What now?
    elif winner_decision == 3:
      #check whether can escape
      if (loser_score <= 0):
        #stop battle
        print(f"{captain1.name} managed to escape!")
        return captain1
      else:
        print(f"{captain1.name} did not manage to escape!")
        if loser_decision == 1 and loser_score != 0:
          print(f"{loser.name} fires canons:")
          flag = winner.receive_damage(loser.fire_canons(loser_score))
    else:
      # draw case
      pass
    input("Press enter to continue\n")


def crew_fight(captain1: Captain, captain2: Captain):
  while captain1.ship.crew > 0 and captain2.ship.crew > 0:
    damage1 = captain1.crew_fight()
    damage2 = captain2.crew_fight()
    print(f"captain1 damage: {damage1}")
    print(f"captain2 damage: {damage2}")
    captain1.ship.crew -= damage2
    captain2.ship.crew -= damage1

  if captain1.ship.crew <= 0:
    print(f"{captain2.name} won the crew fight!")
    return 1
  if captain2.ship.crew <= 0:
    print(f"{captain1.name} won the crew fight!")
    return 2
