import os
import time

print('\n' \
'LISTA DE COMPRAS' \
'' \
'\n\n')

lista_produtos = []

while True:

    print('Selecione uma opção abaixo.\n')
    opc = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opc not in ('i', 'a', 'l', 's'):

        print('ATENÇÃO! Digite apenas [i] - [a] - [l] - [s]: ')
        continue
    
    if opc == 's':
      
      print("Saindo do programa...")
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    
    elif opc == 'i':

        try:
            quantidade_itens = int(input('Quantos itens você deseja inserir? '))
        except ValueError:
            print('Digite apenas números.\n')
            continue

        for _ in range(quantidade_itens):
            produto = input('Digite o produto: ')
            lista_produtos.append(produto)

    elif opc == 'a':

        if not lista_produtos:
            print('Lista vazia.\n')
            continue
         
        apagar_por_indece = input('Deseja apagar pelo index? [s]im [n]ão: ').lower()

        if apagar_por_indece == 's':

            try:
                indice = int(input('Digite o index: '))
                removido = lista_produtos.pop(indice)
                print(f'"{removido}" removido com sucesso.')
            except (IndexError or ValueError):
                print('Índice inválido')
        else:
            lista_produtos.clear()

    elif opc == 'l':
        if not lista_produtos:
            print('ATENÇÃO: Lista vazia...')

        print('####LISTA DE PRODUTOS####')

        for inx, valor in enumerate(lista_produtos):
            print(f'{inx} - {valor}')
            
    print()