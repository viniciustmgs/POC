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
    solutions_final.append([99.2027574291569, 29.614209115130674, 45.25060859873486, 91.17739613790052, 39.595468129596256, 63.708167109067126])
    solutions_final.append([23.386795196558342, 85.71766479382114, 64.50169223776707, 55.06724251883359, 20.158288730855293, 90.43152064865318])
    solutions_final.append([28.50384170410012, 96.9576877396034, 10.629872452530185, 93.37501952113122, 61.51725728684471, 47.50633708109376])
    solutions_final.append([43.998702312486756, 26.39956966912714, 91.80369167090552, 31.95926510302121, 2.619528728839757, 38.82670479176484])
    solutions_final.append([8.623805765249147, 20.80808340799571, 68.81334054180685, 0.5650088837437622, 70.78125161660336, 34.0204594881539])
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