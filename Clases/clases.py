import math

class Circulo():

    def __init__(self, radio):
        self.radio = radio
        if radio <= 0:
            raise ValueError("Solo se permiten crear circulos con radio mayor a 0(cero)")
        
        print("El radio de su circulo creado es: ", self.radio)
    
    def modificar_radio(self,radio):
        self.radio = radio
        if radio <= 0:
            raise ValueError("Solo se permiten crear circulos con radio mayor a 0(cero)")

        print("El nuevo radio de su circulo es: ", self.radio)


    def obtener_area(self):
        area = (math.pi * (math.pow (self.radio, 2)))
        print("El area del circulo es: ", area)

        return area

    def obtener_perimetro(self):
        perimetro = (2 * math.pi * self.radio) 
        print("El perimetro del circulo es: ",perimetro)

        return perimetro

    def multiplicar_circulo(self, numero):
        if numero <= 0:
            raise ValueError("Solo se puede multiplicar el circulo por un numero mayor a 0(cero)")

        circulo = Circulo(self.radio * numero)

        return circulo


    
    
