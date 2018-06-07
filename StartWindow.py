from tkinter import filedialog, messagebox
from tkinter import *


class StartWindow():
    """
    Class responsible for the start window
    """

    def __init__(self):
        """
        initializes window
        """
        self.filename = 0
        #Window#
        self.window = Tk()
        self.window.title("TSP")
        self.window.update_idletasks()
        self.checkvar = IntVar()
        x = 640
        y = 480
        w = (self.window.winfo_screenwidth() // 2 ) - (x // 2)
        h = (self.window.winfo_screenheight() // 2) - (y // 2)
        self.window.geometry('{}x{}+{}+{}'.format(x,y,w,h))
        self.window.configure(background = "black")
        self.window.resizable(width=False, height=False)
        #Frames#
        topFrame = Frame(self.window, bg= "black")
        topFrame.pack(side = TOP)


        botFrame = Frame(self.window, bg= "black")
        botFrame.pack(side = BOTTOM)



        #Labels#
        Label(topFrame,
              text = "Travelling Salesman Problem",
              fg = "Gray",
              bg = "black",
              font = "Helvetica 25 bold italic").pack(side = TOP, pady = 4)
        Label(topFrame,
              text="(with genetic and greedy algorithm)",
              fg="Gray",
              bg="black",
              font="Helvetica 17 bold italic").pack(side=TOP)
        Label(topFrame,
              text = "Authors: ",
              fg = "Light Green",
              bg = "black",
              font = "Times 20 italic").pack(pady = 40)

        Label(topFrame,
              text="Michał Szpak",
              fg="Blue",
              bg="black",
              font="Times 15 bold").pack(padx=20)



        Label(botFrame,
              text = "To continue select the options from below: ",
              fg = "Red",
              bg = "black",
              font ="Helvetica 16 bold italic").pack()

        radioFrame = Frame(botFrame, bg="black")
        radioFrame.pack()
        # RadioButtons#
        R1 = Radiobutton(radioFrame,
                    text="Genetic Algorithm",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 11 bold",
                    variable=self.checkvar,
                    value=1,
                    )
        R1.pack(side=LEFT, padx=5, pady=2)
        R1.select()
        Radiobutton(radioFrame,
                    text="Greedy Algorithm",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 11 bold",
                    variable=self.checkvar,
                    value=2,
                    ).pack()
        #Buttons#
        Button(botFrame,
               text = "Load file from directory",
               fg = "Gray",
               bg = "Black",
               font="Arial 10 bold",
               activebackground = "red",
               borderwidth = 0,
               command = self.open_file).pack(pady = 40)

    def open_file(self):
        """
        Searching for correct file to open and read the data from
        By using filedialog
        :return: nothing
        """
        self.window.filename = filedialog.askopenfilename(
            initialdir="/Desktop",
            title="Load cities from file",
            filetypes=(("tsp files", "*.tsp"), ("all files", "*.*"))
        )

        if self.window.filename[-4:] == ".tsp":
            self.filename = self.window.filename
            messagebox._show('Loaded', 'Loaded successfully')
            self.window.destroy()
        else:
            messagebox._show('Error', 'Loaded error')

    def start(self):
        """
        Showing start window
        :return: nothing
        """
        self.window.mainloop()
