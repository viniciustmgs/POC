from keras.callbacks import EarlyStopping
from keras.applications import Xception, InceptionResNetV2, NASNetLarge, ResNet152
from keras import layers, models, optimizers
import numpy as np
import createGenerators as cg

def buildModel(architecture='ResNet152', freezing_ratio=0.09, dropout_ratio=0.27, optimizer='adagrad', num_fc_layers=4, neurons=4096):
    
    #Carregar o modelo pré-treinado sem a camada superior (top layer)
    if (architecture == 'Xception'):
        base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))
    elif (architecture == 'ResNet152'):
        base_model = ResNet152(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    #Congelar as camadas conforme o freezing ratio
    freeze_until = int(len(base_model.layers) * freezing_ratio)
    for layer in base_model.layers[:freeze_until]:
        layer.trainable = False

    #Criar o modelo
    model = models.Sequential()
    model.add(base_model)
    model.add(layers.GlobalAveragePooling2D())

    #Adicionar as camadas fully connected com o número de neuronios especificado
    for _ in range(num_fc_layers):
        model.add(layers.Dense(neurons, activation='relu'))
        model.add(layers.Dropout(dropout_ratio))

    #Camada de saída
    model.add(layers.Dense(102, activation='softmax'))  # Ajuste conforme necessário

    #Pegar o optimizer
    if optimizer == 'adam':
        opt = optimizers.Adam()
    elif optimizer == 'sgd':
        opt = optimizers.SGD()
    elif optimizer == 'rmsprop':
        opt = optimizers.RMSprop()
    elif optimizer == 'adadelta':
        opt = optimizers.Adadelta()
    elif optimizer == 'adagrad':
        opt = optimizers.Adagrad()
    elif optimizer == 'adamax':
        opt = optimizers.Adamax()
    else:
        raise ValueError("Optimizer not recognized")

    #Compilar o modelo
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])  # Ajuste conforme necessário

    return model

def objective(train_generator, val_generator, architecture='ResNet152', solution=[0.09, 0.27, 'adagrad', 4, 4096]):
    
    #Separando cada hiperparâmetro da solução
    freezing_ratio, dropout_ratio, optimizer, num_fc_layers, neurons = solution
    
    #Construir o modelo com os hiperparâmetros fornecidos
    model = buildModel(architecture, freezing_ratio, dropout_ratio, optimizer, num_fc_layers, neurons)

    #Configurando método de parada para caso o modelo não esteja aprendendo
    early_stopping = EarlyStopping(
        monitor='val_loss',  #Monitora a perda de validação
        min_delta=0.001,  # O mínimo de melhora a ser considerada como uma melhora
        patience=10,  #Número de epochs sem melhora após o qual o treinamento será interrompido
        verbose=1,  #Mostra mensagens quando o treinamento é interrompido
        mode='min',  #Porque o objetivo é minimizar a perda de validação
        restore_best_weights=True   #Restaura os pesos do modelo com a melhor perda de validação observada
    )
    print(int(train_generator.samples // train_generator.batch_size))
    print(int(val_generator.samples // val_generator.batch_size))
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
solution=[0.09, 0.27, 'adagrad', 4, 4096]
train_generator, val_generator, test_generator = cg.createGeneratorIP102(architecture)
objective(train_generator, val_generator, architecture, solution)