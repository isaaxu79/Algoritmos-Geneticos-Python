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


def seleccion(generacion):
    for i in generacion:
        print(generacion[i][0])
        calificacion = fitness(generacion[i][0])

def fitness(individuo):
    global w_distancia, w_historia, w_inventario,k1,k2
    inventario_1 = individuo[0][0]
    distancia_1 = individuo[0][1]
    historial_1 = individuo[0][2]
    print("inventario: ", inventario_1, "distancia: ", distancia_1, "historial: ", historial_1)
    inventario_2 = individuo[1][0]
    distancia_2 = individuo[1][1]
    historial_2 = individuo[1][2]
    print("inventario: ", inventario_2, "distancia: ", distancia_2, "historial: ", historial_2)
    ct1 = (k1+ (inventario_1*w_inventario) - (distancia_1*w_distancia) - (historial_1*w_historia))/k2
    ct2 = (k1+ (inventario_1*w_inventario) - (distancia_1*w_distancia) - (historial_1*w_historia))/k2
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
    #print(population)
    seleccion(population)