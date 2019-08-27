# Script da Chuva
print('Está chovendo?')
verificaChuva = input()

if verificaChuva.capitalize() == 'Sim':
    print('Você tem Guarda-chuva?')
    checkGuardaChuva = input()

    if checkGuardaChuva.capitalize() == 'Não':
        while verificaChuva.capitalize() == 'Sim':
                print('Espere um pouco')
                print('Está chovendo?')
                verificaChuva = input()
                
print('Saia')
