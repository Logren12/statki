from tkinter import *
from tkinter import ttk


class startGUI:
    """Gui handling the beginning of the game."""

    def __init__(self, root):
        self.name = StringVar()
        self.nationality = StringVar()
        self.ship = IntVar()
        self.isok_text = StringVar()

        root.title("Statki")
        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # buttons:
        next = ttk.Button(mainframe, text="Next", command=self.check)

        self.ship.set(1)
        shipframe = ttk.Frame(mainframe)
        sloop = ttk.Radiobutton(shipframe, text="sloop", variable=self.ship, value=1)
        fluyt = ttk.Radiobutton(shipframe, text="Flyut", variable=self.ship, value=2)
        frigate = ttk.Radiobutton(
            shipframe, text="frigate", variable=self.ship, value=3
        )

        # text fields:
        name_entry = ttk.Entry(mainframe, width=7, textvariable=self.name)
        nationality_entry = ttk.Entry(mainframe, width=7, textvariable=self.nationality)

        name = ttk.Label(mainframe, text="name:")
        nationality = ttk.Label(mainframe, text="nationality:")
        ship = ttk.Label(mainframe, text="ship:")
        isok = ttk.Label(mainframe, textvariable=self.isok_text)
        # placement:
        name.grid(column=1, row=1, sticky=(W, E))
        name_entry.grid(column=2, row=1, sticky=(W, E))
        nationality.grid(column=1, row=2, sticky=(W, E))
        nationality_entry.grid(column=2, row=2, sticky=(W, E))
        ship.grid(column=1, row=3, sticky=(W, E))
        shipframe.grid(column=2, row=3, sticky=(N, S, W, E))
        sloop.grid(column=1, row=0, sticky=(W))
        fluyt.grid(column=2, row=0)
        frigate.grid(column=3, row=0, sticky=(E))
        isok.grid(column=1, row=4, sticky=(W, E))
        next.grid(column=2, row=4, sticky=(W, E))

        # placement config:
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=1)
        mainframe.columnconfigure(3, weight=1)
        mainframe.rowconfigure(1, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.rowconfigure(3, weight=1)

        shipframe.rowconfigure(0, weight=1)
        shipframe.columnconfigure(1, weight=1)
        shipframe.columnconfigure(2, weight=1)
        shipframe.columnconfigure(3, weight=1)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in shipframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        name_entry.focus()
        root.bind("<Return>", self.check)
        self.root = root
        root.wait_window()

    def check(self, *args):
        if self.name.get() == "":
            self.isok_text.set("Name is required")
        elif self.nationality.get() == "":
            self.isok_text.set("Nationality is required")
        elif self.ship.get() not in [1, 2, 3]:
            self.isok_text.set("Ship is required")
        else:
            self.isok_text.set("OK")
            self.root.destroy()
