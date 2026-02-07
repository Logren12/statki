from tkinter import *
from tkinter import ttk


class StartGUI:
    """Gui handling the beginning of the game."""

    def __init__(self, root):
        # variables:
        self.name = StringVar()
        self.nationality = IntVar()
        self.ship = IntVar()
        self.isok_text = StringVar()
        self.nationality.set(1)
        self.ship.set(1)

        # tkk elements:
        root.title("Statki")
        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        nationalityframe = ttk.Frame(mainframe)
        french = ttk.Radiobutton(
            nationalityframe, text="French", variable=self.nationality, value=1
        )
        english = ttk.Radiobutton(
            nationalityframe, text="English", variable=self.nationality, value=2
        )
        dutch = ttk.Radiobutton(
            nationalityframe, text="Dutch", variable=self.nationality, value=3
        )
        spanish = ttk.Radiobutton(
            nationalityframe, text="Spanish", variable=self.nationality, value=4
        )

        shipframe = ttk.Frame(mainframe)
        sloop = ttk.Radiobutton(shipframe, text="sloop", variable=self.ship, value=1)
        fluyt = ttk.Radiobutton(shipframe, text="Flyut", variable=self.ship, value=2)
        frigate = ttk.Radiobutton(
            shipframe, text="frigate", variable=self.ship, value=3
        )
        next = ttk.Button(mainframe, text="Next", command=self.check)
        name_entry = ttk.Entry(mainframe, width=7, textvariable=self.name)
        name = ttk.Label(mainframe, text="name:")
        nationality = ttk.Label(mainframe, text="nationality:")
        ship = ttk.Label(mainframe, text="ship:")
        isok = ttk.Label(mainframe, textvariable=self.isok_text)

        # elements' placement:
        name.grid(column=1, row=1, sticky=(W, E))
        name_entry.grid(column=2, row=1, sticky=(W, E))
        nationality.grid(column=1, row=2, sticky=(W, E))
        nationalityframe.grid(column=2, row=2, sticky=(W, E))
        ship.grid(column=1, row=3, sticky=(W, E))
        shipframe.grid(column=2, row=3, sticky=(N, S, W, E))
        isok.grid(column=1, row=4, sticky=(W, E))
        next.grid(column=2, row=4, sticky=(W, E))

        # ship frame elements' placement:
        sloop.grid(column=1, row=0, sticky=(W))
        fluyt.grid(column=2, row=0)
        frigate.grid(column=3, row=0, sticky=(E))

        # nationality elements placement:
        french.grid(column=1, row=0)
        english.grid(column=2, row=0)
        dutch.grid(column=3, row=0)
        spanish.grid(column=4, row=0)

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

        nationalityframe.rowconfigure(0, weight=1)
        nationalityframe.columnconfigure(1, weight=1)
        nationalityframe.columnconfigure(2, weight=1)
        nationalityframe.columnconfigure(3, weight=1)
        nationalityframe.columnconfigure(4, weight=1)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in shipframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in nationalityframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        name_entry.focus()
        root.bind("<Return>", self.check)
        self.root = root
        root.wait_window()

    def check(self, *args):
        if self.name.get() == "":
            self.isok_text.set("Name is required")
        elif self.nationality.get() not in [1, 2, 3, 4]:
            self.isok_text.set("Nationality is required")
        elif self.ship.get() not in [1, 2, 3]:
            self.isok_text.set("Ship is required")
        else:
            self.isok_text.set("OK")
            self.root.destroy()
