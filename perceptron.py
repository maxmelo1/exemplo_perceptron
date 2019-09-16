import random
import numpy as np

class Perceptron():




    def __init__(self):
        self.pesos = []

        self.LR  = 0.1

        for i in range(2):
            self.pesos.append( random.uniform(-1,1) )

    def adivinhar(self, entradas):
        soma = 0

        if len(self.pesos) != len(entradas):
            raise Exception("dimensões diferentes")

        for i in range(len(self.pesos)) :
            soma = soma + self.pesos[i] * entradas[i]

        #soma = 0 pode causar problema
        return np.sign(soma)

    def treinar(self, entradas, classe):
        chute = self.adivinhar(entradas)

        erro = classe - chute

        for(i in len(self.pesos)):
            self.pesos[i] = self.pesos[i] + erro*entradas[i]*self.LR


