import os, time as temp

print('\n' \
'LISTA DE COMPRAS' \
'' \
'\n\n')

lista_produtos = []

while True:
    print('Selecione uma opção abaixo.\n')
    itens_opc = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if(len(itens_opc) != 1 or itens_opc.isdigit()):
        print('Você digitou mais de um caracter ou um número. \nEscolha [i] - [a] - [l] - [s]')
        continue
    
    if(itens_opc == 's'):
       print('Até a próxima...')
       temp.sleep(3)
       os.system('cls')
       break
    elif(itens_opc == 'i'):
        lista_tamanho = int(input('Quantos itens você deseja inserir? '))
        itens_lista = 0
        while itens_lista < lista_tamanho:
            items_produtos = input('Digite os itens que deseja: ')
            lista_produtos.append(items_produtos)
            itens_lista +=1
    elif(itens_opc == 'a'):
        apagar_por_index = input('Deseja apagar pelo index? [s]im [n]ão: ').lower()
        if(apagar_por_index == 's'):
            try:
                apagar_por_index_choece = int(input('Digite o index: '))
                lista_produtos.pop(apagar_por_index_choece)
            except:
                print(f'Você escolheu um indece ({apagar_por_index_choece}) maior que o tamanho da lista ({len(lista_produtos)})')
        else:
            lista_produtos.clear()
    elif(itens_opc == 'l'):
        if(lista_produtos == 0):
            print('ATENÇÃO: Lista vazia...')
        print('####LISTA DE PRODUTOS####')
        for inx, valor in enumerate(lista_produtos):
            print(f'{inx} {valor}')
    print()