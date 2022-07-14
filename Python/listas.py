#definição de lista
my_list = [1, 2, 3]
print(my_list)

#Além de imprimir a lista, mostra os tipos de dados e o primeiro elemento
print (type(my_list[0]))

# Uma lista pode apresentar diveros tipos de variaveis
my_list2 = [1, 10, "Olá python", [1, 2, 3]]
print (my_list2)

#atribuindo metodos nativos na lista
print (my_list2 [2].upper())

#metodos basicos 
##acrescentar numero
l = [1, 2, 3]
l.append(10)
print(l)

##retirar e retornar o valor retirado
l.pop()
print(l)

##ordenar listas
new_list = ["b", "a", "d", "c"]
new_list.sort()
print(new_list)

#ordenar de tras pra frente
new_list.reverse()
print (new_list)

##listas alinhadas (lista dentro de lista)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [list1, list2, list3]
list5 = [my_list, my_list2, new_list]

