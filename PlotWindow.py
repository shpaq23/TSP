import matplotlib.pyplot as plt

class PlotWindow:
    """
    Class responsible for drawing a plot/chart
    Can by shown but by default only save the graph in png format
    """
    def __init__(self, path_distance, avg_distance):
        """
        Drawing a plot
        :param path_distance: list that scores all path distances in all generations
        """
        var = []

        for a in range(0, len(path_distance)):
            var.append(a)


        plt.figure(1)
        plt.figure(figsize=(14,7))

        #plot of distance of the best path in generation#

        #2 graphs#
        #plt.plot(var, path_distance, "k,", var, path_distance, "k", )
        #1 grapf#
        plot1= plt.plot(var, path_distance, "k,", var, path_distance, "k")
        plot2 = plt.plot(var, avg_distance, "b,", var, avg_distance, "b")
        plt.legend((plot1[1],plot2[1]), ("best distance", "average distances"))
        plt.ylabel("D I S T A N C E", fontsize = 12)
        plt.xlabel("G E N E R A T I O N", fontsize = 12)
        # reverse graph#
        #plt.axis([0, len(path_distance), max(path_distance) + max(path_distance) * 0.01,
        #         min(path_distance) - max(path_distance) * 0.01])
        # normal graph#

        plt.axis([0, len(avg_distance), min(path_distance) - max(path_distance) * 0.01,max(avg_distance) + max(avg_distance) * 0.01])
        # 2 graphs#
        #plot of avg distance in generation#
        #plt.subplot(212)
        #plt.plot(var, avg_distance, "k,", var, avg_distance, "k")

        #plt.xlabel("GENERATION")
        #plt.ylabel("AVERAGE DISTANCE")
        # reverse graph#
        #plt.axis([0, len(avg_distance), max(avg_distance) + max(avg_distance) * 0.01,
        #         min(avg_distance) - max(avg_distance) * 0.01])
        # normal graph#
        #plt.axis([0, len(avg_distance), min(avg_distance) - max(avg_distance) * 0.01,max(avg_distance) + max(avg_distance) * 0.01])

        plt.savefig("plot.png")
        plt.close("all")





    def start(self):
        """
        To show graph
        :return: nothing
        """
        plt.show()

    def close(self):
        """
        to close graph window
        :return: nothing
        """
        plt.close("all")

