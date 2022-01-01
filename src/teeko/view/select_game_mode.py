from tkinter import *


class SelectLevel:
    def __init__(self, master):
        self.master = master
        self.value = None
        master.title("Teeko")

        self.label = Label(master,
                           text="Welcome to Teeko!",
                           font=("Helvetica", 27))
        self.label.grid(row=0, column=0, padx=20)

        self.game_info = Label(master,
                               text="Choose game mode",
                               font=("Helvetica", 15))

        self.game_info.grid(row=1, column=0, padx=20, pady=(30, 50))

        self.pvp_button = Button(master,
                                 text="Player vs Player",
                                 command=lambda: self.chose_ia_level(1),
                                 width=30,
                                 padx=10,
                                 pady=10,
                                 font=("Roboto", 15))

        self.pvp_button.grid(row=2, column=0, pady=10, padx=20)

        self.iavp_button = Button(master,
                                  text="Player vs AI",
                                  command=lambda: self.chose_ia_level(2),
                                  width=30,
                                  padx=10,
                                  pady=10,
                                  font=("Roboto", 15))

        self.iavp_button.grid(row=3, column=0, pady=10)

        self.pvia_button = Button(master,
                                  text="AI vs Player",
                                  command=lambda: self.chose_ia_level(3),
                                  width=30,
                                  padx=10,
                                  pady=10,
                                  font=("Roboto", 15))
        self.pvia_button.grid(row=4, column=0, pady=10)

        self.iavia_button = Button(master,
                                   text="AI vs AI",
                                   command=lambda: self.chose_ia_level(4),
                                   width=30,
                                   padx=10,
                                   pady=10,
                                   font=("Roboto", 15))
        self.iavia_button.grid(row=5, column=0, pady=10)

        self.close_button = Button(master,
                                   text="Quit",
                                   command=self.close,
                                   width=30,
                                   padx=10,
                                   pady=10,
                                   font=("Roboto", 15),
                                   fg="red")
        self.close_button.grid(row=6, column=0, pady=10)

    def chose_ia_level(self, choice: int):
        print("Choose level {}".format(choice))
        self.value = choice
        self.master.destroy()

    def close(self):
        self.master.destroy()
        exit()


def close():
    exit()


def select_screen():
    root = Tk()
    w = 404  # width for the Tk root
    h = 704  # height for the Tk root
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
    my_gui = SelectLevel(root)
    root.mainloop()
    return my_gui.value
