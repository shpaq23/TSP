import unittest
from Algorithm import Algorithm

class TestAlgorithm(unittest.TestCase):



    def test_distance_calculate(self):
        cities =[[1,1],[1,3],[3,3],[3,1]]
        algorithm = Algorithm(cities)

        algorithm.path = [1,2,3,4]
        algorithm.set_up_edges()
        algorithm.calculate_total_distance()
        self.assertEqual(algorithm.total_distance, 8)

    def test_shortest_path_calculation(self):
        cities = [[1, 1], [1, 3], [3, 3], [3, 1]]
        algorithm = Algorithm(cities)
        population = [[1,2,3,4],[1,3,2,4],[1,4,2,3]]
        shortest = algorithm.get_shortest_path(population)
        self.assertEqual(shortest, [1,2,3,4])

    def test_average_distance_path_calculation(self):
        cities = [[1, 1], [1, 3], [3, 3], [3, 1]]
        algorithm = Algorithm(cities)
        population = [[1, 2, 3, 4], [1, 3, 2, 4], [1, 4, 2, 3]] #distance [8, 9,65... , 9,65...]
        average = algorithm.get_average_distance_path(population)
        self.assertEqual(average, 9)






