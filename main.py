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

    points = gerarPontosAleatorios()



    x = np.linspace(0, 50, 100)
    plt.plot(x, x)


    # for p in points:
    #     #p.draw()
    #     perc.treinar( p.getEntradas(), p.label )
    #
    #     chute = perc.adivinhar(p.getEntradas())
    #
    #     point = Point(p.x, p.y, ax)
    #     point.setLabel(chute)
    #     print( "%d, %d = %d, certo? = %s" %(point.x, point.y, point.label, "sim" if point.label == p.label else "não" ))
    #     point.draw()

    entradas = []
    labels   = []
    #não precisaria varrer os labels fora do método, fiz apenas para separar
    for p in points:
        entradas.append(p.getEntradas())
        labels.append(p.label)
        p.draw()

    ax.set_title('Resultado correto (antes do treinamento)')
    plt.show()
    plt.close()

    print('As imagens seguintes mostram o resultado da rede, treinando e se ajustando a partir dos exemplos fornecidos')
    perc.treinarBatch(entradas, labels)

    for p in points:
        chute = perc.adivinhar(p.getEntradas())
        point = Point(p.x, p.y, ax)
        point.setLabel(chute)
        #descomente abaixo para se assegurar que todos os exemplos foram classificados corretamente.
        print("%d, %d = %d, certo? = %s" % (point.x, point.y, point.label, "sim" if point.label == p.label else "não"))

    p2 = Point(20,10, ax )   
    print( perc.adivinhar(p2.getEntradas()) )




def gerarPontosAleatorios():
    points = []
    for i in range(50):
        x = int(random.uniform(0,50))
        y = int(random.uniform(0,50))
        points.append(Point(x,y, ax))
    return points


if __name__ == "__main__":
    main()