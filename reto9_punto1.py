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

    #Se solicitan datos.
    gallinas: int = int(input("Ingrese el número de gallinas: "))
    gallos: int = int(input("Ingrese el número de gallos: "))
    pollitos: int = int(input("Ingrese el número de pollitos: "))

    kilos_carne = (lambda a,b,c : a*6+b*7+c*1)(gallinas,gallos,pollitos) #Función lambda que recibe tres argumentos y entrega el resultado de la cantidad de carne.
    print("La cantidad de carne de aves es de",kilos_carne,"kilogramos") #Se imprime la cantidad de carne.

