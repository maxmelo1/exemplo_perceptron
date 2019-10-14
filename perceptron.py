import random
import numpy as np

from point import Point
import matplotlib.pyplot as plt


class Perceptron():

    def __init__(self):
        self.pesos = []

        self.LR = 0.1

        for i in range(2):
            self.pesos.append(random.uniform(-1, 1))

    '''
    dado um exemplo ele prediz a classe do exemplo.
    O nome correto seria predict. Após o treinamento e ajuste dos pesos, deve ser chamado
    '''

    def adivinhar(self, entradas):
        soma = 0

        if len(self.pesos) != len(entradas):
            raise Exception("dimensões diferentes")

        for i in range(len(self.pesos)):
            soma = soma + self.pesos[i] * entradas[i]

        # soma = 0 pode causar problema
        return np.sign(soma)

    '''
    serve para ajustar os pesos da perceptron a partir dos exemplos
    o nome correto seria train. Train deveria receber um vetor de entradas e não somente uma entrada
    '''

    def treinar(self, entradas, classe):
        chute = self.adivinhar(entradas)

        erro = classe - chute

        for i in range(len(self.pesos)):
            self.pesos[i] = self.pesos[i] + erro * entradas[i] * self.LR

    '''
        serve para ajustar os pesos da perceptron a partir dos exemplos
        o nome correto seria train. Deveria repetir até o erro decair a zero
        '''

    def treinarBatch(self, entradas, classes):
        erroAcc = 1
        epoca = 0
        while abs(erroAcc) > 0:
            erroAcc = 0

            fig, axx = plt.subplots()

            x = np.linspace(0, 50, 100)
            plt.plot(x, x)

            for i in range(len(entradas)):
                chute = self.adivinhar(entradas[i])

                erro = classes[i] - chute

                erroAcc += abs(erro)
                for j in range(len(self.pesos)):
                    self.pesos[j] = self.pesos[j] + erro * entradas[i][j] * self.LR

                point = Point(entradas[i][0], entradas[i][1], axx)
                point.setLabel(chute)
                # print("%d, %d" % (point.x, point.y))
                point.draw()


            axx.set_title('Ajuste de pesos, época %d' % epoca)
            print("erro total na iteração: %d" % erroAcc)
            # input()
            plt.show()
            plt.close()
            epoca += 1

        print('Pesos da RNA ajustados. A partir de agora pode-se criar um novo ponto e acionar o método "adivinhar" para testar sua accurácia real')
