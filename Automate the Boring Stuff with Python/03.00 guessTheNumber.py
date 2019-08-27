# Este é um jogo de adivinhar o número.
import random
aleatorio = random.randint(1, 20)

print('Estou pensando em um número entre 1 e 20.')
  
tentativa = 0
advinha = 0
tentativasRestantes = 6

while advinha != aleatorio:
    if tentativasRestantes == 0:
        print('Você não conseguiu. O numero era', aleatorio)
        break
    
    print('Você tem', tentativasRestantes, 'tentativas. Adivinhe:')
    advinha = int(input())
    tentativa = tentativa + 1
    tentativasRestantes = tentativasRestantes - 1

    if advinha < aleatorio:
        print('Sua tentativa está abaixo')
    elif advinha > aleatorio:
        print('Sua tentativa está acima')
    else:
        print('Bom trabalho! Você adivinhou meu número em', tentativa, 'tentativas!')
