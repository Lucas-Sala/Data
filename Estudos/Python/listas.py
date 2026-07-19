#Declaração de Lista
names = ["Lucas", "João", "Maria", "Roberta"] 

#Impressão do primeiro item da lista
print(names[0])

#Adição de um termo a lista
names.append("Carlos")

#Remoção de um termo da lista
names.remove("João")

#Impressão da lista
print(names)

#Reversão
names.reverse()

print(names[0])

names.append("Camila")

print(names)

#Impressão do tamanho da lista
print(len(names))

#Remoção do último item da lista
names.pop()

print(len(names))

name = ["Alan"]

#Concatenação de listas
names = names.__add__(name)

print(names)

#Ordenamento de Listas
names.sort()

print(names)

#Impressão da Posição de um item na lista
print(names.index("Lucas"))

print(type(names))