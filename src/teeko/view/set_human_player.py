from tkinter import *


class SetHumanPlayer:
    def __init__(self, master, desc: str):
        self.master = master
        self.value = None
        self.desc = desc
        master.title("Teeko")

        # frame = Frame(master, width=366, height=459).place(x=70, y=0)
        # frame.grid(row=0, column=0, pady=(20, 50))

        self.game_info = Label(master, text=self.desc, font=("Helvetica", 15))
        self.game_info.grid(row=0,
                            column=0,
                            columnspan=2,
                            pady=(30, 30),
                            padx=20)

        self.pvp_button = Entry(master, width=25, font=("Roboto", 20))
        self.pvp_button.grid(row=1, column=0, columnspan=2, padx=(35, 0))

        self.iavia_button = Button(master,
                                   text="Valider",
                                   command=self.action,
                                   width=10,
                                   padx=10,
                                   font=("Roboto", 15),
                                   anchor=CENTER)
        self.iavia_button.grid(row=2, column=0, pady=30, padx=(30, 0))

        self.close_button = Button(master,
                                   text="Quit",
                                   command=self.close,
                                   width=10,
                                   padx=10,
                                   font=("Roboto", 15),
                                   fg="red")
        self.close_button.grid(row=2, column=1, pady=30)

    def action(self):
        print("Choose level {}".format(self.pvp_button.get()))
        self.value = self.pvp_button.get()
        self.master.destroy()

    def close(self):
        self.master.destroy()
        exit()


def close():
    exit()


def set_human_player(desc: str):
    root = Tk()
    w = 450  # width for the Tk root
    h = 300  # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=0, height=0)
    root.protocol('WM_DELETE_WINDOW', close)
    my_gui = SetHumanPlayer(root, desc)
    root.mainloop()
    return my_gui.value


if __name__ == "__main__":
    set_human_player("Choose level")