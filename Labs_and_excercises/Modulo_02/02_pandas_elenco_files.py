import os

os.listdir()
files = [f for f in os.listdir() if os.path.isfile(f)]
for file in files:
    print(file)
