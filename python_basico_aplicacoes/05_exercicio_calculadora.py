import os
while(True):
        opc = input('Para inicar tecle [i], Para sair tecle [s]').lower()
        if(not opc.isalpha() or len(opc) !=1):
            print('Você digitou um número ou mais de uma letra ou um caracter especial!!!')
            print('ATENÇÃO!!! Digite apenas [i] para iniciar ou [s] para sair.')
        elif(opc == 'i'):
            num_tabela = int(input('Digite o número que queira ver a tabela: '))
            inter_value = 0
            
            while(inter_value <= 10):
                print(f'{num_tabela} x {inter_value} = {num_tabela * inter_value}')
                inter_value += 1
        elif(opc == 's'):
            print("Saindo do programa...")
            break