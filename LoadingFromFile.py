
class Loading:
    """
    Class responsible for loading data from file
    """
    def __init__(self, filename):
        """
        creates and initializes objects
        :param filename: name of data file to take
        """
        self.name = ""
        self.comment = ""
        self.type = ""
        self.dimension = 0
        self.edge_weight_type = ""
        self.node_coord_section = []
        self.filename = filename
        self.scale_x = 0.0
        self.scale_y = 0.0
    def open_file(self):
        """
        Reading data from file
        :return: True if file readed False otherwise
        """
        try:
            file = open(self.filename, "r")
            ver = 0
            for line in file:
                if line == "EOF\n":
                    break
                if ver == 5:
                    ver = ver + 1
                    continue
                if ver < 5 :
                    splited = line.split(":")
                    splited[1] = splited[1][:-1]
                    if ver == 0:
                        self.name = splited[1]
                    if ver == 1:
                        self.comment = splited[1]
                    if ver == 2:
                        self.type = splited[1]
                    if ver == 3:
                        self.dimension = splited[1]
                    if ver == 4:
                        self.edge_weight_type = splited[1]
                    ver = ver + 1
                else:
                    splited = line.split()
                    ver2 = []
                    ver2.append(float(splited[1]))
                    ver2.append(float(splited[2]))
                    self.node_coord_section.append(ver2)

            return True
        except:
            print("Error")
            return False
    def print_nodes(self):
        """
        Printing to console readed cities and their coordinates
        :return: nothing
        """
        for a in range(0, len(self.node_coord_section)):
            print(a+1, self.node_coord_section[a])
    def scale(self):
        """
        Counting the scale for cities to draw them in another class
        :return: True if scale was counting properly False otherwise
        """
        try:
            max_x = self.node_coord_section[0][0]
            max_y = self.node_coord_section[0][1]

            for a in range(0, len(self.node_coord_section)):
                if max_x < self.node_coord_section[a][0]:
                    max_x = self.node_coord_section[a][0]
                if max_y < self.node_coord_section[a][1]:
                    max_y = self.node_coord_section[a][1]

            # print(max_x, max_y)
            self.scale_x = 1200/max_x
            self.scale_y = 676/max_y

            # print(self.scale_x, self.scale_y)
            return True
        except:
            #print("something went wrong with the reading from the file")
            return False



