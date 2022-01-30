numero = int (input ("Informe o numero da tabuada: "))

for c in range (0,11):
    print ('{} x {} = {}'.format(numero,c,c*numero))