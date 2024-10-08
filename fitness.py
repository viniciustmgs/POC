from keras.callbacks import EarlyStopping
from generators.mLGenerator import createGeneratorMl
from generators.d0Generator import createGeneratorD0
from generators.mcwGenerator import createGeneratorMCW
from generators.piGenerator import createGeneratorPI
from model import buildModel
import tensorflow as tf
from translateSolution import translateSolution


def objective(train_generator, val_generator, test_generator, architecture, solution):
    
    #Construir o modelo com os hiperparâmetros fornecidos
    model = buildModel(solution, architecture, train_generator.num_classes)

    #Configurando método de parada para caso o modelo não esteja aprendendo
    early_stopping = EarlyStopping(
        monitor='val_loss',  #Monitora a perda de validação
        min_delta=0.001,  # O mínimo de melhora a ser considerada como uma melhora
        patience=13,  #Número de epochs sem melhora após o qual o treinamento será interrompido
        verbose=1,  #Mostra mensagens quando o treinamento é interrompido
        mode='min',  #Porque o objetivo é minimizar a perda de validação
        restore_best_weights=True   #Restaura os pesos do modelo com a melhor perda de validação observada
    )
    
    #Treinar o modelo
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=32,
        validation_data=val_generator,
        validation_steps=val_generator.samples // val_generator.batch_size,
        callbacks=[early_stopping]
    )

    #Pegando as métricas de validação
    val_accuracies = history.history['val_accuracy']
    val_accuracy = 0
    val_accuracy_index = 0
    for index, accuracy in enumerate(val_accuracies):
        if (index % 2 == 0):
            if (accuracy > val_accuracy):
                val_accuracy = accuracy
                val_accuracy_index = index

    f1_key = list(history.history.keys())[6]
    precision_key = list(history.history.keys())[8]
    recall_key = list(history.history.keys())[9]

    val_precision = history.history[precision_key][val_accuracy_index]
    val_recall = history.history[recall_key][val_accuracy_index]
    val_f1_score = history.history[f1_key][val_accuracy_index]
    mean_val_f1_score = tf.reduce_mean(val_f1_score)
    #mean_val_precision = tf.reduce_mean(val_precision)

    #Avaliar o modelo no conjunto de teste
    test_loss, test_accuracy, test_precision, test_recall, test_f1_score = model.evaluate(test_generator)

    #Calcular a precisão média
    mean_test_precision = tf.reduce_mean(test_precision)

    #Imprimir as métricas
    print('Validation Accuracy:', val_accuracy)
    print('Validation Precision:', val_precision)
    print('Validation Recall:', val_recall)
    print('Validation F1 Score: ', mean_val_f1_score.numpy())

    print('Test Accuracy:', test_accuracy)
    print('Test Precision:', mean_test_precision.numpy())
    print('Test Recall:', test_recall)
    print('Test F1 Score: ', test_f1_score)
    #print('Test Loss: ', test_loss)

    return [test_accuracy, mean_test_precision.numpy(), test_recall, test_f1_score]
    #return [val_accuracy, val_precision, val_recall, mean_val_f1_score.numpy()]

def fitness(architecture, firefly, dataset):
    solution = translateSolution(firefly)
    if (dataset == 'ML'):
        train_generator, val_generator, test_generator = createGeneratorMl(architecture)
    elif(dataset == 'D0'):
        train_generator, val_generator, test_generator = createGeneratorD0(architecture)
    elif(dataset == 'MCW'):
        train_generator, val_generator, test_generator = createGeneratorMCW(architecture)
    elif(dataset == 'PI'):
        train_generator, val_generator, test_generator = createGeneratorPI(architecture)
    test_metrics = objective(train_generator, val_generator, test_generator, architecture, solution)
    test_accuracy, test_precision, test_recall, test_f1_score = test_metrics
    fitness_value = (test_accuracy + test_precision + test_recall + test_f1_score)/4
    print(fitness_value*100)
    with open('metaheuristics/fitnessValue.txt', 'w') as file:
            file.write(f'{fitness_value*100}\n')
            file.write(f'{test_metrics}')
    #return [fitness_value*100, val_metrics]