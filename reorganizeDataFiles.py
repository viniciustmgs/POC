import os
import shutil

#Função para criar os diretórios para cada classe nas pastas train, test e val
def create_class_directories(root_dir, num_classes):
    for split in ['train', 'test', 'val']:
        split_dir = os.path.join(root_dir, split)
        os.makedirs(split_dir, exist_ok=True)
        for class_id in range(num_classes):
            class_dir = os.path.join(split_dir, str(class_id))
            os.makedirs(class_dir, exist_ok=True)

#Função para mover as imagens para seus respectivos diretórios de classe
def organize_images(root_dir, split_file, num_classes):
    split_file_dir = os.path.join(root_dir, split_file)
    with open(split_file_dir, 'r') as file:
        for line in file:
            image_name, class_id = line.strip().split()
            class_id = int(class_id)
            source_path = os.path.join(root_dir, 'images', image_name)
            destination_dir = os.path.join(root_dir, split_file.split('.')[0], str(class_id))
            destination_path = os.path.join(destination_dir, image_name)
            shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    root_dir = "data/ip102_v1.1"
    num_classes = 102
    splits = ['train.txt', 'test.txt', 'val.txt']

    create_class_directories(root_dir, num_classes)

    for split_file in splits:
        organize_images(root_dir, split_file, num_classes)