from metaheuristics.fireflyAlgorithm import fireflyAlgorithm

architecture = 'ResNet152'
dataset = 'D0'
population_size = 5
max_iteration = 10
fireflyAlgorithm(population_size, max_iteration, architecture, dataset)