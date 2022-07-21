'''EX11. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são: •"Telefonou para a vítima?" •"Esteve no local do crime?" •"Mora perto da vítima?" •"Devia para a vítima?" •"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classifi cada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''

class Crime:
    def __init__(self):
        self.qnt_positivo = 0

    def fazer_pergunta(self):
        self.pergunta = print("Telefonou para a vítima?")
        self.resposta1 = input("Resposta: [S/N] ")
        print("--------")
        self.pergunta = print("Esteve no local do crime?")
        self.resposta2 = input("Resposta: [S/N] ")
        print("--------")
        self.pergunta = print("Mora perto da vítima?")
        self.resposta3 = input("Resposta: [S/N] ")
        print("--------")
        self.pergunta = print("Devia para a vítima?")
        self.resposta4 = input("Resposta: [S/N] ")
        print("--------")
        self.pergunta = print("Já trabalhou com a vítima?")
        self.resposta5 = input("Resposta: [S/N] ")
        print("--------")
        lista_resposta = [self.resposta1, self.resposta2, self.resposta3, self.resposta4, self.resposta5]
        for i in lista_resposta:
            if i == "S":
                self.qnt_positivo +=1
            else:
                pass

    def julgamento(self):
        if self.qnt_positivo < 2:
            print(f'Você é inocente')
        elif self.qnt_positivo == 2:
            print(f'Você é suspeito')
        elif self.qnt_positivo == 3 or 4:
            print(f'Você é Cumplice')
        elif self.qnt_positivo == 5:
            print(f'Você é culpado')
        else:
            print("Você está preso KKKK")
        
if __name__ == '__main__':
    investigador = Crime()
    investigador.fazer_pergunta()
    investigador.julgamento()



