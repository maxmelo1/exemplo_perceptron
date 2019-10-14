import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, ax):
        self.x = x
        self.y = y
        self.ax = ax

        self.label = 1 if x > y else -1

    def getEntradas(self):
        return [self.x, self.y]

    def setLabel(self, label):
        self.label = label

    def draw(self, color=None):
        if color is None:
            color = 'r' if self.label == 1 else 'g'

        pt = plt.Circle( (self.x,self.y), 1, color=color )

        self.ax.add_artist(pt)
