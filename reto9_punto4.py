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