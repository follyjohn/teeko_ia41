from tkinter import *


class SelectAIGui:
    def __init__(self, master):
        self.master = master
        self.value = None
        master.title("Teeko")

        self.label = Label(master,
                           text="Choose an AI",
                           font=("Helvetica", 17),
                           anchor=CENTER)
        self.label.grid(row=0, column=0, pady=(30, 30))

        self.pvp_button = Button(master,
                                 text="Nada",
                                 command=lambda: self.chose_ia(1),
                                 width=30,
                                 padx=10,
                                 pady=10,
                                 font=("Roboto", 15))
        self.pvp_button.grid(row=2, column=0, pady=10, padx=20)

        self.iavp_button = Button(master,
                                  text="Jasmine",
                                  command=lambda: self.chose_ia(2),
                                  width=30,
                                  padx=10,
                                  pady=10,
                                  font=("Roboto", 15))
        self.iavp_button.grid(row=3, column=0, pady=10)

        self.pvia_button = Button(master,
                                  text="Justine",
                                  command=lambda: self.chose_ia(3),
                                  width=30,
                                  padx=10,
                                  pady=10,
                                  font=("Roboto", 15))
        self.pvia_button.grid(row=4, column=0, pady=10)

        self.iavia_button = Button(master,
                                   text="Yaw",
                                   command=lambda: self.chose_ia(4),
                                   width=30,
                                   padx=10,
                                   pady=10,
                                   font=("Roboto", 15))
        self.iavia_button.grid(row=5, column=0, pady=10)
        
        self.iavia_button = Button(master,
                                   text="Alan",
                                   command=lambda: self.chose_ia(5),
                                   width=30,
                                   padx=10,
                                   pady=10,
                                   font=("Roboto", 15))
        self.iavia_button.grid(row=6, column=0, pady=10)

        self.close_button = Button(master,
                                   text="Quit",
                                   command=self.close,
                                   width=30,
                                   padx=10,
                                   pady=10,
                                   font=("Roboto", 15),
                                   fg="red")
        self.close_button.grid(row=7, column=0, pady=30)

    def chose_ia(self, choice: int):
        print("Choose AI {}".format(choice))
        self.value = choice
        self.master.destroy()

    def close(self):
        self.master.destroy()
        exit()


def select_ai():
    root = Tk()
    w = 404  # width for the Tk root
    h = 604  # height for the Tk root
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
    my_gui = SelectAIGui(root)
    root.mainloop()
    return my_gui.value


if __name__ == '__main__':
    select_ai()