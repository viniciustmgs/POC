import math
import numpy as np
from fitness import fitness
import random
import time
import multiprocessing

def initializeSolutions(population_size):
    solutions = []
    iteration = 0
    value = 20
    while iteration < population_size:
        solution = []
        for _ in range(6):
            solution.append(random.uniform(0, 100))
        solutions.append(solution)
        value += 20
        iteration += 1
    
    solutions_final = []
    solutions_final.append([58.24796026045113, 71.43740416396933, 13.080297910765022, 7.796866770317362, 38.601303852605675, 93.63247715711032])
    solutions_final.append([14.17580501905442, 62.08550223949069, 48.1821212458895, 58.82651312759204, 7.4299276885040335, 29.593523000349727])
    solutions_final.append([48.36302937670052, 94.06271635112267, 30.38270965211129, 64.40839210902182, 83.27837506876372, 36.14998472419714])
    solutions_final.append([89.99991566674669, 76.67529995758068, 45.6822597297909, 87.24005348103915, 37.108405727124854, 78.47595391758753])
    solutions_final.append([72.53623440292303, 84.45717541171314, 25.579194433790065, 44.23712285277503, 31.201547799017256, 58.89511107043818])
    return solutions_final

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

def rosenbrockFunction(solution):
    total_sum = 0
    iteration = 0
    while iteration < 5:
        total_sum += 100*(solution[iteration+1]-solution[iteration]**2)**2+(solution[iteration]-1)**2
        iteration += 1
    return total_sum

def rastriginFunction(solution):
    total_sum = 0
    a_consant = 10
    for variable in solution:
        total_sum += variable**2 - a_consant*math.cos(2*math.pi*variable)
    final = total_sum + a_consant*6
    return final

def fitness1(x, solution, y):
    best_solution = [45, 63, 83, 14, 27, 71]
    difference_sum = 0
    for index, variable in enumerate(solution):
        difference_sum += (variable - best_solution[index]) ** 2
    r = math.sqrt(difference_sum)
    fitness = 0 - r
    return [fitness, [0, 0, 0, 0]]


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
        difference_sum += (variable - j_firefly[index])**2
    r = math.sqrt(difference_sum)
    return r

def newAlpha(alpha):
    if (alpha > 0.02):
        return alpha - 0.02
    else:
        return alpha
    
def newBeta0(beta0):
    if (beta0 > 1):
        new_beta0 = beta0 - 7
        if new_beta0 <= 0:
            return 1
        else:
            return new_beta0
    else:
        return beta0
    
def getFitness(architecture, firefly, dataset):
    new_process = multiprocessing.Process(target=fitness, args=(architecture, firefly, dataset))
    new_process.start()
    new_process.join()
    with open('metaheuristics/fitnessValue.txt', 'r') as file:
        linha1 = file.readline()
        linha2 = file.readline()
    return [float(linha1), linha2]

