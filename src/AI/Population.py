import random
import json
import numpy as np
from AI.NeuralNetwork import NeuralNetwork
from copy import deepcopy


class Population:

    def __init__(self, populationSize):
        self.__population_size = populationSize
        self.__networks = []
        self.__parameter_list = (3, 8, 3)
        for i in range(self.__population_size):
            self.__networks.append(NeuralNetwork(self.__parameter_list))
        self.__best_network = self.__networks[0]
        self.__generation = 1

    def sort(self, score=None):
        if score is not None:
            for index, network in enumerate(self.__networks):
                network.fitness = score[index]

        self.__networks.sort(key=lambda nn: nn.fitness, reverse=True)
        if self.__networks[0].fitness > self.__best_network.fitness:
            self.__best_network = deepcopy(self.__networks[0])

    def get_size(self):
        return self.__population_size

    def new_generation(self):
        self.sort()

        keep = len(self.__networks) // 3

        for index, network in enumerate(self.__networks):
            if index > keep:
                index1 = random.randint(0, keep)
                index2 = random.randint(0, keep)
                network.crossover(self.__networks[index1], self.__networks[index2])
        self.__generation += 1

        for network in self.__networks:
            network.mutate(0.1)

    def predict_all(self, input):
        predictions = []

        for network in self.__networks:
            predictions.append(network.predict(input))

        return predictions

    def get_best_network(self):
        self.sort()
        return self.__best_network

    def get_generation(self):
        return self.__generation
