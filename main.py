from point import Point
import matplotlib.pyplot as plt
import numpy as np
import random
from perceptron import Perceptron

fig, ax = plt.subplots()

def main():


    perc = Perceptron()
    inputs = [-1,2]
    chute = perc.adivinhar(inputs)

    print(chute)

    points = generatePoints()




    x = np.linspace(0, 50, 100)
    plt.plot(x, x)


    for p in points:
        p.draw()




    plt.show()



def generatePoints():
    points = []
    for i in range(50):
        x = int(random.uniform(0,50))
        y = int(random.uniform(0,50))
        points.append(Point(x,y, ax))
    return points


if __name__ == "__main__":
    main()