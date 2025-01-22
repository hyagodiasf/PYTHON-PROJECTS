import os
lista = []
count = 0
while True:
    print('Selecione uma opção: ')
    opc = input('[i]nserir [a]pagar [l]istar: ').lower()
    if(len(opc) != 1):
        print("Você digitou mais de um caracter!")
        continue
    elif(opc == 'i'):
        os.system('cls')
        valor_insert = input('Digite o que deseja add na lista: ')
        lista.append(valor_insert)
    elif(opc == 'a'):
        esc_indice = input('Escolha o índice para apagar: ')
        if(len(esc_indice) != 1 or not esc_indice.isdigit()):
            print('Não foi possível apagar esse índice')
        elif(esc_indice.isdigit()):
            if(len(lista) == 0):
                print("Lista está vázia, não pode apagar...")
                continue
            else:
                lista.pop(int(esc_indice))     
    elif(opc == 'l'):
        os.system('cls')
        for indice, valor in enumerate(lista):
            print(indice, valor)
    count += 1
    