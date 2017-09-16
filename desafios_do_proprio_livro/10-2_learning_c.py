file_name= '10-1_learning_python/learning_python.txt'

with open(file_name) as text:
    lines= text.readlines()

for line in lines:
    print(line.replace('Python','C').rstrip())
