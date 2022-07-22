
class Conversao:
    def __init__(self, dolar, real):
        self.dolar = dolar
        self.real = real

    def dolar_p_real(self):
        self.dolar = float(self.real * 5.40)
        print(f'Você tem {self.dolar} reais')

    def real_p_dolar(self):
        self.real = float(self.dolar / 5.40)
        print(f'Você tem {self.real} em dolar')

if __name__ == "__main___":
    dolar = input("Digite a quantia em dolar que vc tem: ")
    real = input("Digite a quantia em ral que vc tem: ")
    conversao = Conversao(dolar, real)

    conversao.dolar_p_real()
    conversao.real_p_dolar()

        
