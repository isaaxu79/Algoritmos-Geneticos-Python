import matplotlib.pyplot as plt
import numpy as np
import random

cant_genes_ind = 2
cant_tipo_gen = 10
tienda = {1:[7,3,10], 2:[6,3,8], 3:[4,5,3], 4:[10,5,4], 5:[12,10,2], 6:[3,8,6], 7:[5,8,1], 8:[8,9,2], 9:[9,12,0], 10:[12,12,2]}
functio = []
num_pieza_solicitadas = 5

# Poblacion inicial
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

# Constantes para el calculos de fitness
k1 = 1000
k2 = 100
# Pesos
w_inventario = 0.5
w_historia = 0.25
w_distancia = 0.85

def seleccion(generacion):
    print(".........................")
    #print(generacion)
    # alpha selection
    alpha = []
    alpha_data = 100
    alpha_index = 0
    fit_total=0
    for i in generacion:
        #print(generacion[i])
        calificacion = fitness(generacion[i][0])
        generacion[i][1] = calificacion
        if(calificacion < alpha_data):
            alpha_data = calificacion
            alpha = generacion[i]
            alpha_index = i
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
        #print(c)
        if numeros[0] < c[2]:
            beta = c
            break
    #print(generacion)
    gen_beta = generacion.get(beta[0])
    return [alpha,gen_beta]
    
def get_fit_total(gene):
    fito = 0
    for x in gene:
        fito+=gene[x][1]
    return fito

def generate_individuals(off_and_parents):
    arreglo = {0: [off_and_parents[0],0], 1:[off_and_parents[1],0], 2:[off_and_parents[2],0], 3:[off_and_parents[3],0]}
    for i in range(36):
        var = i+4
        tienda1 = random.randrange(10)+1
        tienda2 = random.randrange(10)+1
        while tienda1 == tienda2:
            tienda2 = random.randrange(10)+1
        arreglo.update({var:[[tienda.get(tienda1),tienda.get(tienda2)],0]})
    return arreglo
        
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
    inventario_2 = individuo[1][0]
    distancia_2 = individuo[1][1]
    historial_2 = individuo[1][2]
    ct1 = (k1+ (inventario_1*w_inventario) - (distancia_1*w_distancia) - (historial_1*w_historia))/k2
    ct2 = (k1+ (inventario_2*w_inventario) - (distancia_2*w_distancia) - (historial_2*w_historia))/k2
    return(ct1+ct2)
    
def ajuste_pesos():
    global w_distancia, w_historia, w_inventario
    if (w_inventario-0.003) > 0:
        w_inventario+=(-0.003)
    if (w_historia+0.004) < 1:
        w_historia+=(0.004)
    if (w_distancia+0.015) < 1:
        w_distancia+=(0.015)

def mutacion(son1x,son2x):
    rand = random.randrange(10)
    rand2 = random.randrange(10)
    if random.randrange(2) == 0:
        son1x[0] = tienda[random.randrange(10)+1]
        while son1x[0]==son1x[1]:
            son1x[0] = tienda[random.randrange(10)+1]
    else:
        son1x[1] = tienda[random.randrange(10)+1]
        while son1x[1]==son1x[0]:
            son1x[1] = tienda[random.randrange(10)+1]
    
    if random.randrange(2) == 0:
        son2x[0] = tienda[random.randrange(10)+1]
        while son2x[0]==son2x[1]:
            son2x[0] = tienda[random.randrange(10)+1]
    else:
        son2x[1] = tienda[random.randrange(10)+1]
        while son2x[1]==son2x[0]:
            son2x[1] = tienda[random.randrange(10)+1]
    #print(son1x, ".....", son2x)
    return [son1x,son2x]
    

def crossover(alpha, beta):
    off_spring_2 = [beta[0],alpha[1]]
    off_spring_1 = [alpha[0],beta[1]]
    # print("debug---",off_spring_1)
    # print("debug---",off_spring_2)
    data = mutacion(off_spring_1,off_spring_2)
    return [data[0],data[1], alpha, beta]

def generateGraphic(x):
    plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
    plt.xlabel("abscisa")   # Inserta el título del eje X
    plt.ylabel("ordenada")   # Inserta el título del eje Y
    plt.ioff()   # Desactiva modo interactivo de dibujo
    plt.legend()
    plt.show()   # Fuerza dibujo de datos de lista3

def busqueda(dato):
    for x in tienda:
        if dato == tienda[x]:
            return x

def fitness_final(individuo):
    global w_distancia, w_historia, w_inventario,k1,k2
    inventario_1 = individuo[0][0]
    distancia_1 = individuo[0][1]
    historial_1 = individuo[0][2]
    inventario_2 = individuo[1][0]
    distancia_2 = individuo[1][1]
    historial_2 = individuo[1][2]
    ct1 = (k1+ (inventario_1*w_inventario) - (distancia_1*w_distancia) - (historial_1*w_historia))/k2
    ct2 = (k1+ (inventario_2*w_inventario) - (distancia_2*w_distancia) - (historial_2*w_historia))/k2
    return [ct1,ct2]

if __name__ == "__main__":
    the_best_gen = seleccion(population) # return [0] = alpha, [1] = beta  SELECTION initial
    #print(the_best_gen)    
    for x in range(59):
        print("generacion ",x)
        off_springs_parents = crossover(the_best_gen[0][0],the_best_gen[1][0]) # CROSSOVER & MUTATION 
        functio.append(the_best_gen[0][1])
        #print(off_springs_parents[0])   
        new_population = generate_individuals(off_springs_parents)
        #print(new_population)
        the_best_gen = seleccion(new_population) #new selection
        ajuste_pesos()
    print("alfa final ", the_best_gen[0])

    tiendas_elect = fitness_final(the_best_gen[0][0])
    elegida = []
    if tiendas_elect[0] < tiendas_elect[1]:
        elegida.extend(the_best_gen[0][0][0])
        if elegida[0] < num_pieza_solicitadas:
            elegida.clear()
            elegida.extend(the_best_gen[0][0][1])
    else:
        elegida.extend(the_best_gen[0][0][1])
        if elegida[0] < num_pieza_solicitadas:
            elegida.clear()
            elegida.extend(the_best_gen[0][0][0])
    
    print("Tienda ",busqueda(elegida))
    generateGraphic(functio)