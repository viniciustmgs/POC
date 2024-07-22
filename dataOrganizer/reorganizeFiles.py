import os
import shutil
from sklearn.model_selection import train_test_split

#NOME DO DIRETORIO, MUDAR PARA OS DIFERENTES DATASETS
directory_name = 'malaria'

# Diretório raiz do seu dataset
dataset_dir = f'data/{directory_name}'

# Diretório de destino para os conjuntos de treinamento e teste
train_dir = f'data/{directory_name}/train'
test_dir = f'data/{directory_name}/test'

# Lista para armazenar os caminhos das imagens e seus respectivos rótulos
images = []
labels = []

# Percorre todas as subpastas do diretório raiz para obter as imagens e rótulos
for class_folder in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_folder)
    if os.path.isdir(class_path):
        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)
            images.append(image_path)
            labels.append(int(class_folder))

# Divide os dados em conjuntos de treinamento e teste
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42, stratify=labels)

# Função para copiar imagens para os diretórios de treinamento e teste mantendo a estrutura de pastas
def copy_images(images, labels, dest_dir):
    for image_path, label in zip(images, labels):
        class_dir = os.path.join(dest_dir, str(label))
        os.makedirs(class_dir, exist_ok=True)
        image_name = os.path.basename(image_path)
        shutil.copy(image_path, os.path.join(class_dir, image_name))

# Copia imagens para o diretório de treinamento
copy_images(train_images, train_labels, train_dir)

# Copia imagens para o diretório de teste
copy_images(test_images, test_labels, test_dir)

print("Dataset dividido em conjuntos de treinamento e teste com sucesso.")