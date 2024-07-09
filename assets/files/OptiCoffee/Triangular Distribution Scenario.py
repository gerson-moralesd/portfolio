
'''
Resolviendo retos logísticos con optimización y simulación
Departamento de Ingeniería Industrial
Facultad de Ingeniería
Universidad de los Andes
'''

# importación de librerías
import math
import pulp as lp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as cm


### lectura de datos
tabla1 = pd.read_excel('./data.xlsx', sheet_name = 'clientes', index_col = [0])
tabla2 = pd.read_excel('./data.xlsx', sheet_name = 'bodegas', index_col = [0])


### conjuntos
# TODO: definir los conjuntos
B = [i for i in tabla2.index]
C = [j for j in tabla1.index]


print(f'El número de bodegas es: {len(B)}')
print(f'El número de clientes es: {len(C)}')

### parámetros
demandaMin = {j : tabla1.iloc[j-1, 2] for j in C}   
demandaMax = {j : tabla1.iloc[j-1, 3] for j in C}    
demandaModa = {j : tabla1.iloc[j-1, 4] for j in C}     

d = {j : round((demandaMin[j]+demandaMax[j]+demandaModa[j])/3,2) for j in C}    # demanda mensual esperada (ton de café)


# TODO: carga de parámetros de costo fijo, capacidad y costo de transporte unitario
f = {i : tabla2.iloc[i-1, 2] for i in B}
k = {i : tabla2.iloc[i-1, 3] for i in B}
alpha = 0.3


ubicacionClientes = {j: (tabla1.iloc[j-1, 0], tabla1.iloc[j-1, 1]) for j in C}      # coordenadas clientes
ubicacionBodegas = {i: (tabla2.iloc[i-1, 0], tabla2.iloc[i-1, 1]) for i in B}       # coordenadas bodegas 

def calcular_distancia(loc1, loc2):
    # calcula la distancia euclideana entre loc1 y loc2
    dx = loc1[0] - loc2[0]
    dy = loc1[1] - loc2[1]
    return round(math.sqrt(dx*dx+dy*dy),2)

h = {(i,j): calcular_distancia(ubicacionBodegas[i], ubicacionClientes[j]) for i in B for j in C}            # distancia en kilómetros

# TODO: carga de parámetros costo de transporte
c = {(i,j): alpha*h[i,j]*d[j] for i in B for j in C} 



### visualización

plt.scatter([ubicacionClientes[j][0] for j in C], [ubicacionClientes[j][1] for j in C], c='forestgreen', marker='x', label='Cliente')
plt.scatter([ubicacionBodegas[i][0] for i in B], [ubicacionBodegas[i][1] for i in B],  c='saddlebrown', marker='s', label='Bodega')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Ubicación de clientes y bodegas', fontsize=14)       # título del gráfico
plt.xlabel('Coordenada $x$')                                    # etiquetas del los ejes
plt.ylabel('Coordenada $y$')
plt.xlim(-5,210)                                                # límites de los ejes
plt.ylim(-5, 110)
plt.grid(alpha = 0.2)
plt.savefig('./resultados/ubicaciones.png', dpi=1200, format='png', bbox_inches='tight')
plt.show()

### modelo de optimización

# TODO: definir el problema y el sentido de optimización en PuLP 
prob = lp.LpProblem(name = 'OptiCoffee', sense = lp.LpMinimize)

### variables de decisión
# TODO: definir las variables de decisión
y = {i : lp.LpVariable(name = f'y_{i}', lowBound = 0, cat = lp.LpBinary) for i in B}
x = {(i,j): lp.LpVariable(name = f'x_{(i,j)}', lowBound = 0, cat = lp.LpBinary) for i in B for j in C}

### restricciones
# TODO: agregar las restricciones al modelo
# 1. cada cliente queda asignado a una bodega

for j in C:
    prob += sum(x[i,j] for i in B) == 1

# 2. no se excede la capacidad de cada bodega

for i in B:
    prob += sum(d[j]*x[i,j] for j in C) <= k[i]

    
# 3. si no opera la bodega, entonces no atiende ningún cliente

for i in B:
    for j in C:
        prob += x[i,j] <= y[i]

### objetivo: minimizar los costos
# TODO: agregar la función objetivo
prob += sum(f[i]*y[i] for i in B) + sum(c[i,j]*x[i,j] for i in B for j in C)



