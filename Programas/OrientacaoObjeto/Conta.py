''' PRIMEIRAS AULAS SOBRE ORIENTAÇÃO A OBJETO '''
def cria_conta(numero, titular, saldo, limite):
    conta = {'Numero': numero, 'Titular': titular, 'Saldo': saldo, 'Limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'Saldo é de R${conta["saldo"]}')

