files= ['cats.txt', 'dogs.txt']
pets=''
for filename in files:
    try:
        with open(filename) as filenam:
            pets= filenam.readlines()
    
    except FileNotFoundError :
        pass
    else:
        for pet in pets:
            print (pet.rstrip())
