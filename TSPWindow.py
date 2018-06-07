import pygame, random
from Algorithm import Algorithm


class TSPWindow:
    """
    Pygame window used to drawing paths in "live"
    """
    def __init__(self, cities, scale_x, scale_y, algorithm_type):
        """
        initializes objects
        :param cities: cities
        :param scale_x: scale x to draw cities with scale
        :param scale_y: scale y to draw cities with scale
        :param algorithm_type: algorithm type, if 1 - Genetic, if 2 - Greedy
        """

        #RESOLUTION#
        self.res = (1400,800)
        #SCREEN#
        self.screen = ''
        #ALGORITHM#
        self.algorithm = Algorithm(cities)
        #SCALES#
        self.scale_x = scale_x
        self.scale_y = scale_y
        #CITY SIZE#
        self.size = 8
        #BACKGROUND#
        self.bg = ''
        #PathDistances#
        self.path_distances =[]
        #Type of Algorithm#
        self.algorithm_type = algorithm_type
        #AVG distance of population in generations#
        self.avg_distance = []
        #distance and number of population
        self.ver = ""

    def start(self):
        """
        Showing pygame window
        This window is drawing cities and paths in "live"
        :return:  path distances of all paths in genetic solution, or false when user will close the app before it stop computing
        """
        # COLORS#
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)

        myfont = pygame.font.SysFont("monospace", 20)
        myfont.set_bold(True)

        for a in range(0, len(self.algorithm.cities)):
            #DRAWING CITIES#
            x = 100 + self.algorithm.cities[a].x * self.scale_x
            y = 770 - self.algorithm.cities[a].y * self.scale_y
            pygame.draw.ellipse(self.screen, GREEN, (x, y, self.size, self.size))
            pygame.time.delay(12)
            pygame.display.flip()
            #DRAWING LABELS#
            #label = myfont.render(str(self.algorithm.cities[a].ID), 1, YELLOW)
            #self.screen.blit(label, (x-self.size/2+1, y+self.size/2+1))

        pygame.image.save(self.screen, "cities.png")
        self.bg = pygame.image.load("cities.png")

        #GENETIC SOLUTION#
        if self.algorithm_type == 1:
            population = []
            if self.algorithm.population_init_option == 1:
                for a in range(0, len(self.algorithm.cities)):
                    #half of population#
                    #if len(population) == int(self.algorithm.population_size/2):
                    #all population#
                    if len(population) == int(self.algorithm.population_size):
                        break
                    population.append(self.algorithm.greedy_solution(a+1))
            #################################
            x = 0
            while len(population) < self.algorithm.population_size:
                ver = random.sample(range(1, len(self.algorithm.cities) + 1), len(self.algorithm.cities))
                if ver in population:
                    pass
                else:
                    population.append(ver)
                x = x + 1
            ###################################

            running = 1
            length = 0

            while running:
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    running = 0

                if length < self.algorithm.number_generations:
                    population = self.algorithm.genetic_solution(population)
                    self.avg_distance.append(self.algorithm.get_average_distance_path(population))
                    self.algorithm.path = self.algorithm.get_shortest_path(population)
                    self.algorithm.set_up_edges()
                    self.draw_edges(0)
                    self.draw_total_distance(length+1)
                    length = length + 1
                    if length == self.algorithm.number_generations:
                        myfont = pygame.font.SysFont("monospace", 15)
                        myfont.set_bold(True)

                        ver2 = str("Probability of mutation: ") + str(self.algorithm.probability_mutation)
                        ver3 = str("Probability of crossover: ") + str(self.algorithm.probability_crossover)
                        ver4 = str("Population size: ") + str(self.algorithm.population_size)
                        ver5 = ""
                        ver6 = ""
                        ver7 = ""
                        ver8 = ""
                        if self.algorithm.population_init_option == 0:
                            ver7 = str("Greedy algorithm init population: DISABLED")
                        elif self.algorithm.population_init_option == 1:
                            ver7 = str("Greedy algorithm init population: ENABLES")
                        if self.algorithm.elitism_strategy_option == 0:
                            ver5 = str("Upgraded elitism strategy: DISABLED")
                        elif self.algorithm.elitism_strategy_option == 1:
                            ver5 = str("Upgraded elitism strategy: ENABLED")
                        if self.algorithm.select_option == 1:
                            ver6= str("Roulette wheel selection")
                        elif self.algorithm.select_option == 2:
                            ver6= str("Tournament selection" + "["+str(self.algorithm.tournament_size)+"]")
                        if self.algorithm.seed_option ==1:
                            ver8= str("Random seed" + "[" + str(self.algorithm.seed_value)+"]")
                        elif self.algorithm.seed_option == 2:
                            ver8 = str("Selected seed: " + str(self.algorithm.seed_value))

                        label2 = myfont.render(ver2, 1, YELLOW)
                        label3 = myfont.render(ver3, 1, YELLOW)
                        label4 = myfont.render(ver4, 1, YELLOW)
                        label5 = myfont.render(ver5, 1, YELLOW)
                        label6 = myfont.render(ver6, 1, YELLOW)
                        label7 = myfont.render(ver7, 1, YELLOW)
                        label8 = myfont.render(ver8, 1, YELLOW)
                        self.screen.blit(label2, (0, 20))
                        self.screen.blit(label3, (0, 35))
                        self.screen.blit(label4, (0, 50))
                        self.screen.blit(label7, (0, 65))
                        self.screen.blit(label6, (0, 80))
                        self.screen.blit(label5, (0, 95))
                        self.screen.blit(label8, (0, 110))
                        try:
                            file = open("options.txt", "w")
                            file.write(self.ver+"\n")
                            file.write(ver2+"\n")
                            file.write(ver3+"\n")
                            file.write(ver4+"\n")
                            file.write(ver5+"\n")
                            file.write(ver6+"\n")
                            file.write(ver7+"\n")
                            file.write(ver8+"\n")
                            file.close()
                            file = open("best path.txt", "w")
                            for a in range(0, len(self.algorithm.path)):
                                if a < len(self.algorithm.path) - 1:
                                    file.write(str(self.algorithm.path[a])+"-")
                                else:
                                    file.write(str(self.algorithm.path[a]))
                            file.close()
                        except:
                            print("Error occured")
                        pygame.display.flip()
                        pygame.image.save(self.screen, "path.png")
                        pygame.quit()
                        return self.path_distances


                    self.screen.fill(BLACK)
                    self.screen.blit(self.bg, (0, 0))
        #GREEDY SOLUTION#
        elif self.algorithm_type == 2:
            while True:
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    break
                self.algorithm.path = random.sample(range(1, len(self.algorithm.cities) + 1), len(self.algorithm.cities))
                self.algorithm.set_up_edges()
                self.draw_edges(30)
                self.draw_total_distance(0)
                pygame.time.delay(2000)
                self.screen.fill(BLACK)
                self.screen.blit(self.bg, (0, 0))
                time = self.algorithm.greedy_solution(1)
                self.draw_edges(100)
                self.draw_total_distance(100)

                myfont = pygame.font.SysFont("monospace", 20)
                myfont.set_bold(True)

                ver2 = str("GREEDY SOLUTION")
                ver3 = str("SOLVED IN: ") + str(round(time,3)) + " SECONDS"
                label2 = myfont.render(ver2, 1, YELLOW)
                label3 = myfont.render(ver3, 1, YELLOW)

                self.screen.blit(label2, (0, 20))
                self.screen.blit(label3, (0, 40))

                pygame.display.flip()
                pygame.image.save(self.screen, "path.png")
                break

        pygame.quit()
        return False


    def start2(self):
        """
        Used only for testing
        :return: nothing
        """
        self.algorithm.genetic_solution()

    def draw_edges(self, delay):
        """
        Drawing the edges in window
        :param delay: delay of edges drawing
        :return: nothing
        """
        WHITE = (255, 255, 255)
        for a in range(0, len(self.algorithm.edges)):
            #DRAWING EDGES#
            x1 = 100 + self.algorithm.edges[a].x1 * self.scale_x
            y1 = 770 - self.algorithm.edges[a].y1 * self.scale_y

            x2 = 100 + self.algorithm.edges[a].x2 * self.scale_x
            y2 = 770 - self.algorithm.edges[a].y2 * self.scale_y

            pygame.draw.line(self.screen, WHITE, (x1+self.size/2, y1+self.size/2), (x2+self.size/2, y2+self.size/2), 1)
            pygame.time.delay(delay)
            pygame.display.flip()

    def draw_total_distance(self, gen):
        """
        drawing a total distance and if genetic solution was choosen number of generations
        :param gen: generation in genetic solution
        :return: nothing
        """
        self.algorithm.calculate_total_distance()
        print(self.algorithm.total_distance)
        self.path_distances.append(round(self.algorithm.total_distance))
        YELLOW = (255, 255, 0)
        myfont = pygame.font.SysFont("monospace", 20)
        myfont.set_bold(True)
        if self.algorithm_type == 1:
            self.ver = str("Total distance: ") + str(round(self.algorithm.total_distance,2)) + str(" Generation: ") + str(gen)
        elif self.algorithm_type == 2:
            self.ver = str("Total distance: ") + str(round(self.algorithm.total_distance, 2))
        label = myfont.render(self.ver, 1, YELLOW)

        self.screen.blit(label, (0, 0))

        pygame.display.flip()


