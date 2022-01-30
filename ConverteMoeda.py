from multiprocessing.dummy import active_children
from operator import truediv
import requests
import json
import pickle

def tela_usuario():
    usuarios = []
    usee = open('usuarios.pckl','wb')
    pickle.dump(usuarios,usee)
    usee.close()

    print ('usuariosssss{}'.format(usuarios))
    action_user = int (input ("1- Acessar com usuario\n2- Cadastrar usuário\n3- Entrar como convidade"))
    if (action_user==1):
        nome_usuario = input("Informe o nome de usuário")
        if nome_usuario in usuarios:
            print("Usuario encontrado")
        else:
            print ('Usuario inexistente')
    elif (action_user==2):
            usuarios=(input('Digite o nome do usuario: '))
            print ('Usuário cadastrado!')    
            arqtxt = open('usuarios.pckl','wb')
            arqtxt.write(usuarios)
            arqtxt.close()

tela_usuario()

def menu_inicial ():
    print ("Informe a opção desejada\n")
    print ("\t1 - Dolar")
    print ("\t2 - Euro")
    print ("\t3 - Bitcoin")
    print ("\t4 - Etherium\n\n")


def define_moeda(moeda,mod):
    request_moeda= requests.get('https://economia.awesomeapi.com.br/all/'+moeda+'-BRL')
    cot = request_moeda.json()
    cot
    print ('\n')
    print ('Moeda: ' + cot[moeda]['name'])
    print ('Data: '+cot[moeda]['create_date'])
    print ('Valor atual: R$' + cot[moeda]['bid']+'\n' )
    valor_d = float (cot[moeda]['bid'])
    while (True): #tratamento de erro 
        try:          
            conv = float (input ("Informe o valor em reais a ser convertido: "))
            break
        except ValueError:
            print ('Digite uma opção vália!')
    print ('O valor de R$ {} em'.format(conv), mod, 'é: {:.2f} '.format(conv/valor_d))


def moeda_dolar ():
    define_moeda('USD', 'Dólar')

def moeda_euro():  
    define_moeda('EUR', 'Euro')

def moeda_btc ():
    define_moeda('BTC','Bitcoin')
def moeda_etherium():
    define_moeda('ETH', 'Etherium')


def switch_esc():
    while (True): #tratamento de erro 
        try:
            moeda_swither = int (input("Informe a moeda: "))
            break
        except ValueError:
            print ('Informe um dos números para as moedas!')
    
    if moeda_swither == 1:
        moeda_selec = "Dolar"
        moeda_dolar()
    elif moeda_swither == 2:
        moeda_selec = "Euro"
        moeda_euro()
    elif moeda_swither == 3: 
        moeda_selec = "Bitcoin"
        moeda_btc()
    elif moeda_swither == 4:
        moeda_selec = "Etherium"
        moeda_etherium()
    else: 
        print ("Moeda inválida!")
        print ('Informe um dos números para as moedas!')

continuar = 1
while (continuar!=0):
    menu_inicial()
    switch_esc()
    while (True): #tratamento de erro 
        try:
            continuar = int (input ("Continuar? 0 Sair - Qualquer numero para continuar\n "))
            break
        except ValueError:
            print ('Digite uma opção válida!')
  
if (continuar==0):
    print ('Programa finalizado')