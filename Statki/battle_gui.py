from tkinter import *
from tkinter import ttk

import state
from Captain import Captain
from Ship import Ship


class Battle_GUI:
    def __init__(self, root, captain1: Captain, captain2: Captain):
        self.captain1 = captain1
        self.captain2 = captain2

        self.ship1 = StringVar()
        self.ship2 = StringVar()
        self.ship1.set(self.captain1.ship)
        self.ship2.set(self.captain2.ship)

        root.title("Statki")

        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))  # left, up, right, down
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # buttons:
        flee = ttk.Button(mainframe, text="Flee")
        fire = ttk.Button(mainframe, text="Fire canons!", command=self.fire)
        board = ttk.Button(mainframe, text="Board")

        # text fields:
        captain1 = ttk.Label(mainframe, text=self.captain1)
        captain2 = ttk.Label(mainframe, text=self.captain2)
        captain1_ship = ttk.Label(mainframe, textvariable=self.ship1)
        captain2_ship = ttk.Label(mainframe, textvariable=self.ship2)

        vs = ttk.Label(mainframe, text="VS")

        # result frame:
        result_frame = ttk.Frame(
            mainframe, borderwidth=5, relief="ridge", width=100, height=200
        )

        # placement:
        captain1.grid(column=1, row=1, sticky=(N, W))
        captain1_ship.grid(column=1, row=2, sticky=(N, W))
        captain2.grid(column=3, row=1, sticky=(N, E))
        captain2_ship.grid(column=3, row=2, sticky=(N, E))

        vs.grid(column=2, row=1, sticky=N)
        result_frame.grid(column=2, row=2, columnspan=1, rowspan=1, sticky=(N, S, W, E))
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
        self.captain1.battle_declaration()


def test():
    root = Tk()
    ship = Ship(1)
    ship2 = Ship(3)
    player = Captain("player_name_mr_captain", "Polish", 4, 5, 6, ship)
    enemy = Captain("JohnAI", "British", 1, 2, 3, ship2)
    Battle_GUI(root, player, enemy)
    root.mainloop()
