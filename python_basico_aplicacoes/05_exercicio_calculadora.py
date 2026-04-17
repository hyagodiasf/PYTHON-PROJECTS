while True:
    opc = input('Para iniciar tecle [i], para sair tecle [s]: ').lower()

    if opc not in ('i', 's'):
        print('ATENÇÃO! Digite apenas [i] ou [s].')
        continue

    if opc == 's':
        print("Saindo do programa...")
        break

    # opção 'i'
    try:
        num_tabela = int(input('Digite o número da tabela: '))
    except ValueError:
        print('Error! Você deve digitar um número válido!')
        continue

    for i in range(11):
        print(f'{num_tabela} x {i} = {num_tabela * i}')