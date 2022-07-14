#definição de dicionario
## O titulo (nome, idade e profissao) é chamado de chaves (keys) e o conteudo é chamado de value
my_dic = {"nome" : "jp", "idade" : "22", "profissao" : "dev", "filhos" : ["maria", "jose"]}
print(my_dic)

##acessar uma chave
print(my_dic["nome"])

##adicionar mais informação 
my_dic ["cidade"] = "São Paulo"
print(my_dic)

##adicionar um dicionario dentro de outro
my_dic ["variavel"] = {"a" : "true", "b" : "false"}
print(my_dic)


new_dic = {"v1" : "20", "v2" : "10", "v3" : "50", "v4" : "30"}
##metodos basicos do dicionario
print(new_dic.keys())

print(new_dic.values())

