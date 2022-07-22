###Faça   um   Programa   que   pergunte   quanto   você   ganha   por   hora   e   o   número   de   horas trabalhadas no mês.
### Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
### 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido. 

class Salario:
    def __init__(self, salario_hora, horas_mes, salario_bruto, valor_inss, valor_sindicato, descontos, valor_salario_liquido):
        self.salario_hora = salario_hora
        self.horas_mes = horas_mes
        self.salario_bruto = salario_bruto
        self.valor_inss = valor_inss
        self.valor_sindicato = valor_sindicato
        self.descontos = descontos
        self.valor_salario_liquido = valor_salario_liquido

    def salario_mensal_bruto(self):
        self.salario_bruto = float(self.salario_hora) * float(self.horas_mes)
        print("-----------")
        print("Seu salário bruto é de: {}\n".format(self.salario_bruto))

    def desconto_inss(self):
        self.valor_inss = float(self.salario_bruto) * 0.11
        print("-----------")
        print("Seu desconto INSS é no valor de: {}\n".format(self.valor_inss))

    def desconto_sindicato(self):
        self.valor_sindicato = float(self.salario_bruto) * 0.05
        print("-----------")
        print("Seu desconto do Sindicado é no valor de: {}\n".format(self.valor_sindicato))

    def descontos_somados(self):
        self.descontos = float(self.valor_inss) + float(self.valor_sindicato)
        print("-----------")
        print("O total de descontos é no valor de: {}\n".format(self.descontos))

    def salario_liquido(self):
        self.valor_salario_liquido = float(self.salario_bruto) - float(self.descontos)
        print("-----------")
        print("Seu salário liquido é de: {}\n".format(self.valor_salario_liquido))
        if self.valor_salario_liquido >= 2300:
            print("Você deverá declarar seu IR")
        else:
            print("Você não precisa declarar seu IR")

if __name__ == '__main__':
    salario_bruto = ''
    valor_inss = ''
    valor_sindicato = ''
    descontos = ''
    valor_salario_liquido = ''
    salario_hora = int(input("Quando você ganha por hora trabalhada?"))
    horas_mes = int(input("Quantas horas trabalhadas por mês?"))
    user = Salario(salario_hora, horas_mes, salario_bruto, valor_inss, valor_sindicato, descontos, valor_salario_liquido)
    user.salario_mensal_bruto()
    user.desconto_inss()
    user.desconto_sindicato()
    user.descontos_somados()
    user.salario_liquido()
        

