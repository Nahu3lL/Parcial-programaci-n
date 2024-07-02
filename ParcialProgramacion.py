go = True

linea1 = [0, 0, 0, 0, 0]    # }
linea2 = [0, 0, 0, 0, 0]    #  > Se inician tres arrays con 5 valores funcionando como las tres lineas con 5 colectivos en cada una 
linea3 = [0, 0, 0, 0, 0]    # }

intL = 0
intC = 0
intG = 0

maxCH1 = 0
maxCH2 = 0
maxCH3 = 0
maxCHT = 0
maxLNC = 0

gananciaLN1 = 0
gananciaLN2 = 0
gananciaLN3 = 0

totalGananciaGeneal = 0

lineaMAX = 0
lineaMAXTXT = ""
cocheMAX = 0
cocheMAXTXT = ""

while go:       # go se inicializa como 'True' lo que genera un bucle infinito hasta que se interrumpa el procedimiento
    intL = int(input("Ingrese el número de línea (1-3): "))
    if intL == 0:       # Interrupción según consigna
        go = False
        print("Sistema cerrado")
        break       # El 'break' es la interrupción mencionada en la linea 28. Corta el bucle donde sea que se encuentre escrito
    elif intL in [1, 2, 3]:     # Esta condición es el rango definido en la consigna "...número de línea (de 1 a 3)..."
        intC = int(input("Ingrese el número de colectivo (1-5): "))
        intG = int(input("Ingrese la ganancia del vehículo ingresado: "))
        
        if intL == 1:
            linea1[intC - 1] += intG        # Autosumador el cual selecciona la posición del colectivo que le corresponde en el array
            gananciaLN1 += intG         # Autosumador de ganancia por linea
            if gananciaLN1 > lineaMAX:          # Comparador para obtener la linea que más recaudó
                lineaMAXTXT = "linea 1"
                lineaMAX = gananciaLN1
        elif intL == 2:
            linea2[intC - 1] += intG
            gananciaLN2 += intG
            if gananciaLN2 > lineaMAX:
                lineaMAXTXT = "linea 2"
                lineaMAX = gananciaLN2
        elif intL == 3:
            linea3[intC - 1] += intG
            gananciaLN3 += intG
            if gananciaLN3 > lineaMAX:
                lineaMAXTXT = "linea 3"
                lineaMAX = gananciaLN3

        totalGananciaGeneal += intG         # Autosumador de ganancia general
    elif intL == "":        # Combate un bug en el que el sistema falla si no hay input
        print("Valor no definido en el rango establecido, vuelva a intentarlo")
    else:       # Contempla valores fuera de los rangos definidos
        print("El valor ingresado excede las opciones disponibles")

maxCH1 = max(linea1)    # }
maxCH2 = max(linea2)    #  > Obtenemos los valores máximos de cada linea
maxCH3 = max(linea3)    # }

maxCHT = max(maxCH1, maxCH2, maxCH3)    # Obtenemos el valor máximo inter-lineal

if maxCHT == maxCH1:        # Comparador para obtener la linea de colectivo donde está el coche con mayor ganancia
    cocheMAX = linea1.index(maxCHT) + 1
    maxLNC = "linea 1"
elif maxCHT == maxCH2:
    cocheMAX = linea2.index(maxCHT) + 1
    maxLNC = "linea 2"
else:
    cocheMAX = linea3.index(maxCHT) + 1
    maxLNC = "linea 3"

x = 0
while x < 3:        # Loop para x de 0 a 2 para obtener el número de linea (en el cuerpo se le suma 1 para poder hacer una relacion con la misma)
    z = 0
    while z < 5:        # Loop para z de 0 a 5 para obtener la posición y numero de coche
        if x == 0:
            print(f"Ganancia de la línea {x + 1} para el coche {z + 1}: ", linea1[z])
        elif x == 1:
            print(f"Ganancia de la línea {x + 1} para el coche {z + 1}: ", linea2[z])
        elif x == 2:
            print(f"Ganancia de la línea {x + 1} para el coche {z + 1}: ", linea3[z])
        z += 1      # autosumador para poder continuar con la secuencia
    x += 1

print("Total ganancia de la línea 1: ", gananciaLN1)
print("Total ganancia de la línea 2: ", gananciaLN2)
print("Total ganancia de la línea 3: ", gananciaLN3)

print("Suma total de ganancias: ", totalGananciaGeneal)

print(f"La línea que más recaudó fue la {lineaMAXTXT} con ${lineaMAX}")
print(f"El coche que más facturó fue el {cocheMAX} de la {maxLNC} con ${maxCHT}")