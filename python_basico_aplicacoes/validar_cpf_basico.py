def formatar_cpf_lista(lista):
    # Junta os números da lista em uma string
    cpf = ''.join(map(str, lista))
    # Aplica a formatação
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# TRANSFORMAR LISTA DE NÚMEROS EM STRING 
# EX.: [7, 4, 6, 8, 2, 4, 8, 9, 0, 7, 0] => 74682489070
# def lista_para_cpf(lista):
#     # Junta os números da lista em uma string
#     return ''.join(map(str, lista))

########## PRIMEIRO DÍGITO ##########

aux_lista = []
numeros = []

dado_cpf = input('Digite seu CPF. ex: 746.824.890-70 = ')
lista_dados = dado_cpf.replace('.','')[:-3]

for cpf_numeros in lista_dados:
    numeros.append(int(cpf_numeros))
    regressiva_1 = list(range(10, 10 - len(lista_dados), -1))
    produto_1 = [numero * reg for numero, reg in zip(numeros, regressiva_1)]
print("",numeros,"\n",regressiva_1,"\n",produto_1)

soma_1 = 0
for sum in produto_1:
    soma_1 += sum
resto_divisao_1 = ((soma_1*10)%11)
multiplicacao_cpf_1 = soma_1*10
print(f"Resultado da soma: {soma_1}")
print(f"Multiplicação de {soma_1} * 10 = {multiplicacao_cpf_1}")
print(f"Resto da divisão de {multiplicacao_cpf_1} % 11 = {resto_divisao_1}")

if(resto_divisao_1 > 9):
    print("Dígito: ", 0)
elif(resto_divisao_1 >= 2):
    numeros.append(resto_divisao_1)
    
print()
print("-------------------------------------------")
print()
########## SEGUNDO DÍGITO #############

regressiva_2 = list(range(11, 10 - len(lista_dados), -1))
produto_2 = [numero * reg for numero, reg in zip(numeros, regressiva_2)]
print("",numeros,"\n",regressiva_2,"\n",produto_2)

soma_2 = 0
for sum in produto_2:
    soma_2 += sum
resto_divisao_2 = ((soma_2*10)%11)
multiplicacao_cpf_2 = soma_2*10
print(f"Resultado da soma: {soma_2}")
print(f"Multiplicação de {soma_2} * 10 = {multiplicacao_cpf_2}")
print(f"Resto da divisão de {multiplicacao_cpf_2} % 11 = {resto_divisao_2}")

if(resto_divisao_2 > 9):
    print("Dígito: ", 0)
elif(resto_divisao_2 <= 9):
    numeros.append(resto_divisao_2)

cpf_formatado = formatar_cpf_lista(numeros)
if(cpf_formatado == dado_cpf):
    print("CPF válido: ",cpf_formatado)
else:
    print("CPF inválido!")