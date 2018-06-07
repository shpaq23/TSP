import math, random, time

class City:
    """
    City class
    """
    def __init__(self):
        """
        creates and initializes objects
        """
        self.ID = 0
        self.x = 0
        self.y = 0

class Edge:
    """
    Edge class
    """
    def __init__(self):
        """
        creates and initializes objects
        """
        self.ID = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0


class Algorithm:
    """
    Main algorithm class
    """
    def __init__(self, cities):
        """
        creates and initializes objects
        :param cities: cities coordination readed from file
        """
        self.cities = []
        self.edges = []
        self.total_distance = 0
        self.path = []
        self.population_size = 0
        self.probability_crossover = 0.0
        self.probability_mutation = 0.0
        self.number_generations = 0
        self.elitism_strategy_option = 0 # if 0 normal selection if 1 elitism strategy
        self.population_init_option = 0 # if 0 normal if 1 starting population initialization by greedy solutions
        self.select_option = 0  # if 1 roulette wheel selection if 2 tournament selection
        self.seed_option = 0 # if 1 random seed if 2 my seed
        self.best_individual = []
        self.tournament_size = 0
        self.seed_value = 0

        for a in range(0, len(cities)):
            edge = Edge()
            edge.ID = a+1
            city = City()
            city.ID = a+1
            city.x = cities[a][0]
            city.y = cities[a][1]
            self.cities.append(city)
            self.edges.append(edge)

    def greedy_solution(self, start_city):
        """
        Greedy solution of TSP
        An algorithm that finds the shortest path for each subsequent city starting from the city 1
        :return: Time deal to solved a problem
        """
        del self.path[:]
        path = []
        path.append(start_city)
        self.path.append(start_city)
        time1 = time.time()
        for a in range(0, len(self.cities)-1):
            ind = []
            dist = []
            for b in range(0, len(self.cities)):
                if (b+1) not in path:
                    dist.append(math.sqrt(
                        math.pow((self.cities[b].x - self.cities[path[a]-1].x), 2) + math.pow(
                            (self.cities[b].y - self.cities[path[a]-1].y), 2)))
                    ind.append(b+1)


            path.append(ind[dist.index(min(dist))])
        if self.population_init_option == 1:
            return path
        self.path = path
        time2 = time.time()
        self.set_up_edges()
        total_time = (time2-time1)
        return total_time

    def set_up_edges(self):
        """
        Setting up edges and connecting cities by using path list
        Counting edge distances / path from city to city /
        :return: nothing
        """
        for a in range(0, len(self.path)):
            # OUT CITY#
            self.edges[a].out_city = self.path[a]
            self.edges[a].x1 = self.cities[self.path[a] - 1].x
            self.edges[a].y1 = self.cities[self.path[a] - 1].y

            # IN CITY#
            if a < len(self.path) - 1:
                self.edges[a].in_city = self.path[a + 1]
                self.edges[a].x2 = self.cities[self.path[a + 1] - 1].x
                self.edges[a].y2 = self.cities[self.path[a + 1] - 1].y
            elif a == len(self.path) - 1:
                self.edges[a].in_city = self.path[0]
                self.edges[a].x2 = self.cities[self.path[0] - 1].x
                self.edges[a].y2 = self.cities[self.path[0] - 1].y

            # EDGE DISTANCE#
            self.edges[a].distance = math.sqrt(
                math.pow((self.edges[a].x2 - self.edges[a].x1), 2) + math.pow(
                    (self.edges[a].y2 - self.edges[a].y1), 2))
            #print(a + 1, self.edges[a].distance)

    def calculate_total_distance(self):
        """
        calculating total distance in path
        :return: nothing
        """
        self.total_distance = 0
        for a in range(0, len(self.edges)):
            self.total_distance = self.total_distance + self.edges[a].distance

    def set_parameters(self, population_size, probability_crossover, probability_mutation, number_generations, elitism_strategy_option, populaion_init_option,\
                select_option, tournament_size, seed_option, seed_value):
        """
        Parameters are given by user via tkinter window,
        Setting parameters in algorithm class
        :param population_size: population size
        :param probability_crossover: probability of crossover
        :param probability_mutation: probability of mutation
        :param number_generations: number of generations
        :param offspring_selected_option: Offspring selected option, offsprings can be selected normally, or selected by only the best of them will survive
        :return: nothing
        """
        self.population_size = population_size
        self.probability_crossover = probability_crossover
        self.probability_mutation = probability_mutation
        self.number_generations = number_generations
        self.elitism_strategy_option = elitism_strategy_option
        self.population_init_option = populaion_init_option
        self.select_option = select_option
        self.tournament_size = tournament_size
        self.seed_option = seed_option
        self.seed_value = seed_value

        if seed_option == 1:
            self.seed_value = random.randint(0, pow(2,15))

        random.seed(self.seed_value)







    def genetic_solution(self, population):
        """
        Genetic solution written in 5 steps
        #Step1 - fitness function
        #Step2 - selecting population by rulette wheel
        #Step3 - doing a OX crossover operation
        #Step4 - doing a inversion mutation
        #Step5 - choosing offsprings to replace parents
        :param population: Previous population
        :return: population after 1 generation
        """



        selection = 0
        # Setp 1
        fitness = self.fitness_fun(population, "fitness")
        if self.select_option == 1:
            # Step 2
            selection = self.rulette_wheel_selection(fitness, population)
        elif self.select_option == 2:
            #2
            selection = self.tournament_selection(fitness, population, self.tournament_size)
        #Step 3
        offspring = self.OX_crossover(selection)
        #Step 4
        offspring = self.inversion_mutation(offspring)
        #Step 5
        ########## CLASSIC ##########
        if self.elitism_strategy_option == 0:
            for a in range(0, len(offspring)):
                population[fitness.index(min(fitness))] = offspring[a]
                fitness[fitness.index(min(fitness))] = 100

        ######### Upgraded elitism strategy #############
        elif self.elitism_strategy_option == 1:
            distance_popul = self.fitness_fun(population, "distance")
            distance_offspring = self.fitness_fun(offspring, "distance")
            for a in range(0, len(offspring)):
                if min(distance_offspring) < max(distance_popul):
                    population[distance_popul.index(max(distance_popul))] = offspring[distance_offspring.index(min(distance_offspring))]
                    var = distance_popul[distance_popul.index(max(distance_popul))]
                    distance_popul[distance_popul.index(max(distance_popul))] = min(distance_offspring)
                    distance_offspring[distance_offspring.index(min(distance_offspring))] = var


        return population


    def rulette_wheel_selection(self, fitness, population):
        """
        Selecting new population by rulette wheel,
        :param fitness: fitness of given population
        :param population: population
        :return: new population selected by rulette wheel
        """
        rulette_wheel = []
        rulette_wheel.append(0)
        new_population = []
        if self.elitism_strategy_option == 1:
            new_population.append(population[fitness.index(max(fitness))])
            self.best_individual = new_population[0]
        ver = 0
        for a in range(0, len(fitness)):
            ver = ver + fitness[a]
            rulette_wheel.append(ver)
        for a in range(0, len(fitness)):
            ver = random.randint(0,10000)
            ver = ver / 100
            if len(new_population) == len(population):
                break
            for b in range(0, len(rulette_wheel)-1):
                if ver >rulette_wheel[b] and ver <= rulette_wheel[b+1]:
                    new_population.append(population[b])
                    break

        return new_population

    def tournament_selection(self, fitness, population, tournament_size):
        new_population = []

        if self.elitism_strategy_option == 1:
            new_population.append(population[fitness.index(max(fitness))])
            self.best_individual = new_population[0]
        for a in range(0, len(population)):
            tournaments = random.sample(range(0, len(population)), tournament_size)
            var = []
            max1 = 0.0
            indx = 0
            if len(new_population) == len(population):
                break
            for b in range(0, tournament_size):
                var.append(fitness[tournaments[b]])
                if max1 < var[b]:
                    max1 = var[b]
                    indx = tournaments[b]
            new_population.append(population[indx])


        return new_population



    def OX_crossover(self, population):
        """
        OX crossover operation
        Doing the OX crossover with given probability
        :param population: population
        :return: offsprings
        """
        #Selecting parents randomly
        combinations = random.sample(range(0, len(population)),len(population))
        size = int(len(population)/2)
        parents = []
        ind = 0
        for a in range(0, size):
            ver = []
            ver.append(population[combinations[ind]])
            ver.append(population[combinations[ind+1]])
            parents.append(ver)
            ind = ind+2
        #Checking probability of crossover and place to do a cut
        probability = []
        cut = []

        for a in range(0, size):
            probability.append(random.randint(0,100)/100)
            cut.append(random.sample(range(1, len(population[0])-1), 2))
            cut[a].sort()
            if cut[a][0]+1 == cut[a][1]:
                if cut[a][1] < len(population[0])-2:
                    cut[a][1] = cut[a][1] + 1
                else:
                    cut[a][0] = cut[a][0] - 1
        #Crossovering
        offspring = []
        for a in range(0, size):
            o1 = []
            o2 = []
            p1 = parents[a][0]
            p2 = parents[a][1]
            if probability[a] < self.probability_crossover:
                #Step 1
                for b in range(0, len(p1)):
                    if b >= cut[a][0] and b < cut[a][1]:
                        o1.append(p1[b])
                        o2.append(p2[b])
                    else:
                        o1.append(0)
                        o2.append(0)
                #Setp 2
                chain1 = []
                chain2 = []
                for b in range(cut[a][1], len(p1)):
                    chain1.append(p2[b])
                    chain2.append(p1[b])

                for b in range(0, cut[a][1]):
                    chain1.append(p2[b])
                    chain2.append(p1[b])
                #Setp 3
                for b in range(0, len(p1)):
                    if o1[b] in chain1:
                        chain1.remove(o1[b])
                    if o2[b] in chain2:
                        chain2.remove(o2[b])
                #Step 4
                ind = 0
                for b in range(cut[a][1], len(p1)):
                    o1[b] = chain1[ind]
                    o2[b] = chain2[ind]
                    ind = ind + 1
                for b in range(0, cut[a][0]):
                    o1[b] = chain1[ind]
                    o2[b] = chain2[ind]
                    ind = ind +1
                offspring.append(o1)
                offspring.append(o2)


        return offspring

    def fitness_fun(self, population, option):
        """
        Calculating the fitness for each individual
        Calculating the distance for each individual
        :param population: population
        :param option: given option can be distance or fitness
        :return: fitness or distacne dependent on option
        """
        fitness = []
        value = []
        sume = 0

        for a in range(0, len(population)):
            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0
            distance = 0
            for b in range(0, len(population[a])):
                # OUT CITY#

                x1 = self.cities[population[a][b] - 1].x
                y1 = self.cities[population[a][b] - 1].y

                # IN CITY#
                if b < len(population[a]) - 1:
                    x2 = self.cities[population[a][b + 1] - 1].x
                    y2 = self.cities[population[a][b + 1] - 1].y
                elif b == len(population[a]) - 1:
                    x2 = self.cities[population[a][0] - 1].x
                    y2 = self.cities[population[a][0] - 1].y

                # EDGE DISTANCE#
                distance = distance + math.sqrt(
                    math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
            value.append(distance)
            sume = sume + 1/value[a]
        if option == "fitness":
            for a in range(0, len(population)):
                fitness.append(((1 / value[a]) / sume) * 100)

            return fitness
        elif option == "distance":
            return value

    def inversion_mutation(self, offspring):
        """
        Inversion mutation
        Doing a inversion mutation with given probability on offsprings
        :param offspring: offsprings
        :return: mutated(or not) offsprings
        """
        # Checking probability of mutation and place to do a cut
        probability = []
        cut = []

        for a in range(0, len(offspring)):
            probability.append(random.randint(0, 100) / 100)
            cut.append(random.sample(range(1, len(offspring[0]) - 1), 2))
            cut[a].sort()
            if cut[a][0] + 1 == cut[a][1]:
                if cut[a][1] < len(offspring[0]) - 2:
                    cut[a][1] = cut[a][1] + 1
                else:
                    cut[a][0] = cut[a][0] - 1
        #mutation
        for a in range(0, len(offspring)):
            revers=[]
            x = 0
            if probability[a] < self.probability_mutation:
                #step 1
                for b in range(cut[a][0], cut[a][1]):
                    revers.append(offspring[a][b])
                revers.reverse()
                #step 2
                for b in range(cut[a][0], cut[a][1]):
                    offspring[a][b] = revers[x]
                    x = x+1

        return offspring

    def get_shortest_path(self, population):
        """
        Given the shortest path of population,
        Finding the shortest individual in population
        :param population: population
        :return: shortest path
        """
        fitness = self.fitness_fun(population, "fitness")
        shortest = population[fitness.index(max(fitness))]
        return shortest

    def get_average_distance_path(self, population):
        distances = self.fitness_fun(population, "distance")
        suma = 0
        for a in range(0, len(distances)):
            suma = suma + distances[a]

        suma = round(suma/len(distances))
        return suma














