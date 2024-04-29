import random

def generateArray():
    array = []
    for num1 in range(6):
        for num2 in range(6):    
            for num3 in range(6):
                if ((num2 != num1) and (num3 != num2) and (num3 != num1)):
                    array.append([num1+1, num2+1, num3+1])
    return array
                    
first_half = generateArray()
second_half = generateArray()

random.shuffle(first_half)
random.shuffle(second_half)

final_results = []

for index in range(120):
    final_results.append(first_half[index] + second_half[index])

final = []

for result in final_results:
    new_solution = []
    for number in result:
        if number == 1:
            rand = random.uniform(0, 16.7)
        if number == 2:
            rand = random.uniform(16.7, 33.4)
        if number == 3:
            rand = random.uniform(33.4, 50)
        if number == 4:
            rand = random.uniform(50, 66.7)
        if number == 5:
            rand = random.uniform(66.7, 83.4)
        if number == 6:
            rand = random.uniform(83.4, 100)
        new_solution.append(rand)
    final.append(new_solution)

with open('initialPoints.txt', 'w') as file:
    for result in final:
        file.write(f'solutions_final.append({result})\n')