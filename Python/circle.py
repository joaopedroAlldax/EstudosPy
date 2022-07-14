
class Circle:
    def __init__(self, para, comprimento, diametro):
        self.raio = para
        self.comprimento = comprimento
        self.diametro = diametro

    def calcular_raio(self):
        self.raio = float(self.comprimento) / (2 * 3.14)
        print(f'o raio calculado é: {self.raio}')

    def calculo_diametro(self):
        self.diametro = 2 * self.raio
        print(f'O valor do diametro é: {self.diametro}')



if __name__ == "__main__":
    diametro = 0
    raio = 0
    comprimento = input("qual o comprimento do circulo? ")
    circulo1 = Circle(raio, comprimento, diametro)
    circulo1.calcular_raio()
    circulo1.calculo_diametro()


        
