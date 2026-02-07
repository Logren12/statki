from asyncio.unix_events import SelectorEventLoop
from tkinter import *
from tkinter import ttk

import game_utils
from Captain import Captain
from Ship import Ship


class GameGUI:
    def __init__(self, root, captain1: Captain, captain2: Captain):
        self.captain1 = captain1
        self.captain2 = captain2
        self.ship1 = StringVar()
        self.ship2 = StringVar()
        self.round_number = IntVar()
        self.round_number_text = StringVar(value="VS")
        self.message = StringVar()
        self.declaration = IntVar()
        self.result = IntVar()

        self.ship1.set(str(self.captain1.ship))
        self.ship2.set(str(self.captain2.ship))
        root.title("Statki")
        self.root = root

        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))  # left, up, right, down
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # buttons:
        flee = ttk.Button(mainframe, text="Flee", command=self.flee)
        fire = ttk.Button(mainframe, text="Fire canons!", command=self.fire)
        board = ttk.Button(mainframe, text="Board", command=self.board)

        # text fields:
        captain1_text = ttk.Label(mainframe, text=str(self.captain1))
        captain2_text = ttk.Label(mainframe, text=str(self.captain2))
        captain1_ship = ttk.Label(mainframe, textvariable=self.ship1)
        captain2_ship = ttk.Label(mainframe, textvariable=self.ship2)

        vs = ttk.Label(mainframe, textvariable=self.round_number_text)

        # message frame:
        message_frame = ttk.Frame(
            mainframe, borderwidth=5, relief="ridge", width=300, height=200
        )
        message_field = ttk.Label(message_frame, textvariable=self.message)

        # placement:
        captain1_text.grid(column=1, row=1, sticky=(N, W))
        captain1_ship.grid(column=1, row=2, sticky=(N, W))
        captain2_text.grid(column=3, row=1, sticky=(N, E))
        captain2_ship.grid(column=3, row=2, sticky=(N, E))

        vs.grid(column=2, row=1, sticky=N)
        message_frame.grid(
            column=2, row=2, columnspan=1, rowspan=1, sticky=(N, S, W, E)
        )
        message_field.grid(column=0, row=0, sticky=(N, S, W, E))

        flee.grid(column=1, row=4, sticky=(S, W))
        fire.grid(column=2, row=4, sticky=S)
        board.grid(column=3, row=4, sticky=(S, E))

        # placement config
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=1)
        mainframe.columnconfigure(3, weight=1)
        mainframe.rowconfigure(1, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.rowconfigure(3, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def fire(self):
        self.declaration.set(1)
        self.result.set(self.battle_GUI())
        self.end_round()

    def board(self):
        self.declaration.set(2)
        self.result.set(self.battle_GUI())
        self.end_round()

    def flee(self):
        self.declaration.set(3)
        self.result.set(self.battle_GUI())
        self.end_round()

    def end_round(self):
        self.ship1.set(str(self.captain1.ship))
        self.ship2.set(str(self.captain2.ship))
        # debugging:
        print(f"result: {self.result.get()}")

        if self.result.get() != 0:
            self.root.destroy()

    def update_message(self, new_message):
        """appends new_message to self.message after newline."""
        self.message.set(f"{self.message.get()}\n {new_message}")

    def manouver(self, captain: Captain):
        """Captain rolls self.sailing dice. If his ship's sails are destroyed, he rolls only one die."""

        if captain.ship.sails == 0:
            captain_roll = captain.roll(1)
            self.update_message(
                f"{captain.name}'s sails are shredded! {captain.name} rolls with only 1 die: {captain.skulify_roll(captain_roll)}"
            )
        else:
            captain_roll = captain.roll(captain.sailing)
            self.update_message(
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

    def battle_GUI(self) -> int:
        """Simulates a round of battle between two captains."""
        self.round_number.set(self.round_number.get() + 1)
        self.round_number_text.set(f"VS\nRound: {self.round_number.get()}")
        self.message.set(f"Round {self.round_number.get()} begins!")
        outcome = 0
        decision1 = self.declaration.get()
        decision2 = self.captain2.battle_declaration()

        # manouvering phase - each Captain rolls for sailing:
        captain1_roll = self.manouver(self.captain1)
        captain2_roll = self.manouver(self.captain2)

        # determining the winner of the maneuvering phase
        score1 = self.count_score(captain1_roll)
        score2 = self.count_score(captain2_roll)

        if score1 > score2:
            winner = self.captain1
            loser = self.captain2
            winner_decision = decision1
            loser_decision = decision2
            loser_score = score2
            self.update_message(f"{winner.name} outmanouvered {loser.name}!")

        elif score2 > score1:
            winner = self.captain2
            loser = self.captain1
            winner_decision = decision2
            loser_decision = decision1
            loser_score = score1
            self.update_message(f"{winner.name} outmanouvered {loser.name}!")
        else:
            self.update_message("Draw!")
            return 0

        if winner_decision == 1:
            damage_to_loser = winner.fire_canons(winner.ship.canons)

            if loser_decision == 1 and loser_score != 0:
                damage_to_winner = loser.fire_canons(loser_score)

                self.update_message(
                    f"{winner.name} fires canons: {winner.skulify_roll(damage_to_loser)}"
                )
                self.update_message(
                    f"{loser.name} fires canons: {loser.skulify_roll(damage_to_winner)}"
                )

                loser.ship.receive_damage(damage_to_loser)
                winner.ship.receive_damage(damage_to_winner)

            else:
                self.update_message(
                    f"{winner.name} fires canons: {winner.skulify_roll(damage_to_loser)}"
                )
                loser.ship.receive_damage(damage_to_loser)

        elif winner_decision == 2:
            self.update_message("Crew fight begins!")
            outcome = game_utils.crew_fight(self.captain1, self.captain2)

        elif winner_decision == 3:
            self.update_message(f"{winner.name} managed to escape!")
        else:
            # draw case
            pass

        # checking whether any ship is destroyed
        if self.captain2.ship.is_destroyed():
            outcome = 1
        if self.captain1.ship.is_destroyed():
            outcome = 2
        if self.captain1.ship.is_destroyed() and self.captain2.ship.is_destroyed():
            outcome = 4
        if not (self.captain1.ship.is_destroyed() or self.captain2.ship.is_destroyed()):
            outcome = 0

        return outcome


def test():
    root = Tk()
    ship = Ship(1)
    ship2 = Ship(3)
    player = Captain("player_name_mr_captain", "Polish", 4, 5, ship)
    enemy = Captain("JohnAI", "British", 1, 2, ship2, True)
    GameGUI(root, player, enemy)
    root.mainloop()
