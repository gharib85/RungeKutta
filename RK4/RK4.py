import numpy as np
import matplotlib.pyplot as plt


class RK4(object):
    """"
    Implementation of the method of Runge Kutta of fourth order, to obtain the value of a differential equation given
    its initial conditions, obtain its graph and its table of values.
    The function receives equations of the form dy / dt = f(t,y)
    Example:
        def(t, y):
            return 2*t -3*y + 1
        y = RK4(f)
        ► To get the solution given the initial conditions
        ti = 1
        yi = 5
        done = 1.5
        h = 0.1
        y.solve(ti, yi, done, h)
        ► To obtain the graph
        y.graph('r--', label = "Function y"
        ► To get the table of values
        y.table(lw = 2)
    """

    def __init__(self, function):
        """
        :param function: Function to solve
        """
        self.ts = []
        self.ys = []
        self.f = function

    def solve(self, ti, yi, done, h):
        """
        Initialize the ODE solution given the initial values
        :param ti: Value of the initial t
        :param yi: Value of the initial y
        :param done: Value that you want to evaluate in the equation
        :param h: Integration step
        :return: Value of the equation
        """
        st = np.arange(ti, done, h)

        for _ in st:
            K1 = self.f(ti, yi)
            K2 = self.f(ti + h / 2, yi + K1 * h / 2)
            K3 = self.f(ti + h / 2, yi + K2 * h / 2)
            K4 = self.f(ti + h, yi + K3 * h)

            yi += (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
            self.ys.append(yi)

            ti += h
            self.ts.append(ti)
        return yi

    def graph(self, *args, **kwargs):
        """
        Graph the function with the values obtained from each iteration
        :param args:
        :param kwargs:
        :return:
        """
        plt.title("Graph of the function")
        plt.plot(self.ts, self.ys, *args, **kwargs)
        plt.legend()
        plt.grid()
        plt.xlabel("$ t $")
        plt.ylabel("$ y(t) $")

    def table(self):
        """
        Show the obtained table of the values of each iteration
        :param:
        :return: Table of values
        """
        data = []
        for i in range(len(self.ts)):
            data.append([self.ts[i], self.ys[i]])

        color = plt.cm.GnBu(np.linspace(1, len(data)))
        colLab = ('t', 'y')
        plt.table(cellText=data, cellColours=None,
                  cellLoc='center', colWidths=None,
                  rowLabels=None, rowColours=None, rowLoc='center',
                  colLabels=colLab, colColours=color, colLoc='center',
                  loc='center', bbox=None)

        ax = plt.gca()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.title("Value table")
        plt.show()