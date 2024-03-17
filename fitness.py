from keras.callbacks import EarlyStopping
from generators.ip102Generator import createGeneratorIP102
from generators.d0Generator import createGeneratorD0
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
        steps_per_epoch=int(train_generator.samples // train_generator.batch_size),
        epochs=32,
        validation_data=val_generator,
        validation_steps=int(val_generator.samples // val_generator.batch_size),
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

    val_precision = history.history['val_precision'][val_accuracy_index]
    val_recall = history.history['val_recall'][val_accuracy_index]
    val_f1_score = history.history['val_f1_score'][val_accuracy_index]
    mean_val_precision = tf.reduce_mean(val_precision)

    #Avaliar o modelo no conjunto de teste
    test_loss, test_accuracy, test_precision, test_recall, test_f1_score = model.evaluate(test_generator)

    #Calcular a precisão média
    mean_test_precision = tf.reduce_mean(test_precision)

    #Imprimir as métricas
    print('Validation Accuracy:', val_accuracy)
    print('Validation Precision:', mean_val_precision.numpy())
    print('Validation Recall:', val_recall)
    print('Validation F1 Score: ', val_f1_score)

    print('Test Accuracy:', test_accuracy)
    print('Test Precision:', mean_test_precision.numpy())
    print('Test Recall:', test_recall)
    print('Test F1 Score: ', test_f1_score)
    print('Test Loss: ', test_loss)

    return [[val_accuracy, mean_val_precision.numpy(), val_recall, val_f1_score], [test_accuracy, mean_test_precision.numpy(), test_recall, test_f1_score]]

def fitness(architecture, firefly, dataset):
    solution = translateSolution(firefly)
    if (dataset == 'IP102'):
        train_generator, val_generator, test_generator = createGeneratorIP102(architecture)
    elif(dataset == 'D0'):
        train_generator, val_generator, test_generator = createGeneratorD0(architecture)
    val_metrics, test_metrics = objective(train_generator, val_generator, test_generator, architecture, solution)
    val_accuracy, val_precision, val_recall, val_f1_score = val_metrics
    fitness_value = (val_accuracy + val_precision + val_recall + val_f1_score)/4
    with open('metaheuristics/output.txt', 'w') as file:
        file.write(f'     Val metrics: {val_metrics}\n')
        file.write(f'     Test metrics: {test_metrics}\n')
    return fitness_value*100


#architecture = 'ResNet152'
#solution=[0.09, 0.27, 'adagrad', 4, 4096, 0.01]
#solution=[0.3, 0.3, 'sgd', 3, 1024, 0.01]
#train_generator, val_generator, test_generator = createGeneratorD0(architecture)
#objective(train_generator, val_generator, test_generator, architecture, solution)