def fireflyAlgorithm(population_size, max_iteration, architecture, dataset):
    
    #Inicialiazndo a população de vagalumes
    fireflies = initializeSolutions(population_size)

    light_intensities = []
    results = []
    for index, firefly in enumerate(fireflies):
        with open('metaheuristics/output.txt', 'a') as file:
            file.write(f'Vagalume inicial {index+1}\n')
            file.write(f' Vagalume: {firefly}\n')
        fitness_result = getFitness(architecture, firefly, dataset)
        with open('metaheuristics/output.txt', 'a') as file:
            file.write(f' Teste: {fitness_result[1]}\n')
            file.write(f' Fitness: {fitness_result[0]}\n')
        light_intensity = fitness_result[0]
        results.append(fitness_result)
        light_intensities.append(light_intensity)

    #Definindo o coeficiente de absorção de luz
    gamma = 0.1
    #Definindo o alpha (step size)
    alpha = 0.5
    #Definindo a atratividade inicial
    beta0 = 60
    #Definindo o range das variáveis
    variable_range = [0, 100]

    i_firefly = 0
    j_firefly = 1
    iteration = 0
    evaluations = 5
    max_beta = 1.4

    while iteration < max_iteration:
        with open('metaheuristics/output.txt', 'a') as file:
            file.write(f'Começando a iteração {iteration}\n')
        while i_firefly < population_size:
            with open('metaheuristics/output.txt', 'a') as file:
                file.write(f' AVALIANDO O VAGALUME {i_firefly}\n')
            while j_firefly < population_size:
                if (i_firefly != j_firefly):
                    with open('metaheuristics/output.txt', 'a') as file:
                        file.write(f'  Comparando com o vagalume {j_firefly}\n')
                    #Caso o vagalume j seja mais luminoso que o vagalume i
                    if(light_intensities[i_firefly] < light_intensities[j_firefly]):
                        with open('metaheuristics/output.txt', 'a') as file:
                            file.write(f'    O vagalume {j_firefly} é mais luminoso que o vagalume {i_firefly}\n')
                            file.write(f'    Vagalume i: {fireflies[i_firefly]}\n')
                            file.write(f'    Vagalume j: {fireflies[j_firefly]}\n')
                        #Calculando a distância entre os vagalumes
                        r = calc_distance(fireflies[i_firefly], fireflies[j_firefly])
                        with open('metaheuristics/output.txt', 'a') as file:
                            file.write(f'    A distância entre eles é de {r}\n')
                        #Calculando a atratividade
                        beta = relativeAttractiveness(beta0, gamma, r)
                        if beta > max_beta:
                            beta = max_beta
                        with open('metaheuristics/output.txt', 'a') as file:
                            file.write(f'    A atratividade entre eles é {beta}\n')
                        #Movendo o vagalume i em direção ao j
                        fireflies[i_firefly] = movement(fireflies[i_firefly], fireflies[j_firefly], beta, alpha)
                        #Avaliando o range das variáveis
                        fireflies[i_firefly] = evaluateRange(variable_range, fireflies[i_firefly])
                        with open('metaheuristics/output.txt', 'a') as file:
                            file.write(f'    O novo vagalume {i_firefly} é {fireflies[i_firefly]}\n')
                        #Avaliando o novo vagalume
                        fitness_result = getFitness(architecture, fireflies[i_firefly], dataset)
                        results[i_firefly] = fitness_result
                        light_intensities[i_firefly] = fitness_result[0]
                        with open('metaheuristics/output.txt', 'a') as file:
                            file.write(f'    Teste: {fitness_result[1]}\n')
                            file.write(f'    Sua nova intensidade é: {light_intensities[i_firefly]}\n')
                        evaluations += 1
                j_firefly += 1
            i_firefly +=1
            j_firefly = 0
        i_firefly = 0
        with open('metaheuristics/output.txt', 'a') as file:
            file.write(f'Fim da iteraçao {iteration}\n')
            file.write(f'População atual: {fireflies}\n')
            for index, result in enumerate(results):
                file.write(f' Vagalume {index+1}: {fireflies[index]}\n')
                file.write(f'  Validação: {result[1]}\n')
            file.write(f'Intensidades atuais: {light_intensities}\n')
            file.write(f'Numero de avaliações: {evaluations}\n')
            iteration += 1
            alpha = newAlpha(alpha)
            file.write(f'Novo alpha: {alpha}\n')
            beta0 = newBeta0(beta0)
            file.write(f'Novo Beta0: {beta0}\n')
        if iteration > 6:
            max_beta = max_beta - 0.1
    best_result = max(light_intensities)
    indice_numero = light_intensities.index(best_result)
    with open('metaheuristics/output.txt', 'a') as file:
        file.write(f'FINAL:\nFitness: {light_intensities}\n')
        file.write(f'Soluções: {fireflies}\n')
        file.write(f'Melhor fitness: {best_result}\n')
        file.write(f'Solução: {fireflies[indice_numero]}, que é a solução: {indice_numero} da lista\n')