### resolver
# TODO: resolver y recuperar información del optimizador
prob.solve()
print(f'Status:  {lp.LpStatus[prob.status]}')
print(f'Objetivo: {lp.value(prob.objective)}')
print(f'Costo fijo: {sum(f[i]*y[i].value() for i in B)}')
print(f'Costo de transporte: {sum(c[i,j]*x[i,j].value() for i in B for j in C)}')
print(f'Número de bodegas operando: {sum(y[i].value() for i in B)}')


### resultados
resultados = []
bodegasOperando = []
bodegasNoOperando = []
clientesAtendidos = {}

for i in B:
    if y[i].value() == 1:                               # la bodega opera
        bodegasOperando.append(i)
        fila = []
        fila.append(i)
        cust = []
        capacidadUsada = 0
        costoTransporte = 0
        for j in C:
            if x[i,j].value() == 1:                     # la bodega i atiende al cliente j
                cust.append(int(j))
                capacidadUsada += d[j]
                costoTransporte += c[i,j]
        fila.extend([cust, len(cust), capacidadUsada, k[i], round(capacidadUsada/k[i],3)*100, f[i], round(costoTransporte, 3)])
        resultados.append(fila)
        clientesAtendidos[i] = cust
    else:                                               # la bodega no opera
        bodegasNoOperando.append(i)
        
df = pd.DataFrame(resultados, columns = ['Id', 'Clientes atendidos', '# de clientes atendidos', 'Capacidad Usada', 'Capacidad Total', 'Usada/Total', 'Costo fijo', 'Costo de transporte'])      
df.to_excel('./resultados/resultadosOptimizacion.xlsx', index = False)


### gráficos (plots)
colors = [cm.to_hex(plt.cm.tab20(i)) for i in range(len(B)+1)]
# https://matplotlib.org/stable/gallery/color/named_colors.html 

# red de abastecimiento
plt.scatter([ubicacionClientes[j][0] for j in C], [ubicacionClientes[j][1] for j in C], c='blue', marker='x', label='Cliente')
plt.scatter([ubicacionBodegas[i][0] for i in bodegasOperando], [ubicacionBodegas[i][1] for i in bodegasOperando],  c='orange', marker='s', label='Bodega operando')
plt.scatter([ubicacionBodegas[i][0] for i in bodegasNoOperando], [ubicacionBodegas[i][1] for i in bodegasNoOperando],  c='gray', marker='s', label='Bodega no operando')
plt.legend(bbox_to_anchor=(1.02, 1))
plt.xlim(-5,210)                                                    # límites de los ejes
plt.ylim(-5, 110)
plt.grid(alpha = 0.2)
for i in bodegasOperando:
    for j in C:
        if x[i,j].value() == 1:
            plt.plot([ubicacionBodegas[i][0], ubicacionClientes[j][0]], [ubicacionBodegas[i][1], ubicacionClientes[j][1]], linestyle='dashed', color = colors[i])
        
# TODO: agregarle al gráfico los títulos 

plt.savefig('./resultados/redDistribucion.png', dpi=1200, format='png', bbox_inches='tight')
plt.show()

# costos
# TODO: crear un gráfico de torta que muestre la segmentación de costos
costos = [sum(c[i,j]*x[i,j].value() for i in B for j in C), sum(f[i]*y[i].value() for i in B)]
etiquetas = ['Costo de transporte', 'Costo fijo']


plt.savefig('./resultados/segmentacionCostos.png', dpi=1200, format='png')
plt.show()

# operación de las bodegas
capacidadUsada = [sum(d[j]*x[i,j].value() for j in C) for i in bodegasOperando]
capacidadRemanente = [k[i] - sum(d[j]*x[i,j].value() for j in C) for i in bodegasOperando]
plt.bar([i for i in range(1,len(bodegasOperando)+1)], capacidadUsada, color='blue', label = 'Capacidad usada')
plt.bar([i for i in range(1,len(bodegasOperando)+1)], capacidadRemanente, bottom=capacidadUsada, color='green', label = 'Capacidad remanente')
plt.legend(bbox_to_anchor=(1.02, 1))
plt.xticks(ticks = [i for i in range(1,len(bodegasOperando)+1)], labels = bodegasOperando)
# TODO: agregarle los títulos al gráfico


plt.savefig('./resultados/operacionBodegas.png', dpi=1200, format='png', bbox_inches='tight')
plt.show()

### SIMULACIÓN

# importación de librerías
from scipy import stats          #para cálculo de probabilidades
import numpy as np
# TODO: instalar librerías (en caso de ser necesario)


