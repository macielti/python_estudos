#esse tipo de importação, importa uma unica função do modulo
from pizza_module import makeador_de_pizza

#importamos um modulo junto com todas as suas funções, não é preciso imformar o
#módulo quando for chamar as funções
from pizza_module import *

#Esse tipo de importação, importa uma única função do modulo usando um nome
#personalizado para a função
from pizza_module import makeador_de_pizza as pizza

#importa todas as funções de um modulo mas para chamar uma função devemos
#indentificar em que modulo se encontra a função
import pizza_module

#Esse import importa um módulo com um nome personalizado
import pizza_module as pizza_m
