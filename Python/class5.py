'''EX12.  Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    •Álcool: •até 20 litros, desconto de 3% por litro •acima de 20 litros, desconto de 5% por litro
    •Gasolina: •até 20 litros, desconto de 4% por litro •acima de 20 litros, desconto de 6% por litro 
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
    A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90. '''

class Posto:
    def __init__(self, quantidade=0):
        self.quantidade = quantidade

    def valor_a_pagar_gasol(self):
        self.valor_pago = self.quantidade * 2.5
        print(f"Valor do abastecimento sem desconto: {self.valor_pago}")

    def valor_a_pagar_alcool(self):
        self.valor_pago = self.quantidade * 1.90
        print(f"Valor do abastecimento sem desconto: {self.valor_pago}")

    def alcool(self):
        if self.quantidade <= 20:
            self.valor_desconto = self.valor_pago * 0.03 
            print(f"Seu desconto é de: {self.valor_desconto}")
            self.valor_pago_desconto = self.valor_pago - self.valor_desconto
            print(f"Você deverá pagar (desconto vigente): {self.valor_pago_desconto} ")
        elif self.quantidade > 20:
            self.valor_desconto = self.valor_pago * 0.05
            print(f"Seu desconto é de: {self.valor_desconto}")
            self.valor_pago_desconto = self.valor_pago - self.valor_desconto
            print(f"Você deverá pagar (desconto vigente): {self.valor_pago_desconto} ")
        else:
            pass

    def gasolina(self):
        if self.quantidade <= 20:
            self.valor_desconto = self.valor_pago * 0.04
            print(f"Seu desconto é de: {self.valor_desconto}")
            self.valor_pago_desconto = self.valor_pago - self.valor_desconto
            print(f"Você deverá pagar (desconto vigente): {self.valor_pago_desconto} ")
        elif self.quantidade > 20:
            self.valor_desconto = self.valor_pago * 0.06
            print(f"Seu desconto é de: {self.valor_desconto}")
            self.valor_pago_desconto = self.valor_pago - self.valor_desconto
            print(f"Você deverá pagar (desconto vigente): {self.valor_pago_desconto} ")
            
        else:
            pass
    
if __name__ == '__main__':
    ...


        
    
    
    



