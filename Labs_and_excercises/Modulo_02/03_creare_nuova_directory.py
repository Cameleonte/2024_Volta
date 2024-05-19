import os

directory = "IVolta"
parent_dir = "C:\\Lavorativa\\2024_Volta\\Esercizi Python"
path = os.path.join(parent_dir, directory)

# creare la directory "IVolta" nella directory parentale
os.mkdir(path)
print("Directory '% s' created" % directory)
