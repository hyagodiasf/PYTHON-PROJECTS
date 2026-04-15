while(True):
    try:
        num_tabela = int(input('Digite o número que queira ver a tabela: '))
        inter_value = 0
        
        while(inter_value <= 10):
            print(f'{num_tabela} x {inter_value} = {num_tabela * inter_value}')
            inter_value += 1
    
    except ValueError:
        print('Error: Você não digitou um número!!!')