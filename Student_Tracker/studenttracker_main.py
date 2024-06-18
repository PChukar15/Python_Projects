#
# Python Ver:   3.12
#
# Author:       Emmett Espinosa
#
# Purpose:      Student Tracker project
#

from tkinter import *
import tkinter as tk

# gives access to other modules
import studenttracker_func
import studenttracker_gui


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 360)
        self.master.maxsize(500, 360)
        # This CenterWindow method will center our app on the user's screen
        studenttracker_func.center_window(self, 500, 300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracker_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clean
        studenttracker_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
