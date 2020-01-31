import matplotlib.pyplot as plt
import numpy as np
import random

cant_genes_ind = 2
cant_tipo_gen = 10
tienda = {1:[7,3,10], 2:[6,3,8], 3:[4,5,3], 4:[10,5,4], 5:[12,10,2], 6:[3,8,6], 7:[5,8,1], 8:[8,9,2], 9:[9,12,0], 10:[12,12,2]}

# poblacion inicial
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

# constantes para el calculos de fitness
k1 = 1000
k2 = 100
# pesos
w_inventario = 0.5
w_historia = 0.25
w_distancia = 0.85


def seleccion(generacion):
    
    # alpha selection
    alpha = []
    alpha_data = 100
    alpha_index = 0
    fit_total=0
    for i in generacion:
        calificacion = fitness(generacion[i][0])
        generacion[i][1] = calificacion
        if(calificacion < alpha_data):
            alpha_data = calificacion
            alpha = generacion[i]
            alpha_index = i
    #print("best and minimum: ",alpha, "-", alpha_index)
    generacion.pop(alpha_index)
    
    # beta selection
    fit_total= get_fit_total(generacion)
    beta_aux=[]
    beta = []
    gen_beta=[]
    aux =0
    for x in generacion:
        aux += (generacion[x][1]/fit_total)*100
        beta_aux.append([x,generacion[x][1],aux])
    numeros = [random.uniform(0,100) for x in range(1)]
    for c in beta_aux:
        if numeros[0] < c[2]:
            beta = c
            break
    gen_beta = generacion.get(beta[0])
    return [alpha,gen_beta]
    

def get_fit_total(gene):
    fito = 0
    for x in gene:
        fito+=gene[x][1]
    return fito


def generate_individuals():
    arreglo = {}
    for i in range(36):
        var = i+4
        tienda1 = random.randint(1, 10)
        tienda2 = random.randint(1, 10)
        if tienda1 == tienda2:
            tienda2 = compare_change(tienda1,tienda2)
        arreglo.update({var:[[tienda.get(tienda1),tienda.get(tienda2)],0]})
    print(arreglo)
        
def compare_change(x,y):
    y = random.randint(1, 10)
    if y != x:
        return y
    else:
        compare_change(x,y)


def fitness(individuo):
    global w_distancia, w_historia, w_inventario,k1,k2
    inventario_1 = individuo[0][0]
    distancia_1 = individuo[0][1]
    historial_1 = individuo[0][2]
    #print("inventario: ", inventario_1, "distancia: ", distancia_1, "historial: ", historial_1)
    inventario_2 = individuo[1][0]
    distancia_2 = individuo[1][1]
    historial_2 = individuo[1][2]
    #print("inventario: ", inventario_2, "distancia: ", distancia_2, "historial: ", historial_2)
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

def crossover(alpha, beta):
    off_spring_2 = [beta[0],alpha[1]]
    off_spring_1 = [alpha[0],beta[1]]
    print(off_spring_1)
    print(off_spring_2)


if __name__ == "__main__":
    the_best_gen = seleccion(population) # return [0] = alpha, [1] = beta
    print(the_best_gen)
    crossover(the_best_gen[0][0],the_best_gen[1][0])
