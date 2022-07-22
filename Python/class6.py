
class Area:
    def __init__(self, area):
        self.area = area
        self.lata = 0
        self.preco = 0


    def calcular_lata(self):
        self.lata =  float(self.area) / 6
        print('Voçê deverá usar: {} latas'.format(self.lata))

    def calcular_preco(self):
        self.preco = float(self.lata) * 80
        print('Voçê pagará: {} reais'.format(self.preco))

if __name__ == "__main__":
    area1 = input("Digite a area pretendida para pintura em m2: ")
    area = Area(area1)
    area.calcular_lata()
    area.calcular_preco()
