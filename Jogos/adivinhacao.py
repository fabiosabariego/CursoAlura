''' CRIANDO O PRIMEIRO JOGO DE ADIVINHAÇÃO '''
print('*********************************')
print('Bem vindo ao Jogo de Adivinhação')
print('*********************************')

numero_secreto = 42

usuario = int(input('Digite o seu Numero: '))

if usuario == numero_secreto:
    print(f'Você digitou {usuario}, o numero secreto é {numero_secreto}, você acertou, parabéns!!')
else:
    print(f'Você digitou {usuario}, o numero secreto é {numero_secreto}, você errou!!')

print('Fim do Jogo!!')
