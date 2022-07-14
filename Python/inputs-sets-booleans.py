#INPUT
##faz com que o usuario digite valores
a = input()
print(int(a))

##SET
##igual conj da matematica, ou seja não se repete
x = set()
x.add(1)
x.add(2)
x.add(20)
x.add(45)
print(x)

##ultilizando o metodo set na lista
lista = [1, 2, 3, 3, 3, 4, 5, 5, 5]
lista = set(lista)
print(lista)

##metodos basicos do set
new= x.union(lista)
new1 = x.intersection(lista)

print(new)
print(new1)
