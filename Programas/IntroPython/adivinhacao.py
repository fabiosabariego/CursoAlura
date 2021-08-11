''' CRIANDO O PRIMEIRO JOGO DE ADIVINHAÇÃO '''
print('*********************************')
print('Bem vindo ao Jogo de Adivinhação')
print('*********************************')

numero_secreto = 42
tentativas = 3



while tentativas > 0:
    usuario = int(input('Digite o seu Numero: '))
    if usuario == numero_secreto:
        print(f'Você digitou {usuario}, o numero secreto é {numero_secreto}, você acertou, parabéns!!')
    elif usuario > numero_secreto:
        print(f'Você digitou {usuario}, o numero secreto é {numero_secreto}, o numero digitado é Maior que o numero Secreto!')
    elif usuario < numero_secreto:
        print(f'Você digitou {usuario}, o numero secreto é {numero_secreto}, o numero digitado é Menor que o numero Secreto!')
    tentativas -= 1

print('Fim do Jogo!!')
