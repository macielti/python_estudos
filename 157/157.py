#o from import foi usado para unir os dois modulos.
import eletro_car

#crio uma instancia carro
carro= eletro_car.Eletro_Car('sam', 'relampago marquinhos')

#mostro o valor da bateria
carro.batterya.show_batterya()

#mostro a distancia que o carro roda com essa beteria
carro.batterya.eficiencia_bate()
