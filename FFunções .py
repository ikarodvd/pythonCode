from math import exp, expm1
def soma (x, y):
    return (x+y)

def substracao(x,y):
    return (x-y)

continuar = 1.0

def razao(x,y):
    return (x/y)

def potenciax (x):
    return (exp(x))

while (continuar):
    x = float (input ("Digite o primeir valor: "))
    y = float (input ("Digite o segundo valor: "))
    if (continuar):
        print ("A soma dos valores é:", soma(x,y))
        print ("A substração dos valores é:", substracao(x,y))
        e = potenciax(x)
        print ('A pontecia (math.exp(x) de {}  é = {}'.format(x,e))
        print ('Razão entre os números {} e {} é: {}'.format(x,y,razao(x,y)))

        continuar = (int(input('Digite 0 para sair, ou qualquer outro valor para sair: ')))


