#ejercicio_1.1


class Cuadrado():
    print("Ingrese el largo del cuadrado")
    largo = int(input())
    def __init__(self, largo):
        self.largo = largo
    def area(self):
        area = (self.largo * self.largo)
        return area
    def perimetro(self):
        perimetro = (self.largo * 4)
        return perimetro
r1 = Cuadrado(2)
area = r1.area()
perimetro = r1.perimetro()
print("El area es : ", area)
print("El perimetro es:", perimetro)

class Rectangulo():
    print("Ingrese el ancho del rectangulo")
    ancho = int(input())
    print("Ingrese el alto del rectangulo")
    alto = int(input())
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        area = self.alto * self.ancho
        return area
    def perimetro(self):
        perimetro = (self.alto*2) + (self.ancho*2)
        return perimetro
r1 = Rectangulo(4,2)
area = r1.area()
perimetro = r1.perimetro()
print("El area es : ", area)
print("El perimetro es:", perimetro)

class Triangulo():
    print("Ingrese la base del triangulo")
    base = int(input())
    print("Ingrese la altura del triangulo")
    altura = int(input())
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        area = ((self.base * self.altura) / 2)
        return area
    #PITGORAS 
    def perimetro(self):
        perimetro = (self.base )
        return perimetro
r1 = Triangulo()#TAMPOCO SE QUE VA ADENTRO DEL PARENTESIS
area = r1.area()
perimetro = r1.perimetro()
print("El area es : ", area)
print("El perimetro es:", perimetro)
#FAlTA DEFINIR EL TIPO DE TRIANGULO 


class Circulo():
    print("Ingrese el radio del circulo")
    radio = int(input())
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        area = (3.14 * self.radio * self.radio)
        return area
    def perimetro(self):
        perimetro = (self.radio * 2 * 3.14)
        return perimetro
r1 = Circulo() #NO SE QUE VA EN LOS PARENTESIS
area = r1.area()
perimetro = r1.perimetro()
print("El area es : ", area)
print("El perimetro es:", perimetro)