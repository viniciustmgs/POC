import tensorflow as tf
from keras.applications.xception import preprocess_input as preprocess_xc
from keras.applications.resnet import preprocess_input as preprocess_rn

def createGeneratorPI(architecture):
    
    train_dir = 'data/Pistachio_Image_Dataset/train'
    test_dir = 'data/Pistachio_Image_Dataset/test'

    #Criação dos geradores de dados com pré-processamento
    if (architecture == 'Xception'):
        image_size = (299, 299)
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc,
            validation_split = 0.125
        )

        test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_xc
        )
    elif (architecture == 'ResNet152'):
        image_size = (224, 224)
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn,
            validation_split = 0.125
        )

        test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_rn
        )

    #Carregamento e pré-processamento das imagens de treinamento, validação e teste
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical',
        subset='training'
    )

    val_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical',
        subset='validation'
    )

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical'
    )
 
    return train_generator, val_generator, test_generator