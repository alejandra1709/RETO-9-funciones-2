# RETO 9 funciones 2
>## 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
>## Se desarrolló:
>* Función lambda para volúmen
>* Función lambda para área superficial
>* Función lambda para cantidad de carne
>
>***RETO 6 - PUNTO 1 - Dada la figura de la imagen, desarrolle:***
>
>* Una función matemática para calcular el volumen y el área superficial.
>
>* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
>
>* Revise como utilizar el valor de pi usando import math y math.pi
<div align="center">
  <img src="https://i.postimg.cc/kg7bRdXK/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png">
</div>

>***Funciones área superficial y perímetro, como lambdas:***

```python
import math #Se importa math.
pi=math.pi #Se asigna el valor de pi, traido de math, a la variable 'pi'.
if __name__ == "__main__":
    #Se solicitan datos.
    radio_esfera: float = float (input("Ingrese el radio de la esfera en centímetros: ")) 
    radio_cono: float = float (input("Ingrese el radio del cono en centímetros: "))
    altura_cono: float = float (input("Ingrese la altura del cono en centímetros: "))
    altura_inclinacion=(radio_cono**2+altura_cono**2)**0.5 #Se calcula la altura de inclinación del cono.

    volumen = (lambda a,b,c : ((pi*a**2*b)/3)+(4/3*pi*c**3))(radio_cono,altura_cono,radio_esfera) #Se halla el volúmen por medio de una función lambda que recibe tres argumentos y entrega el volúmen de la esfera y cono sumados.
    print("El volúmen de la figura es",volumen,"centímetros cúbicos") #Se imprime el volúmen.

    area = (lambda a,b,c : ((pi*a*b)+(pi*b**2))+(4*pi*c**2))(altura_inclinacion,radio_cono,radio_esfera) #Se halla el área superficial por medio de una función lambda que recibe tres argumentos y entrega el área superficial de la esfera y el cono sumadas.
    print("El área superficial de la figura es de",area,"centímetros cuadrados") #Se imprime el área superficial.
```
>***RETO 6 - PUNTO 3 - Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.***
>***Tercera función lambda.***
```python
if __name__ == "__main__":
    #Se solicitan datos.
    gallinas: int = int(input("Ingrese el número de gallinas: "))
    gallos: int = int(input("Ingrese el número de gallos: "))
    pollitos: int = int(input("Ingrese el número de pollitos: "))

    kilos_carne = (lambda a,b,c : a*6+b*7+c*1)(gallinas,gallos,pollitos) #Función lambda que recibe tres argumentos y entrega el resultado de la cantidad de carne.
    print("La cantidad de carne de aves es de",kilos_carne,"kilogramos") #Se imprime la cantidad de carne.
```
>## 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
>## Se desarrolló:
>* Función con argumentos no definidos para promedio
>* Función con argumentos no definidos para promedio multiplicativo
>* Función con argumentos no definidos para orden ascendente
>
>***RETO 6 - PUNTO 7 - Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:***
>* El promedio
>
>* El promedio multiplicativo
>
>* Ordenar los números de forma ascendente

```python
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
```
>## 3. Escriba una función recursiva para calcular la operación de la potencia.

```python
def potencia_recursiva(base:int,exponente:int )-> int: #función que recibe dos argumentos enteros y devuelve un entero.
  # Caso base 
  if exponente == 0: #Si el exponente es 0, se devuelve 1 inmediatamente.
    return 1
  else:
    # Condición de la función recursiva
    pot=base*potencia_recursiva(base, exponente-1) #Si el exponente no es cero, se llama la función potencia_recursiva dentro de la misma función, pero ahora se dan como argumentos base y exponente-1 y esto se multiplica por base.
    return pot #Se devuelve el valor final de pot.

#mejor explicación:
#2**6
#2*2**5
#2*2*2**4
#2*2*2*2**3
#2*2*2*2*2**2
#2*2*2*2*2*2**1
#2*2*2*2*2*2*2**0 --> se debe llegar hasta el caso base en donde el exponente es 0.

if __name__ == "__main__":
  #Se solicitan datos.
  base = int(input("Ingrese el número que será la base de la operación de potencia: "))
  exponente = int(input("Ingrese el número que será el exponente de la operación de potencia: "))
  potencia = potencia_recursiva(base,exponente) #Se evualúa la función potencia_recursiva con los datos ingresados como argumentos.
  print("El resultado de",base,"**",exponente,"es",potencia) #Se imprime el resultado.
```
>## 4. Utilice la plantilla de code para contar el tiempo, realice pruebas para calcular fibonacci con iteración o con recursión y determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

```python
import time #Se importa time.

def fibonacci(n : int )-> int: #Función que recibe entero y entrega entero.
  if n <=1:
    # caso base
    return 1 #Si se solicita el término 1 o 0 se devuelve inmediatamente 1.
  else:
    # condición de la función recursiva
    return fibonacci(n-1)+fibonacci(n-2)  #Se devuelve el valor del término solicitado en la serie, evaluando la función fibonacci para los dos números anteriores y sumando los resultados.
#Se inician timer y num en 0
timer=0 
num = 0
while timer<=10: #Se establece que el "tiempo significativo" es más de 10 segundos, así que se hace el cáculo para los números que tome menos de 10 segundos.
    start_time = time.time() #Tiempo de inicio.
    # instrucciones sobre las cuales se quiere medir tiempo de ejecución
    serie_fibonacci = fibonacci(num) #Se evalúa la función fibonacci con num.
    print("El número de la serie de Fibonacci en la posición",num,"es",serie_fibonacci)
    end_time = time.time() #Tiempo final.
    timer = end_time - start_time #Tiempo que tomó hallar el número en la posición.
    print(timer) #Se imprime el tiempo.
    num+=1 #Se suma 1 a num para continuar con el siguiente número.
print("Teniendo en cuenta que se toma como tiempo significativo 10 segundos, el tiempo empieza a ser significativo en el término",num-1,"de la serie.")
#Sin embargo, se puede notar que hasta el término 35 el tiempo para calcular cada número de la serie aumenta de a pocos milisegundos, y, desde el término 36 se inicia a aumentar de manera más drástica.
```
>## 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo
<div align="center">
  <img src="https://i.postimg.cc/QMRshVQL/Captura-de-pantalla-2024-04-22-171701.png">
</div>

>## 6. Cosas de adultos....ir a linkedin y crear perfil....
[Mi Perfil de LinkedIn ](https://www.linkedin.com/in/alejandra-landines-806617305/)
