import matplotlib.pyplot as plt


class Plotter:

    def __init__(self, x, y, title, xlabel, ylabel):
        # themes: Solarize_Light2, dark_background, bmh, seaborn, seaborn-whitegrid
        self.fig = None
        self.ax = None
        self.x = x
        self.y = y
        self.theme = 'seaborn-whitegrid'
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.titleSize = 17
        self.labelSize = 14
        self.tickSize = 13
        self.xmin = 0
        self.ymin = 0
        self.figSize = [10, 6]
        self.lineWidth = 2
        self.xmax = None

    def build_plot(self, limits=False):
        plt.style.use(self.theme)
        plt.rcParams['figure.figsize'] = self.figSize
        plt.rcParams['lines.linewidth'] = self.lineWidth
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.set_title(self.title, size=self.titleSize)
        self.ax.set_xlabel(self.xlabel, size=self.labelSize)
        self.ax.set_ylabel(self.ylabel, size=self.labelSize)
        self.ax.tick_params(axis='x', labelsize=self.tickSize)
        self.ax.tick_params(axis='y', labelsize=self.tickSize)
        self.ax.plot(self.x, self.y)
        self.xmax = self.x[-1]
        self.ax.set_xlim(left=self.xmin)
        if limits == False:
            self.ax.set_ylim(bottom=self.ymin)


def graficar(x, y, title, xlabel, ylabel):
    Plotter(x, y, title, xlabel, ylabel).build_plot()