from tkinter import *

from StartWindow import StartWindow
from LoadingFromFile import Loading
from TSPWindow import TSPWindow
from ParametersWindow import ParametersWindow
from PlotWindow import PlotWindow
from Solution import Solution



class Main:
    """
    Main class of program
    All another classes are connected in here
    """
    def __init__(self):
        """
        creates and initializes objects
        """
        self.start_window = StartWindow()
        self.loading = ''
        self.tsp_window = ''
        self.parameters_window = ''
        self.plotWindow = 0
        self.path_distances = []
        self.avg_distances = []
        self.solution = ''
        self.algorithm_type = 0 # if 1 Genetic if 2 Greedy



    def run(self):
        """
        The hearth of the program
        All another class are starting with correct order from here
        :return: nothing
        """
        self.start_window.start()
        if self.start_window.filename == 0:
            self.quit_app("No file selected")
        self.loading = Loading(self.start_window.filename)
        self.algorithm_type = self.start_window.checkvar.get()
        del self.start_window
        if self.loading.open_file() == False:
            self.quit_app("Corrupted file")
        if self.loading.scale() == False:
            self.quit_app("Something went wrong with the reading from the file")
        self.tsp_window = TSPWindow(self.loading.node_coord_section, self.loading.scale_x, self.loading.scale_y, self.algorithm_type)
        #Genetic solution#
        if self.algorithm_type == 1:
            self.parameters_window = ParametersWindow()
            self.parameters_window.start()
            if self.parameters_window.population_size == 0:
                self.quit_app("No parameters selected")
            self.tsp_window.algorithm.set_parameters(self.parameters_window.population_size, self.parameters_window.probability_crossover, self.parameters_window.probability_mutation,
                                                     self.parameters_window.number_generations, self.parameters_window.elitism_strategy_option, self.parameters_window.population_init_option,
                                                     self.parameters_window.select_option, self.parameters_window.tournament_size, self.parameters_window.seed_option, self.parameters_window.seed_value)

            del self.parameters_window

            self.path_distances = self.tsp_window.start()
            self.avg_distances = self.tsp_window.avg_distance


            if self.path_distances != False:
                # Plot
                self.plotWindow = PlotWindow(self.path_distances, self.avg_distances)
                # self.plotWindow.start()

                # Solution
                self.solution = Solution(self.algorithm_type)
                self.solution.start()

        #Greedy solution#
        elif self.algorithm_type == 2:
            self.tsp_window.start()

            self.solution = Solution(self.algorithm_type)
            self.solution.start()


    def quit_app(self, statement):
        """
        Quiting the app immediately when error occurs
        :param statement: Error message
        :return: nothing
        """
        sys.exit(statement)



m = Main()
m.run()





