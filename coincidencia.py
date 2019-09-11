import numpy as np
#funcion encargada de realizar la division del arreglo para realizar la comparación
def posiones(i):
    if i < 30:
        inf = 0
        sup = i + 1
        
        inf1 = 30 - (i+1)
        sup1 = 30
    elif i >= 150 :
        inf = i -30
        sup = 150
        
        inf1 = 0
        sup1 = 30 - (i - 120)
    else:
        inf = i-30
        sup = i 
        
        inf1 = 0
        sup1 = 30
        
    return inf, sup, inf1, sup1

# Generación de arreglos
s1 = np.random.randint(4, size = 150)
s2 = np.random.randint(4, size = 30)
# Para el ejercicio se tendra la siguiente convención:
## 0 -> A
## 1 -> C
## 2 -> G
## 3 -> T

puntaje = np.zeros((180, 2), dtype=int)   # Almacena en número de coincidencias

# Vector puntaje
for i in range(180):
    ## Estructura de desiciones de las posisiones a comparar en el arreglo
    inf, sup, inf1, sup1 = posiones(i)    
    # Toma los valores a comparar
    a = s1[inf: sup]
    b = s2[inf1: sup1]     
    # Realiza la cmparación
    c = (a==b)    
    # Guarda el número de coincidencias
    puntaje[i] = [i, np.sum(c)]
    
# impresiones
print("Lista de coincidencia, posición y número de coincidencias ")
print(puntaje)

# Matrices
print("La secuencia con mayor número de coincidencias es:",puntaje[::, 1].max())
inf, sup, inf1, sup1 = posiones(puntaje[::, 1].argmax())
print("En la posición:",puntaje[::, 1].argmax())
#Saca las possiciones de las secuencias a imprimir 

print("La secuencia de coincidencia es:")
#Impresion de las secuencias con mayor coincidencia 
print(s1[inf:sup])
print(s2[inf1:sup1])    
