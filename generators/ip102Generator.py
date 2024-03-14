import tensorflow as tf
from keras.applications.xception import preprocess_input as preprocess_xc
from keras.applications.resnet import preprocess_input as preprocess_rn

def createGeneratorIP102(architecture):

    train_dir = 'data/ip102_v1.1/train'
    val_dir = 'data/ip102_v1.1/val'
    test_dir = 'data/ip102_v1.1/test'

    #Criação dos geradores de dados com pré-processamento
    if (architecture == 'Xception'):
        image_size = (299, 299)
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc
        )
    elif (architecture == 'ResNet152'):
        image_size = (224, 224)
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn,
        )

    #Carregamento e pré-processamento das imagens de treinamento, validação e teste
    train_generator = datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )

    val_generator = datagen.flow_from_directory(
        val_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )

    test_generator = datagen.flow_from_directory(
        test_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )
 
    return train_generator, val_generator, test_generator