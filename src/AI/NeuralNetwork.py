import numpy as np
import random

# Resources: 
# https://enlight.nyc/projects/neural-network/
# https://www.python-course.eu/neural_networks_with_python_numpy.php


class NeuralNetwork:

    def __init__(self, parameter_list):
        self.__input_size = parameter_list[0]
        self.__hidden_size = parameter_list[1]
        self.__output_size = parameter_list[2]

        self.__weights_ih = np.random.randn(self.__hidden_size, self.__input_size)
        self.__weights_ho = np.random.randn(self.__output_size, self.__hidden_size)

        self.__fitness = 0

    def sigmoid(self, vector):
        return 1 / (1 + np.exp(-vector))

    def predict(self, input):
        input_vector = np.array(input, ndmin=2).T

        output_vector = np.dot(self.__weights_ih, input_vector)
        output_vector = self.sigmoid(output_vector)

        output_vector = np.dot(self.__weights_ho, output_vector)
        output_vector = self.sigmoid(output_vector)

        return output_vector

    def mutate(self, mutationRate):
        for element in self.__weights_ih:
            if mutationRate >= random.random():
                element += random.gauss(0, 0.1)

        for element in self.__weights_ho:
            if mutationRate >= random.random():
                element += random.gauss(0, 0.1)

    def crossover(self, parent1, parent2):
        fitness_comp = parent1.fitness / (parent1.fitness + parent2.fitness)
        for index, element in enumerate(self.__weights_ih):
            for index2 in range(len(element)):
                if fitness_comp >= random.random():
                    self.__weights_ih[index][index2] = parent1.weights_ih[index][index2]
                else:
                    self.__weights_ih[index][index2] = parent2.weights_ih[index][index2]

        for index, element in enumerate(self.__weights_ho):
            for index2 in range(len(element)):
                if fitness_comp >= random.random():
                    self.__weights_ho[index][index2] = parent1.weights_ho[index][index2]
                else:
                    self.__weights_ho[index][index2] = parent2.weights_ho[index][index2]

    def set_network(self, weights_ih, weights_ho):
        self.__weights_ih = weights_ih
        self.__weights_ho = weights_ho