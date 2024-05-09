from metaheuristics.fireflyAlgorithm import fireflyAlgorithm

architecture = 'Xception'
dataset = 'MCW'
population_size = 5
max_iteration = 10
fireflyAlgorithm(population_size, max_iteration, architecture, dataset)