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