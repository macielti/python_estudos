from car import Car

#classe para cuidar da bateria do carro elétrico
class Bateria():
    
    #construtor da instancia com um valor padrão
    def __init__(self, value=70):
        self.batterya=70
    
    #mostrar o estado da batterya    
    def show_batterya(self):
        """Mostrar a quantidade de bateria caso o carro seja da classe 
        eletronico"""
        print('Bateria: '+str(self.batterya))
        
        
    def eficiencia_bate(self):
        """Mostrar a eficiencia da bateria e a distanca que ela dura"""
        if self.batterya == 70:
            distancia=240
        else:
            distancia= 270
        print('Esse carro pode ir aproximadamente '+str(distancia)+'milhas com\
 uma carga total')


#Classe filho da primeira class
class Eletro_Car(Car):
    
    #Construtor da classe que recebe dois orgumentos herdados da primeira class
    # e o terceiro argumento śempre será 2030 visto que os carros eletronicos
    #teoricaente se tornariam populares por volta de 2030(contexto kkk)
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 2030)
        self.batterya= Bateria()
