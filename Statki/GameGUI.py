from tkinter import *
from tkinter import messagebox, ttk

from Captain import Captain


class GameGUI:
    """This class handles the main UI for the game."""

    def __init__(self, root, player: Captain, enemy: Captain):
        """This method determines how GUI works and looks."""
        # variables:
        self.root = root
        self.player = player
        self.enemy = enemy
        self.player_ship = StringVar()
        self.enemy_ship = StringVar()
        self.round_number = IntVar()
        self.battle_log = StringVar(value="Declare your intention in the next round!")
        self.declaration = IntVar()
        self.result = IntVar()
        self.player_ship.set(str(self.player.ship))
        self.enemy_ship.set(str(self.enemy.ship))

        # tkk elements (in order of appearance):
        root.title("Sea battle")
        main_frame = ttk.Frame(root, padding=(12, 12, 12, 12))  # left, up, right, down
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # text fields:
        player_stats = ttk.Label(main_frame, text=str(self.player))
        enemy_stats = ttk.Label(main_frame, text=str(self.enemy))
        player_ship = ttk.Label(main_frame, textvariable=self.player_ship)
        enemy_ship = ttk.Label(main_frame, textvariable=self.enemy_ship)
        leave_label = ttk.Label(main_frame, text="Press 'esc' to exit the game.")

        # battlelog frame:
        battle_log_frame = ttk.LabelFrame(
            main_frame,
            text="Battle log",
            borderwidth=5,
            relief="ridge",
            width=500,
            height=200,
        )
        battle_log_content = ttk.Label(battle_log_frame, textvariable=self.battle_log)

        # buttons:
        flee_button = ttk.Button(main_frame, text="1 - Flee!", command=self.flee)
        fire_button = ttk.Button(main_frame, text="2 - Fire canons!", command=self.fire)
        board_button = ttk.Button(main_frame, text="3 - Board!", command=self.board)

        # placement:
        player_stats.grid(column=1, row=1, sticky=(N, W))
        leave_label.grid(column=2, row=1, sticky=N)
        enemy_stats.grid(column=3, row=1, sticky=(N, E))
        player_ship.grid(column=1, row=2, sticky=(N, W))
        battle_log_frame.grid(
            column=2, row=2, columnspan=1, rowspan=1, sticky=(N, S, W, E)
        )
        battle_log_content.grid(column=0, row=0, sticky=(N, S, W, E))
        enemy_ship.grid(column=3, row=2, sticky=(N, E))
        flee_button.grid(column=1, row=3, sticky=(S, W))
        fire_button.grid(column=2, row=3, sticky=S)
        board_button.grid(column=3, row=3, sticky=(S, E))

        # placement config
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # keyboard control:
        root.bind("1", self.flee)
        root.bind("2", self.fire)
        root.bind("3", self.board)
        root.bind("<Escape>", self.quit)

    # GUI FUNCTIONS:
    def quit(self, *args):
        self.result.set(2)
        self.root.destroy()

    def fire(self, *args):
        self.declaration.set(1)
        self.result.set(self.battle())
        self.end_round()

    def board(self, *args):
        self.declaration.set(2)
        self.result.set(self.battle())
        self.end_round()

    def flee(self, *args):
        self.declaration.set(3)
        self.result.set(self.battle())
        self.end_round()

    def end_round(self):
        """Updates ships' status. If any player has been sunk,
        displays a window with information about the round result."""

        self.log_update("Round over!")
        # updating ships' status
        self.player_ship.set(str(self.player.ship))
        self.enemy_ship.set(str(self.enemy.ship))

        battle_over_message = ""
        if self.result.get() == 1:
            battle_over_message = f"{self.player.name} destroyed {self.enemy.name}!"
        elif self.result.get() == 2:
            battle_over_message = f"{self.enemy.name} destroyed {self.player.name}!"
        elif self.result.get() == 3:
            battle_over_message = (
                f"{self.player.name} managed to escape!"  # bots will never try to flee
            )
        else:  # result ==4
            battle_over_message = "Everyone died! :("

        if self.result.get() != 0:
            messagebox.showinfo(
                title="Battle over",
                message="Battle over!",
                detail=battle_over_message,
                icon="info",
            )
            self.root.destroy()

    #######################################
    # IN BATTLE FUNCTIONS:
    def log_update(self, new_entry):
        """Appends new_entry to battle_log after newline."""
        self.battle_log.set(f"{self.battle_log.get()}\n {new_entry}")

    def manouver(self, captain: Captain):
        """Captain rolls self.sailing dice. If his ship's sails are destroyed, he rolls only one die."""

        if captain.ship.sails == 0:
            captain_roll = captain.roll(1)
            self.log_update(
                f"{captain.name}'s sails are shredded! {captain.name} rolls with only 1 die: {captain.skulify_roll(captain_roll)}"
            )
        else:
            captain_roll = captain.roll(captain.sailing)
            self.log_update(
                f"{captain.name} is rolling for sailing: {captain.skulify_roll(captain_roll)}"
            )
        return captain_roll

    def count_score(self, roll):
        """Counts the number of 5s and 6s in a roll."""
        score = 0
        for die in roll:
            if die == 5 or die == 6:
                score += 1
        return score

    def end_battle_check(self) -> int:
        """Checks, whether any ship is destroyed. Returns 0 if battle should continue, 1 if player wins, 2 if enemy wins, and 4 if both ships are destroyed"""
        if self.player.ship.is_destroyed() and self.enemy.ship.is_destroyed():
            self.log_update("Both ships were destroyed! Game over!")
            return 4
        if self.enemy.ship.is_destroyed():
            self.log_update(f"{self.player.name} destroyed {self.enemy.name}'s ship!")
            return 1
        if self.player.ship.is_destroyed():
            self.log_update(f"{self.enemy.name} destroyed {self.player.name}'s ship!")
            return 2
        else:
            return 0

    def battle(self) -> int:
        """Simulates a round of battle between two captains.
        Returns 0 if battle should continue, 1 if player wins, 2 if enemy wins, 3 if player manages to escape, and 4 if both ships are destroyed."""
        # check whether the battle should be over:
        if self.end_battle_check() != 0:
            return self.end_battle_check()

        self.round_number.set(self.round_number.get() + 1)
        self.battle_log.set(f"Round {self.round_number.get()} begins!")

        # declaration phase - each Captain declares their intention:
        player_decision = self.declaration.get()
        if self.enemy.ship.canons > 0:
            enemy_decision = 1
            self.log_update(f"{self.enemy.name} decided to fire cannons!")
        else:
            enemy_decision = 2
            self.log_update(f"{self.enemy.name} decided to aboard our ship!")

        # manouvering phase - each Captain rolls for sailing:
        player_roll = self.manouver(self.player)
        enemy_roll = self.manouver(self.enemy)

        # determining the winner of the maneuvering phase
        player_score = self.count_score(player_roll)
        enemy_score = self.count_score(enemy_roll)

        if player_score > enemy_score:
            winner = self.player
            loser = self.enemy
            winner_decision = player_decision
            loser_decision = enemy_decision
            loser_score = enemy_score
            self.log_update(f"{winner.name} outmanouvered {loser.name}!")

        elif enemy_score > player_score:
            winner = self.enemy
            loser = self.player
            winner_decision = enemy_decision
            loser_decision = player_decision
            loser_score = player_score
            self.log_update(f"{winner.name} outmanouvered {loser.name}!")
        else:  # Draw
            self.log_update("Draw!")
            damage_to_player = []
            damage_to_enemy = []
            if player_decision == 1 and player_score > 0:
                damage_to_enemy = self.player.fire_canons(player_score)
                self.log_update(
                    f"{self.player.name} fires canons: {self.player.skulify_roll(damage_to_enemy)}"
                )
            if enemy_decision == 1 and enemy_score > 0:
                damage_to_player = self.enemy.fire_canons(enemy_score)
                self.log_update(
                    f"{self.enemy.name} fires canons: {self.enemy.skulify_roll(damage_to_player)}"
                )
            self.enemy.ship.receive_damage(damage_to_enemy)
            self.player.ship.receive_damage(damage_to_player)
            return self.end_battle_check()

        # applying the winner's decision:
        if winner_decision == 1:
            damage_to_loser = winner.fire_canons(winner.ship.canons)

            if loser_decision == 1 and loser_score != 0:
                damage_to_winner = loser.fire_canons(loser_score)
                self.log_update(
                    f"{winner.name} fires canons: {winner.skulify_roll(damage_to_loser)}"
                )
                self.log_update(
                    f"{loser.name} fires canons: {loser.skulify_roll(damage_to_winner)}"
                )
                loser.ship.receive_damage(damage_to_loser)
                winner.ship.receive_damage(damage_to_winner)

            else:
                self.log_update(
                    f"{winner.name} fires canons: {winner.skulify_roll(damage_to_loser)}"
                )
                loser.ship.receive_damage(damage_to_loser)

        elif winner_decision == 2:
            self.log_update("Crew fight begins!")
            return self.crew_fight()

        else:  # winner_decision == 3:
            self.log_update(f"{winner.name} managed to escape!")
            return 3

        return self.end_battle_check()

    def capture_ship(self):
        "Player's ship type changes to defeated enemy's ship type if player's ship level is lower."
        ship1_level = self.player.ship.determine_ship_level()
        ship2_level = self.enemy.ship.determine_ship_level()

        if ship1_level < ship2_level:
            self.player.ship.ship_type = self.enemy.ship.ship_type
            self.log_update(f"{self.player.name} captured enemy's ship!")

    def crew_fight(self) -> int:
        """Captains fight until one of them loses all crew. Returns 1 if player won, 2 if enemy won and 4 in case of a draw. Player may capture enemy's ship."""
        player_damage_log = []
        enemy_damage_log = []

        while self.player.ship.crew > 0 and self.enemy.ship.crew > 0:
            player_damage = self.player.crew_attack()
            enemy_damage = self.enemy.crew_attack()

            self.player.ship.crew -= enemy_damage
            self.enemy.ship.crew -= player_damage
            player_damage_log.append(player_damage)
            enemy_damage_log.append(enemy_damage)

        self.log_update(f"{self.player.name} damage: {player_damage_log}")
        self.log_update(f"{self.enemy.name} damage: {enemy_damage_log}")

        if self.enemy.ship.crew <= 0 and self.player.ship.crew <= 0:
            self.log_update("Draw - everyone died :)")
            return 4
        elif self.enemy.ship.crew <= 0:
            self.log_update(f"{self.player.name} won the crew fight!")
            self.capture_ship()
            return 1
        elif self.player.ship.crew <= 0:
            self.log_update(f"{self.enemy.name} won the crew fight!")
            return 2
        else:
            # it will never happen - above conditions are exhaustive required for return syntax
            return 4
