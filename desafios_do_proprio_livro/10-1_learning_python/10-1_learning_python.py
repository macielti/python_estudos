file_name= 'learning_python.txt'
with open(file_name) as texto:
    lista= texto.readlines()

for line in lista[:3]:
    print(line.rstrip())
