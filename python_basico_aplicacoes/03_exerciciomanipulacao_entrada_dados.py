
while(True):
    try:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))

        if(nome == ''):
            print('Nome não pode ser vázio!!!')
        else:
            print(f'Seu nome é: {nome}')
            print(f'Seu nome invertido é: {nome[::-1]}')
            print(f'Seu nome contém (ou não) espaços: {nome.count(' ')}')
            print(f'Seu nome tem: {len(nome)}')
            print(f'A primeira letra do seu nome é: {nome[0]}')
            print(f'A última letra do seu nome é: {nome[-1]}')
    except ValueError:
        print('Erro: Idade deve ser um número!!! ')
