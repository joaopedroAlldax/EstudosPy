"""Faça um programa no qual o usuario digite um nome e o programa retorna se o nome é curto (4 letras),
se o nome for normal(5 e 6 letras), 6 ou mais letras (seu nome é muito grande)"""
class Nome:
    def __init__(self, nome):
        self.nome = nome
        self.letra = len(self.nome)
    
    def calcular_nome(self):
        if self.letra < 4:
            print("Seu nome é curto")
        elif self.letra < 5 or self.letra < 6:
            print("Seu nome é normal")
        elif self.letra >= 6:
            print("Seu nome é grande")
        else:
            pass

if __name__ == '__main__':
    nome = input("Qual é o seu nome?")
    nome1 = Nome(nome)
    nome1.calcular_nome()        