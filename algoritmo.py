import matplotlib.pyplot as plt
import numpy as np

cant_genes_ind = 2
cant_tipo_gen = 10
tienda = {1:[7,3,10], 2:[6,3,8], 3:[4,5,3], 4:[10,5,4], 5:[12,10,2], 6:[3,8,6], 7:[5,8,1], 8:[8,9,2], 9:[9,12,0], 10:[12,12,2]}
population = {
  0:[[tienda[2],tienda[4]],0], 1:[[tienda[2],tienda[8]],0], 2:[[tienda[10],tienda[1]],0], 3:[[tienda[5],tienda[2]],0]
, 4:[[tienda[10],tienda[6]],0], 5:[[tienda[9],tienda[5]],0], 6:[[tienda[2],tienda[3]],0], 7:[[tienda[6],tienda[3]],0], 8:[[tienda[1],tienda[5]],0]
, 9:[[tienda[1],tienda[4]],0], 10:[[tienda[6],tienda[10]],0], 11:[[tienda[5],tienda[8]],0], 12:[[tienda[2],tienda[10]],0], 13:[[tienda[4],tienda[9]],0]
, 14:[[tienda[3],tienda[10]],0], 15:[[tienda[1],tienda[9]],0], 16:[[tienda[2],tienda[4]],0], 17:[[tienda[9],tienda[6]],0], 18:[[tienda[2],tienda[10]],0]
, 19:[[tienda[9],tienda[6]],0], 20:[[tienda[5],tienda[4]],0], 21:[[tienda[6],tienda[2]],0], 22:[[tienda[5],tienda[6]],0], 23:[[tienda[9],tienda[3]],0]
, 24:[[tienda[1],tienda[2]],0], 25:[[tienda[5],tienda[4]],0], 26:[[tienda[2],tienda[10]],0], 27:[[tienda[9],tienda[7]],0], 28:[[tienda[9],tienda[8]],0]
, 29:[[tienda[6],tienda[3]],0], 30:[[tienda[5],tienda[6]],0], 31:[[tienda[2],tienda[10]],0], 32:[[tienda[2],tienda[10]],0], 33:[[tienda[5],tienda[7]],0]
, 34:[[tienda[6],tienda[10]],0], 35:[[tienda[2],tienda[10]],0], 36:[[tienda[3],tienda[4]],0], 37:[[tienda[2],tienda[3]],0], 38:[[tienda[3],tienda[8]],0]
, 39:[[tienda[5],tienda[2]],0] }


k1 = 1000
k2 = 100
# pesos
w_inventario = 0.5
w_historia = 0.25
w_distancia = 0.85


def seleccion(generacion):
    for i in generacion:
        print(generacion[i])
        calificacion = fitness(generacion[i][0])
        generacion[i][1] = calificacion
    
    print(generacion)


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
    ct2 = (k1+ (inventario_2*w_inventario) - (distancia_2*w_distancia) - (historial_2*w_historia))/k2
    return(ct1+ct2)
    
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