def contador(filename, word):
   
    try:
        with open(filename) as f_obj:
            conteudo= f_obj.read()
    
    except FileNotFoundError:
        print('O arquivo '+filename+' não existe.')
    
    else:
        num_words= conteudo.lower().count(word)
        print("a palavra '"+word+"' aparece "+ str(num_words)+ " vezes no\
 arquivo de texto.")
        
contador('txt.txt','the')
