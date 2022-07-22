#criando a classe
class Notas:
    #metodo construtor
    def __init__(self, nota1, nota2, nota3 , nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        print(type(self.nota1))
        

    def calculo_media(self):
        self.media = (float(self.nota1 + self.nota2 + self.nota3 + self.nota4)/4)
        print(self.media)
        
    
if __name__ == "__main__":
    
    nota1 = input("Digite a primeira nota do aluno: ")
    nota2 = input("Digite a segunda nota do aluno: ")
    nota3 = input("Digite a terceira nota do aluno: ")
    nota4 = input("Digite a quarta nota do aluno: ")
    notas = Notas(nota1, nota2, nota3, nota4)
    notas.calculo_media()

        
