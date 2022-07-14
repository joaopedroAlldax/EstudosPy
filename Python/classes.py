
class User:
    # definindo metodo contrutor e outros metodos
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

        # instanciando objeto

    def mostrar_dados(self):
        print(f'Meu nome é: {self.nome}, Minha idade é: {self.idade}, Minha altura é: {self.altura}m.')

    def mostrar_peso(self):
        print(f'meu peso é de: {self.peso}')

    def calculo_imc(self):
        if ',' in self.altura:
            self.altura = self.altura.replace(',', ".")
            imc =float(self.peso)/float(self.altura)**2
            print(f'Seu imc é: {imc}')
        else:
            imc =float(self.peso)/float(self.altura)**2
            print(f'Seu imc é: {imc}')


if __name__ == "__main__":
    nome = input("Digite o nome: ")
    idade = input("Digite o idade: ")
    altura = input("Digite o altura: ")
    peso = input("Digite seu peso: ")
    user = User(nome, idade, altura, peso)
    
    user.calculo_imc()







