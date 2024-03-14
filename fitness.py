from keras.callbacks import EarlyStopping
from generators.ip102Generator import createGeneratorIP102
from model import buildModel


def objective(train_generator, val_generator, architecture, solution):
    
    #Construir o modelo com os hiperparâmetros fornecidos
    model = buildModel(solution, architecture, train_generator.num_classes)

    #Configurando método de parada para caso o modelo não esteja aprendendo
    early_stopping = EarlyStopping(
        monitor='val_loss',  #Monitora a perda de validação
        min_delta=0.001,  # O mínimo de melhora a ser considerada como uma melhora
        patience=10,  #Número de epochs sem melhora após o qual o treinamento será interrompido
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

    val_accuracy = history.history['val_accuracy']

    print(val_accuracy)

architecture = 'ResNet152'
solution=[0.09, 0.27, 'adagrad', 4, 4096, 0.001]
train_generator, val_generator, test_generator = createGeneratorIP102(architecture)
objective(train_generator, val_generator, architecture, solution)