from keras.applications import Xception, ResNet152
from keras import layers, models, optimizers, regularizers
import tensorflow as tf
#from metrics.f1score import F1Score
#import tensorflow_addons as tfa

def buildModel(solution, architecture, num_classes):
    
    #Separando cada hiperparâmetro da solução
    freezing_ratio, dropout_ratio, optimizer, num_fc_layers, neurons, l2_reg = solution

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

    #Adicionar as camadas fully connected com o número de neuronios especificado,regularizador L2 e o dropout
    for _ in range(num_fc_layers):
        model.add(layers.Dense(neurons, activation='relu', kernel_regularizer=regularizers.l2(l2_reg)))
        #, kernel_regularizer=regularizers.l2(l2_reg)
        model.add(layers.Dropout(dropout_ratio))

    #Camada de saída
    model.add(layers.Dense(num_classes, activation='softmax'))

    #Definir o optimizer
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

    precision = tf.keras.metrics.Precision()
    recall = tf.keras.metrics.Recall()
    f1score = tf.keras.metrics.F1Score()

    #Compilar o modelo
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy', precision, recall, f1score])

    return model