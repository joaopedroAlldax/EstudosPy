"""Estudo sobre a função len, que consiste na contagem de caracteres existentes na string
    o len leva em consideração os espaços do teclado"""

usuario = input("qual é o seu nome? ")
qnt_caracteres = len(usuario)
print(qnt_caracteres)

dicionario = {'Nome' : 'João', 'idade' : '19', 'cargo' : 'dev'}
print(len(dicionario))

lista = ['oi', 'como ce ta', 'eu', 'quero saber a cor da sua calcinha']
print(len(lista))