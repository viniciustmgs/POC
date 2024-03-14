import math
import numpy as np

def initializeSolutions(population_size):
    solutions = []
    iteration = 0
    value = 20
    while iteration < population_size:
        solution = []
        for _ in range(6):
            solution.append(np.random.rand()*100)
        solutions.append(solution)
        value += 20
        iteration += 1

    return solutions

def evaluateRange(variable_range, solution):
    evaluated_solution = []
    for variable in solution:
        if (variable < variable_range[0]):
            evaluated_solution.append(variable_range[0])
        elif (variable > variable_range[1]):
            evaluated_solution.append(variable_range[1])
        else:
            evaluated_solution.append(variable)
    return evaluated_solution

def fitness(solution):
    best_solution = [45, 63, 83, 14, 27, 71]
    difference_sum = 0
    for index, variable in enumerate(solution):
        difference_sum += (variable - best_solution[index]) ** 2
    r = math.sqrt(difference_sum)
    fitness = 0 - r
    return fitness


def relativeAttractiveness(beta0, gamma, r):
    return beta0/(1+gamma*(r**2))

def movement(firefly, target_firefly, beta, alpha):
    new_firefly = []
    for index, variable in enumerate(firefly):
        new_firefly.append(variable*(1-beta)+target_firefly[index]*beta+alpha*(np.random.rand()-0.5))
    
    return new_firefly

#Função para calcular a distância entre dois vagalumes
def calc_distance(i_firefly, j_firefly):
    difference_sum = 0
    for index, variable in enumerate(i_firefly):
        difference_sum += (variable - j_firefly[index]) ** 2
    r = math.sqrt(difference_sum)
    return r

def fireflyAlgorithm(population_size, max_iteration):
    
    #Inicialiazndo a população de vagalumes
    fireflies = initializeSolutions(population_size)

    #Calculando a intensidade de luz de cada vagalume
    light_intensities = []
    for firefly in fireflies:
        light_intensity = fitness(firefly)
        light_intensities.append(light_intensity)

    #Definindo o coeficiente de absorção de luz
    gamma = 0.1
    #Definindo o alpha (step size)
    alpha = 0.2
    #Definindo a atratividade inicial
    beta0 = 100
    #Definindo o range das variáveis
    variable_range = [0, 100]

    i_firefly = 0
    j_firefly = 1
    iteration = 1
    evaluations = 10
    with open('output.txt', 'w') as file:
        file.write(f'População inicial: {fireflies}\n')
        file.write(f'Intensidade inicial: {light_intensities}\n')
        while iteration < max_iteration:
            file.write(f'Começando a iteração {iteration}\n')
            while i_firefly < population_size:
                file.write(f' AVALIANDO O VAGALUME {i_firefly}\n')
                while j_firefly < population_size:
                    if (i_firefly != j_firefly):
                        file.write(f'  Comparando com o vagalume {j_firefly}\n')
                        #Caso o vagalume j seja mais luminoso que o vagalume i
                        if(light_intensities[i_firefly] < light_intensities[j_firefly]):
                            file.write(f'    O vagalume {j_firefly} é mais luminoso que o vagalume {i_firefly}\n')
                            #Calculando a distância entre os vagalumes
                            r = calc_distance(fireflies[i_firefly], fireflies[j_firefly])
                            file.write(f'    A distância entre eles é de {r}\n')
                            #Calculando a atratividade
                            beta = relativeAttractiveness(beta0, gamma, r)
                            file.write(f'    A atratividade entre eles é {beta}\n')
                            #Movendo o vagalume i em direção ao j
                            fireflies[i_firefly] = movement(fireflies[i_firefly], fireflies[j_firefly], beta, alpha)
                            #Avaliando o range das variáveis
                            fireflies[i_firefly] = evaluateRange(variable_range, fireflies[i_firefly])
                            file.write(f'    O novo vagalume {i_firefly} é {fireflies[i_firefly]}\n')
                            #Avaliando o novo vagalume
                            light_intensities[i_firefly] = fitness(fireflies[i_firefly])
                            evaluations += 1
                            file.write(f'    Sua nova intensidade é {light_intensities[i_firefly]}\n')
                    j_firefly += 1
                i_firefly +=1
                j_firefly = 0
            i_firefly = 0
            file.write(f'Fim da iteraçao {iteration}\n')
            file.write(f'População atual: {fireflies}\n')
            file.write(f'Intensidades atuais: {light_intensities}\n')
            file.write(f'Numero de avaliações: {evaluations}\n')
            iteration += 1
    


population_size = 5
max_iteration = 10
fireflyAlgorithm(population_size, max_iteration)