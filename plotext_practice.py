"""
This module shows how to use plotext library
"""
import plotext as plt


class Plotext:
    """
    Plotext class uses plotext library to display graphs on console
    """
    def __init__(self):
        """
        displays a graph on console
        """
        # plotext exercise
        y = plt.sin(100, 3)
        plt.plot(y)
        plt.plotsize(100, 30)
        plt.title("Plot Example")
        plt.show()
