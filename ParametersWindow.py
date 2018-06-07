from tkinter import messagebox
from tkinter import *


class ParametersWindow():
    """
    Class responsible for the window with parameters in genetic solution
    """
    def __init__(self):
        """
        creates and initializes objects
        """
        self.filename = ""
        #Window#
        self.window = Tk()
        self.window.title("Genetic solution")
        self.window.update_idletasks()
        x = 340
        y = 330
        w = (self.window.winfo_screenwidth() // 2 ) - (x // 2)
        h = (self.window.winfo_screenheight() // 2) - (y // 2)
        self.window.geometry('{}x{}+{}+{}'.format(x,y,w,h))
        self.window.configure(background = "black")
        self.window.resizable(width=False, height=False)
        self.text = []
        self.entry = Entry()   # selection option entry
        self.entry2 = Entry()  # Seed option entry
        self.population_size = 0
        self.probability_crossover = 0.0
        self.probability_mutation = 0.0
        self.number_generations = 0
        self.elitism_strategy_option = 0 # if 0 normal selection if 1 by the best
        self.population_init_option = 0  # if 0 normal if 1 starting population initialization by greedy solutions
        self.select_option = 0 # if 1 roulette wheel selection if 2 tournament selection
        self.seed_option = 0 # if 1 random seed if 2 my seed
        self.seed_value = 0
        self.tournament_size = 0
        self.checkvar1 = IntVar()  # offspring selected option
        self.checkvar2 = IntVar()  # population init option
        self.checkvar4 = IntVar()  # tournament or rulette wheel selection option
        self.checkvar5 = IntVar()  # my seed or random seed option
        #Frames#
        topFrame = Frame(self.window, bg= "black")
        topFrame.pack(side = TOP)
        frame = []
        for a in range(0, 4):
            frame.append(Frame(self.window, bg="black"))

        botFrame = Frame(self.window, bg= "black")
        botFrame.pack(side = BOTTOM)
        #Labels & textfields#
        Label(topFrame,
              text = "Partameters",
              fg = "Gray",
              bg = "black",
              font = "Helvetica 15 bold italic").pack(side = TOP, pady = 4)
        Label(frame[0],
              text="Population size: ",
              fg="Gray",
              bg="black",
              font="Helvetica 12 bold italic").pack(side=LEFT, padx = 5, pady = 5)
        self.text.append(Text(frame[0],
                              height = 1,
                              width = 10,
                              bg = "black",
                              fg = "Gray",
                              insertbackground = "White",
                              bd = 1, ))

        Label(frame[1],
              text="Probability of crossover: ",
              fg="Gray",
              bg="black",
              font="Helvetica 12 bold italic").pack(side=LEFT, padx=5, pady=5)
        self.text.append(Text(frame[1],
                              height=1,
                              width=10,
                              bg="black",
                              fg="Gray",
                              insertbackground="White",
                              bd=1,
                              ))


        Label(frame[2],
              text="Probability of mutation: ",
              fg="Gray",
              bg="black",
              font="Helvetica 12 bold italic").pack(side=LEFT, padx=5, pady=5)
        self.text.append(Text(frame[2],
                              height=1,
                              width=10,
                              bg="black",
                              fg="Gray",
                              insertbackground="White",
                              bd=1,
                              ))

        Label(frame[3],
              text="Number of generations: ",
              fg="Gray",
              bg="black",
              font="Helvetica 12 bold italic").pack(side=LEFT, padx=5, pady=5)
        self.text.append(Text(frame[3],
                              height=1,
                              width=10,
                              bg="black",
                              fg="Gray",
                              insertbackground="White",
                              bd=1,
                              ))

        for a in range(0, len(self.text)):
            self.text[a].pack(side=LEFT, padx=5, pady=5)
            frame[a].pack(fill = X)

        self.text[0].insert(INSERT, "60")
        self.text[1].insert(INSERT, "0.75")
        self.text[2].insert(INSERT, "0.35")
        self.text[3].insert(INSERT, "200")

        radioFrame = Frame(botFrame, bg="black")
        radioFrame.pack()
        # RadioButtons#
        #selection option #
        R1 = Radiobutton(radioFrame,
                         text="Roulette selection",
                         fg="Gray",
                         bg="Black",
                         activebackground="red",
                         font="Arial 9 bold",
                         variable=self.checkvar4,
                         value=1,
                         )
        R1.pack(side=LEFT, padx=5, pady=2)
        R1.select()
        Radiobutton(radioFrame,
                    text="Tournament selection",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 9 bold",
                    variable=self.checkvar4,
                    value=2
                    ).pack(side = LEFT, padx = 5, pady = 2)
        self.entry = Entry(radioFrame,
              width=4,
              bg="black",
              fg="Gray",
              insertbackground="White",
              bd=1
              )
        self.entry.pack()
        #seed option#
        radioFrame2 = Frame(botFrame, bg="black")
        radioFrame2.pack()
        R2 = Radiobutton(radioFrame2,
                         text="Random seed",
                         fg="Gray",
                         bg="Black",
                         activebackground="red",
                         font="Arial 9 bold",
                         variable=self.checkvar5,
                         value=1,
                         )
        R2.pack(side=LEFT, padx=5, pady=2)
        R2.select()
        Radiobutton(radioFrame2,
                    text="My seed",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 9 bold",
                    variable=self.checkvar5,
                    value=2
                    ).pack(side=LEFT, padx=5, pady=2)
        self.entry2 = Entry(radioFrame2,
                           width=6,
                           bg="black",
                           fg="Gray",
                           insertbackground="White",
                           bd=1
                           )
        self.entry2.pack()

        #Buttons#
        Checkbutton(botFrame,
                    text="Upgraded elitism strategy",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 9 bold",
                    variable= self.checkvar1,
                    onvalue=1,
                    offvalue=0
                    ).pack()
        Checkbutton(botFrame,
                    text="Starting population init by greedy algorithm",
                    fg="Gray",
                    bg="Black",
                    activebackground="red",
                    font="Arial 9 bold",
                    variable=self.checkvar2,
                    onvalue=1,
                    offvalue=0
                    ).pack()
        Button(botFrame,
               text = " ACCEPT ",
               fg = "Gray",
               bg = "Black",
               font="Arial 12 bold",
               activebackground = "red",
               borderwidth = 0,
               command = self.get_parameters).pack(pady = 10 )

    def get_parameters(self):
        """
        Function that gets parameters when the button is clicked
        :return: nothing
        """
        try:
            self.population_size = int(self.text[0].get("1.0", END))
            self.probability_crossover = float(self.text[1].get("1.0", END))
            self.probability_mutation = float(self.text[2].get("1.0", END))
            self.number_generations = int(self.text[3].get("1.0", END))
            self.elitism_strategy_option = self.checkvar1.get()
            self.population_init_option = self.checkvar2.get()
            self.select_option = self.checkvar4.get()
            self.seed_option = self.checkvar5.get()
            if self.select_option == 2:
                if int(self.entry.get()) > self.population_size:
                    raise ValueError()
                else:
                    self.tournament_size = int(self.entry.get())

            if self.seed_option == 2:
                if int(self.entry2.get()) > pow(2,15):
                    raise ValueError()
                else:
                    self.seed_value = int(self.entry2.get())
            self.window.destroy()
        except:
            self.population_size = 0
            messagebox._show('Error', 'Wrong parameters')

    def start(self):
        """
        Starting the parameters window
        :return: nothing
        """
        self.window.mainloop()
