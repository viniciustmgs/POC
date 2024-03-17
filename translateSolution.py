def translateSolution(firefly):

    #Dividindo a solução
    variable_1, variable_2, variable_3, variable_4, variable_5, variable_6 = firefly

    #Transformando em inteiro
    variable_1 = int(variable_1)
    variable_2 = int(variable_2)
    variable_4 = int(variable_4)
    variable_6 = int(variable_6)

    if (variable_1 == 0):
        freezing_ratio = 0.01
    else:
        freezing_ratio = variable_1/100

    if (variable_2 == 0):
        dropout_ratio = 0.01
    else:
        dropout_ratio = variable_2/100

    if ((variable_3 >= 0) and (variable_3 < 16.7)):
        optimizer = 'adam'
    elif ((variable_3 >= 16.7) and (variable_3 < 33.4)):
        optimizer = 'sgd'
    elif ((variable_3 >= 33.4) and (variable_3 < 50)):
        optimizer = 'rmsprop'
    elif ((variable_3 >= 50) and (variable_3 < 66.7)):
        optimizer = 'adadelta'
    elif ((variable_3 >= 66.7) and (variable_3 < 83.4)):
        optimizer = 'adagrad'
    elif ((variable_3 >= 83.4) and (variable_3 <= 100)):
        optimizer = 'adamax'

    if ((variable_4 >= 0) and (variable_4 < 20)):
        num_fc_layers = 1
    elif ((variable_4 >= 20) and (variable_4 < 40)):
        num_fc_layers = 2
    elif ((variable_4 >= 40) and (variable_4 < 60)):
        num_fc_layers = 3
    elif ((variable_4 >= 60) and (variable_4 < 80)):
        num_fc_layers = 4
    elif ((variable_4 >= 80) and (variable_4 <= 100)):
        num_fc_layers = 5

    if ((variable_5 >= 0) and (variable_5 < 16.7)):
        neurons = 64
    elif ((variable_5 >= 16.7) and (variable_5 < 33.4)):
        neurons = 128
    elif ((variable_5 >= 33.4) and (variable_5 < 50)):
        neurons = 256
    elif ((variable_5 >= 50) and (variable_5 < 66.7)):
        neurons = 512
    elif ((variable_5 >= 66.7) and (variable_5 < 83.4)):
        neurons = 1024
    elif ((variable_5 >= 83.4) and (variable_5 <= 100)):
        neurons = 2048

    if (variable_6 == 0):
        l2_reg = 0.001
    else:
        l2_reg = variable_6/1000

    print(firefly ,[freezing_ratio, dropout_ratio, optimizer, num_fc_layers, neurons, l2_reg])

    return [freezing_ratio, dropout_ratio, optimizer, num_fc_layers, neurons, l2_reg]