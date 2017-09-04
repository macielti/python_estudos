f_numbers={
    'Bruno Ribeiro':[24, 15, 26],
    'Rafaela':[69, 23],
    'Vinicius':[12, 40, 70],
    'Samuel':[42, 90, 22],
    'Mateus':[40],    
    }

for k, v in f_numbers.items():
    print(k.title()+': ')
    for num in v:
        print(str(num))
    print('\n')
