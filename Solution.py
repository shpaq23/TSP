from tkinter import *

class Solution:
    """
    Solution window pops after the program finish calculations and find "correct" path
    """
    def __init__(self, algoritm_type):
        """
        initializes windows
        :param algoritm_type: 1 if genetic solution, and two windows will pop, 2 if greedy solution and one window will pop
        """

        self.window = Tk()
        if algoritm_type == 1:
            self.path_window = PathWindow(self.window)
            self.window2 = Toplevel(self.window)
            self.plot_window = PlotWindow(self.window2)
        elif algoritm_type == 2:
            self.path_window = PathWindow(self.window)

    def start(self):
        self.window.mainloop()


class PathWindow:
    """
    Window with found path
    """
    def __init__(self, master):
        """
        initializes path window
        :param master: reference to master parent
        """
        self.master = master
        self.master.title("Path")

        self.master.update_idletasks()
        self.master.configure(background="black")
        self.master.resizable(width=False, height=False)

        # Solution image
        self.solution = PhotoImage(file ="path.png")
        Label(self.master, image=self.solution).pack()

class PlotWindow:
    """
    Window with plot
    """
    def __init__(self, master):
        """
        initializes plot window
        :param master: reference to master parent
        """

        self.master = master
        self.master.title("Plot")

        self.master.update_idletasks()
        self.master.configure(background="black")
        self.master.resizable(width=False, height=False)

        # Plot image
        self.plot = PhotoImage(file="plot.png")
        Label(self.master, image=self.plot).pack()





