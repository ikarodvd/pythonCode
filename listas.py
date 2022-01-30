
lista = []

def listas ():
    for i in range (0,10):
        lista.append(int(input('Digite o valor {}: '.format(i))))

    print (lista)

def soma(lista):
    soma = 0
    for i in  lista:
        soma = i + soma
    print (soma)    

def somasum(lista):
    lista1 = [int (string)for string in lista]
    lista2 = sum(lista1)
    print (lista2)
listas()
soma(lista)
somasum(lista)