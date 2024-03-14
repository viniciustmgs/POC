import tensorflow as tf
from keras.applications.xception import preprocess_input as preprocess_xc
from keras.applications.inception_resnet_v2 import preprocess_input as preprocess_irnv2
from keras.applications.resnet import preprocess_input as preprocess_rn

def createGeneratorIP102(architecture):

    train_dir = 'data/ip102_v1.1/train'
    val_dir = 'data/ip102_v1.1/val'
    test_dir = 'data/ip102_v1.1/test'

    

    #Criação dos geradores de dados com pré-processamento
    if (architecture == 'Xception'):
        image_size = (299, 299)
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc,
        )

        val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc,
        )

        test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc,
        )
    elif (architecture == 'ResNet152'):
        image_size = (224, 224)
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn,
        )

        val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn,
        )

        test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn,
        )

    #Carregamento e pré-processamento das imagens de treinamento e validação
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )

    val_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )
 
    return train_generator, val_generator, test_generator