import matplotlib.pyplot as plt
import numpy as np

cant_genes_ind = 2
cant_tipo_gen = 10
tienda = {1:[7,3,10], 2:[6,3,8], 3:[4,5,3], 4:[10,5,4], 5:[12,10,2], 6:[3,8,6], 7:[5,8,1], 8:[8,9,2], 9:[9,12,0], 10:[12,12,2]}
population = {0:[[tienda[2],tienda[4]],0], 1:[[tienda[2],tienda[8]],0]}

k1 = 1000
k2 = 100
# pesos
w_inventario = 0.5
w_historia = 0.25
w_distancia = 0.85


def seleccion():
    pass

def fitness(data):
    global w_distancia, w_historia, w_inventario,k1,k2
    
    ct1 = (k1+ (inventario*w_inventario) - (distancia*w_distancia) - (historia*w_historia))/k2
    ct2 = (k1+ (10*w_inventario) - (5*w_distancia) - (4*w_historia))/k2
    print(ct1+ct2)
    
def ajuste_pesos():
    global w_distancia, w_historia, w_inventario
    w_inventario+=(-0.003)
    w_historia+=(0.004)
    w_distancia+=(0.015)

def mutacion():
    pass

def crossover():
    pass


if __name__ == "__main__":
    fitness(1)