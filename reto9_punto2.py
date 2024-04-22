def promedio (*args) -> float: #Función de argumentos no definidos para hallar promedio.
    suma : int = 0 #Se inicia variable suma en 0.
    for num in args: #Bucle que recorre la tupla args y para cada num...
        suma +=  num #La variable suma cambia su valor, sumándose a sí misma num.
    prom = suma/len(args) #El promedio es suma dividido la cantidad de números en args.
    return prom #devuelve 'prom'.

def promedio_multiplicativo(*args) -> float: #Función de argumentos no definidos para hallar promedio multiplicativo.
    mult : int = 1 #Se inicia variable mult en 1.
    for num in args: #Bucle que recorre la tupla args y para cada num...
        mult *=  num #La variable mult cambia su valor, multiplicándose a sí misma num.
    if mult <0: #Si el resultado de la multiplicación final es negativo...
        prom_mult=(-mult)**(1/len(args))*-1 #Se debe convertir en positivo multiplicándolo por menos, sacar la raíz respectiva del número de términos y al final volver a multiplicar por menos.
    else:
        prom_mult=mult**(1/len(args)) #Si el resultado de la multiplicación es positivo, solo se debe sacar la raíz respectiva al número de términos.
    return prom_mult #Se devuelve el resultado final de prom_mult.

def orden_ascendente(*args) -> list: #Función de argumentos no definidos para hallar orden ascendente.
    lista_orden=[] #Se crea una lista vacía.
    for num in args: #Bucle que recorre la tupla args y cada num lo añade a la lista creada antes.
        lista_orden.append(num)
    lista_orden.sort() #Se usa la función sort() para ordenar los valores de la lista.
    return lista_orden #Se devuelve la lista ordenada.

if __name__ == "__main__":
    #Se solicitan valores.
    a: float = float(input("Escriba el primer número real: "))
    b: float = float(input("Escriba el segundo número real: "))
    c: float = float(input("Escriba el tercer número real: "))
    d: float = float(input("Escriba el cuarto número real: "))
    e: float = float(input("Escriba el quinto número real: "))

    #Se evalúa e imprime el promedio de dos, tres, cuatro y cinco números, para observar la utilidad de la función sin argumentos definidos.
    print ("El promedio de los primeros dos números es: " , promedio(a,b))
    print ("El promedio de los primeros tres números es: " , promedio(a,b,c))
    print ("El promedio de los primeros cuatro números es: " , promedio(a,b,c,d))
    print ("El promedio de los cinco números es: " , promedio(a,b,c,d,e))

    #Se evalúa e imprime el promedio multiplicativo de dos, tres, cuatro y cinco números, para observar la utilidad de la función sin argumentos definidos.
    print ("El promedio multiplicativo de los primeros dos números es: " , promedio_multiplicativo(a,b))
    print ("El promedio multiplicativo de los primeros tres números es: " , promedio_multiplicativo(a,b,c))
    print ("El promedio multiplicativo de los primeros cuatro números es: " , promedio_multiplicativo(a,b,c,d))
    print ("El promedio multiplicativo de los cinco números es: " , promedio_multiplicativo(a,b,c,d,e))

    #Se evalúa e imprimen en orden los dos, tres, cuatro o cinco números, para observar la utilidad de la función sin argumentos definidos.
    print("Los dos primeros números ordenados de forma ascendente: ", orden_ascendente(a,b))
    print("Los tres primeros números ordenados de forma ascendente: ", orden_ascendente(a,b,c))
    print("Los cuatro primeros números ordenados de forma ascendente: ", orden_ascendente(a,b,c,d))
    print("Los cinco números ordenados de forma ascendente: ", orden_ascendente(a,b,c,d,e))





