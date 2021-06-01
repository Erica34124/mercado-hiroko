from django.shortcuts import render , HttpResponse

# Create your views here.
import requests

# Create your tests here.
while True:
    print("_"*50)
    print("Qual cotação deseja efetuar:\n \n [1] -> Bitcoin \n [2] -> Ethereum \n [3] -> para Litecoin")
    print("_"*50)
    cot =int(input('Digite item de pesquisa: '))
    print("="*50)
    if cot >= 1 and cot <= 3:
        break
    else:
        print('pesquisa inválida')

def cotacao():

    if cot == 1:
        return 'BTC'
    
    elif cot == 2:
        return 'ETH'
        
    elif cot == 3:
        return  'LTC'
    
    
            
        
response = requests.get('https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD,ETH,LTC'.format(cotacao()))
bit = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')
eth= requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,ETH,LTC')
lit = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,ETH,LTC')
#print(response.status_code);

dados = response.json()

if cot == 1:
    print('A conversão de Bitcoin para Dolar é U${} '.format(dados['USD']));

elif cot == 2:
    print('A conversão de Ethereum para Dolar é U${} '.format(dados['USD']));

elif cot == 3:
    print('A conversão de Litecoin para Dolar é U${} '.format(dados['USD']));
b = bit.json()
e =eth.json()
l = lit.json()
print("="*50)
print('valor just-time do Bitcoin: {}'.format(b['USD']));
print("_"*50)
print('valor just-time do Ethereum: {}'.format(e['USD']));
print("_"*50)
print('valor just-time do Litcoin: {}'.format(l['USD']));
print("_"*50)