# generación de demandas aleatorias para todos los clientes
n_exps = 5000                   # cantidad de veces que se corre la simulación
realizacionDemanda = {}
# TODO: generar realizaciones de la demanda de cada cliente
for j in C:
    aleatorio = np.random.triangular(demandaMin[j], demandaModa[j], demandaMax[j], size = n_exps)
    realizacionDemanda[j] = aleatorio


# diccionario y lista para la simulación
costosTotales = []
demandasTotales = {}


# evaluación de los costos
# TODO: mostrar la distribución de los costos totales
for n in range(n_exps):
    costoTotal = 0
    for i in bodegasOperando:
        costoTotal += f[i]
        costoTotal += sum(alpha*realizacionDemanda[j][n]*h[i,j] for j in clientesAtendidos[i])
    costosTotales.append(costoTotal)
    


Costo= pd.DataFrame()
Costo['Histograma de los costos totales'] = costosTotales 
Costo.hist(bins=30, color='#ff008b')
plt.xlabel('Costo total mensual (miles de COP)',fontsize=12)
plt.ylabel('Frencuencia',fontsize=12)
plt.savefig('./resultados/histogramaCostoTotal.png', dpi=1200, format='png')
plt.show()

# TODO: estadísticas descriptivas del costo total
print(Costo.describe())

# TODO: mostrar la distribución de la demanda total satisfecha por una bodega de interés
bodegaInteres = 3
demandaTotal_bodegaInteres = [sum(realizacionDemanda[j][n] for j in clientesAtendidos[bodegaInteres]) for n in range(n_exps)]

Demanda = pd.DataFrame()
Demanda[f'Histograma de la demanda total de la bodega {bodegaInteres}']  = demandaTotal_bodegaInteres
Demanda.hist(bins=30, color='#01d6fe')
plt.axvline(x=k[bodegaInteres], color='r', linestyle='--')
plt.xlabel('Demanda mensual (ton de café)',fontsize=12)
plt.ylabel('Frencuencia',fontsize=14)
plt.savefig(f'./resultados/histogramaDemanda_bodega{bodegaInteres}.png', dpi=1200, format='png')


# TODO: obtener estadísticas descriptivas para la bodega de interés
print(Demanda.describe())


# se crea la figura con 8 subplots: uno para cada bodega operando
fig, subplots = plt.subplots(figsize=(16,8),nrows=2,ncols=4,sharex=True,sharey=True)
plt.subplots_adjust(wspace=0.1,hspace=0.15)

# ordenar las bodegas que están operando, de acuerdo a su capacidad (en toneladas)
dict_capacidad = {i : k[i] for i in bodegasOperando}
bodegasOperando = list(sorted(dict_capacidad,key=dict_capacidad.get))

# cada uno de los subplots se asigna a alguna de las bodegas, para llamarlas por Id. en los histogramas
axes = {}; coords = {}
j = 0; p = 0
for i in bodegasOperando:
    coords[i] = (j,p)
    axes[i] = subplots[j,p]
    if p == 3: j = 1; p = 0
    else: p += 1


Demanda = pd.DataFrame()
# recorrido por todas las bodegas operando
for i in bodegasOperando:

    demandaTotal_bodega = [sum(realizacionDemanda[j][n] for j in clientesAtendidos[i]) for n in range(n_exps)]
    demandasTotales[i] = demandaTotal_bodega
    
    Demanda[f'Histograma de la demanda total de la bodega {i}'] = demandasTotales[i]
    # Histograma de la demanda total para cada bodega
    axes[i].hist(demandasTotales[i],bins=30, color='#01d6fe')
    axes[i].axvline(x=k[i], color='r', linestyle='--')
    axes[i].set_xlim(40,110)
    axes[i].set_title(f'Bodega {i}',fontsize=12)
    if coords[i][0] == 0:
        axes[i].text(x=k[i]+12,y=425,s=f'Capacidad:\n{k[i]} ton.',va='center',ha='center',color='red')
    else:
        axes[i].text(x=k[i]-10,y=425,s=f'Capacidad:\n{k[i]} ton.',va='center',ha='center',color='red')
    if coords[i][0] == 1:
        axes[i].set_xlabel('Demanda mensual (ton. café)',fontsize=12)
    if coords[i][1] == 0:
        axes[i].set_ylabel('Frecuencia',fontsize=12)
fig.suptitle('Distribución de demanda total por cada bodega operando',fontsize=18)
plt.savefig('./resultados/histogramasDemanda.png', dpi=1200, format='png')


# métricas de probabilidad de interés para demanda, capacidad y costos

# parámetros
sig = 5             # nivel de significancia para el intervalo (en porcentaje)



