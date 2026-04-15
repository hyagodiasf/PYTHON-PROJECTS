try:
    #### PAR OU IMPAR ####
    numero = int(input('Digite um número inteiro: '))
    
    par_ou_impar = "par" if (numero % 2 == 0) else "impar"

    print(par_ou_impar)

    #### INFORMAR HORA ####
    hora = int(input('Digite a hora: '))
    if(hora > 0 and hora < 12):
        print('Bom dia!')
    elif(hora >= 12 and hora < 18):
        print('Boa tarde!')
    elif(hora >= 18 and hora <= 23):
        print('Boa noite!')
    else:
        print('Hora não certa! ')

    #### INFORMAR NOME ####
    nome = input('Digite seu nome: ')
    if(len(nome) <= 4):
        print('Seu nome é curto!')
    elif(len(nome) > 4 and len(nome) <= 6):
        print('Seu nome é normal! ')
    else:
        print('Seu nome é muito grande!')
except TypeError:
    print('Error: Informe um número!!!')

