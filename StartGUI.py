from tkinter import *
from tkinter import ttk

from Captain import Captain
from Ship import Ship


class StartGUI:
    """Gui handling the beginning of the game."""

    def __init__(self, root):
        # variables:
        self.name = StringVar()
        self.nationality = StringVar()
        self.ship = IntVar()
        self.isok_text = StringVar()
        self.nationality_modifiers = StringVar()
        self.players = []

        # initialize default values:
        self.ship.set(3)
        self.nationality.set("British")
        self.update_modifiers()

        # tkk elements (in order of appearance):
        root.title("Statki")
        main_frame = ttk.Frame(root, padding=(12, 12, 12, 12))
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        name_label = ttk.Label(main_frame, text="name:")
        name_entry = ttk.Entry(main_frame, width=7, textvariable=self.name)
        nationality_label = ttk.Label(main_frame, text="nationality:")
        nationality_frame = ttk.Frame(main_frame)
        french = ttk.Radiobutton(
            nationality_frame,
            text="French",
            variable=self.nationality,
            value="French",
            command=self.update_modifiers,
        )
        british = ttk.Radiobutton(
            nationality_frame,
            text="British",
            variable=self.nationality,
            value="British",
            command=self.update_modifiers,
        )
        dutch = ttk.Radiobutton(
            nationality_frame,
            text="Dutch",
            variable=self.nationality,
            value="Dutch",
            command=self.update_modifiers,
        )
        spanish = ttk.Radiobutton(
            nationality_frame,
            text="Spanish",
            variable=self.nationality,
            value="Spanish",
            command=self.update_modifiers,
        )
        modifiers_label = ttk.Label(main_frame, text="nationality modifier:")
        modifiers_text = ttk.Label(main_frame, textvariable=self.nationality_modifiers)
        ship_label = ttk.Label(main_frame, text="ship:")
        ship_frame = ttk.Frame(main_frame)
        sloop = ttk.Radiobutton(ship_frame, text="Sloop", variable=self.ship, value=1)
        fluyt = ttk.Radiobutton(ship_frame, text="Flyut", variable=self.ship, value=2)
        frigate = ttk.Radiobutton(
            ship_frame, text="Frigate", variable=self.ship, value=3
        )
        galleon = ttk.Radiobutton(
            ship_frame, text="Galleon", variable=self.ship, value=4
        )
        ship_of_the_line = ttk.Radiobutton(
            ship_frame, text="Ship of the Line", variable=self.ship, value=5
        )

        isok_label = ttk.Label(main_frame, textvariable=self.isok_text)
        next_button = ttk.Button(main_frame, text="Next", command=self.check)

        # elements' placement:
        name_label.grid(column=1, row=1, sticky=(W, E))
        name_entry.grid(column=2, row=1, sticky=(W, E))
        nationality_label.grid(column=1, row=2, sticky=(W, E))
        nationality_frame.grid(column=2, row=2, sticky=(W, E))
        modifiers_label.grid(column=1, row=3, sticky=W)
        modifiers_text.grid(column=2, row=3)
        ship_label.grid(column=1, row=4, sticky=(W, E))
        ship_frame.grid(column=2, row=4, sticky=(N, S, W, E))
        isok_label.grid(column=1, row=5, sticky=(W, E))
        next_button.grid(column=2, row=5, sticky=(W, E))

        # nationality_frame elements' placement:
        french.grid(column=1, row=0, sticky=W)
        british.grid(column=2, row=0)
        dutch.grid(column=3, row=0)
        spanish.grid(column=4, row=0, sticky=E)

        # ship_frame elements' placement:
        sloop.grid(column=1, row=0, sticky=W)
        fluyt.grid(column=2, row=0)
        frigate.grid(column=3, row=0)
        galleon.grid(column=4, row=0)
        ship_of_the_line.grid(column=5, row=0, sticky=E)

        # placement config:
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)
        main_frame.rowconfigure(4, weight=1)

        ship_frame.rowconfigure(0, weight=1)
        ship_frame.columnconfigure(1, weight=1)
        ship_frame.columnconfigure(2, weight=1)
        ship_frame.columnconfigure(3, weight=1)
        ship_frame.columnconfigure(4, weight=1)
        ship_frame.columnconfigure(5, weight=1)

        nationality_frame.rowconfigure(0, weight=1)
        nationality_frame.columnconfigure(1, weight=1)
        nationality_frame.columnconfigure(2, weight=1)
        nationality_frame.columnconfigure(3, weight=1)
        nationality_frame.columnconfigure(4, weight=1)

        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in ship_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in nationality_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        name_entry.focus()
        root.bind("<Return>", self.check)
        self.root = root
        root.wait_window()

    def update_modifiers(self):
        """Updates the modifiers_text based on the selected nationality."""
        if self.nationality.get() == "French":
            self.nationality_modifiers.set("1 ⎈ | 4 ⚔")
        elif self.nationality.get() == "British":
            self.nationality_modifiers.set("4 ⎈ | 1 ⚔")
        elif self.nationality.get() == "Dutch":
            self.nationality_modifiers.set("3 ⎈ | 2 ⚔")
        elif self.nationality.get() == "Spanish":
            self.nationality_modifiers.set("2 ⎈ | 3 ⚔")

    def players_setup(self):
        """Creates a list of players."""
        players = []
        players.append(
            Captain(
                self.name.get(), self.nationality.get(), Ship(self.ship.get()), False
            )
        )
        players.append(Captain("Marine", "French", Ship(1), True))
        players.append(Captain("John", "British", Ship(2), True))
        players.append(Captain("Erik", "Dutch", Ship(3), True))
        players.append(Captain("Vanessa", "Spanish", Ship(4), True))
        players.append(Captain("Donald Truck", "American", Ship(5), True))
        self.players = players

    def check(self, *args):
        if self.name.get() == "":
            self.isok_text.set("Name is required")
        elif self.nationality.get() not in ["French", "British", "Dutch", "Spanish"]:
            self.isok_text.set("Nationality is required")
        elif self.ship.get() not in [1, 2, 3, 4, 5]:
            self.isok_text.set("Ship is required")
        else:
            self.isok_text.set("OK")
            self.players_setup()
            self.root.destroy()
