from tkinter import *


class SetHumanPlayer:
    def __init__(self, master):
        self.master = master
        self.value = None
        master.title("Teeko")

        self.game_info = Label(master, text="Enter the name of the payer", font=("Helvetica", 15), anchor=CENTER)

        self.game_info.grid(row=1, column=0,columnspan=2, pady=(30, 50))

        self.pvp_button = Entry(master, width=25, font=("Roboto", 20))
        self.pvp_button.grid(row=2, column=0, padx=(40,0))

        self.iavia_button = Button(master, text="Valider", command=self.action, width=10,  font=("Roboto", 15), anchor=CENTER)
        self.iavia_button.grid(row=3, column=0, pady=10)

        self.close_button = Button(master, text="Quit", command=self.close,width=10, font=("Roboto", 15), fg="red")
        self.close_button.grid(row=3, column=1, pady=10)

    def action(self):
        print("Choose level {}".format(self.pvp_button.get()))
        self.value = self.pvp_button.get()
        self.master.destroy()

    def close(self):
        self.master.destroy()
        exit()


def set_human_player():
    root = Tk()
    w = 600  # width for the Tk root
    h = 400  # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=0, height=0)
    my_gui = SetHumanPlayer(root)
    root.mainloop()
    return my_gui.value
