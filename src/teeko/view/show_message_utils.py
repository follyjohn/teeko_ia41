from tkinter import *
from tkinter import messagebox
from enum import Enum

class MessageType(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3

def show_message(title: str, message: str, message_type: MessageType):
    root = Tk()
    root.withdraw()
    root.lift()
    if message_type == MessageType.INFO:
        messagebox.showinfo(title, message)
    elif message_type == MessageType.WARNING:
        messagebox.showwarning(title, message)
    elif message_type == MessageType.ERROR:
        messagebox.showerror(title, message)
    root.destroy()


class YesOrNo:
    def __init__(self, master):
        self.master = master
        self.value = None
        master.title("Teeko")

        self.game_info = Label(
            master,
            text="Do you want to change the name of the ai ?",
            font=("Helvetica", 10))

        self.game_info.grid(row=1, column=0, padx = 10, pady = (10, 5))

        self.pvp_button = Button(master,
                                 text="Yes",
                                 command=lambda: self.chose_response(True),
                                 width=10,
                                 padx=10,
                                 pady=10,
                                 font=("Roboto", 10))

        self.pvp_button.grid(row=2, column=0, pady=10)
        
        self.pnp_button = Button(master,
                                 text="No",
                                 command=lambda: self.chose_response(False),
                                 width=10,
                                 padx=10,
                                 pady=10,
                                 font=("Roboto", 10))

        self.pnp_button.grid(row=2, column=1, pady=10)

        # self.iavp_button = Button(master,
        #                           text="Player vs AI",
        #                           command=lambda: self.chose_ia_level(2),
        #                           width=30,
        #                           padx=10,
        #                           pady=10,
        #                           font=("Roboto", 15))

        # self.iavp_button.grid(row=3, column=0, pady=10)



    def chose_response(self, choice: bool):
        # print("Choose level {}".format(choice))
        self.value = choice
        self.master.destroy()

    def close(self):
        self.master.destroy()
        exit()


def close():
    exit()


def yes_or_no():
    root = Tk()
    w = 500 # width for the Tk root
    h = 150  # height for the Tk root
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
    my_gui = YesOrNo(root)
    root.mainloop()
    return my_gui.value

if __name__ == "__main__":
    select_screen()