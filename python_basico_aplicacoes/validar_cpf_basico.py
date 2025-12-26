import os, time as tmp

def formatar_cpf_lista(lista):
    # Junta os números da lista em uma string
    cpf = ''.join(map(str, lista))
    # Aplica a formatação
    # EX:  [7, 4, 6, 8, 2, 4, 8, 9, 0, 7, 0] --> 746.824.890-70
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Obtém o número de CPF, depois retira os 3 últimos valores
# usando a técanica de slice

print()
print("-------------------------------------------")
print()
########## PRIMEIRO DÍGITO #############

dado_cpf = input('Informe o CPF. EX: 746.824.890-70 \n')
lista_dados = dado_cpf.replace('.','')[:-3]

aux_lista = []
numeros = []

for cpf_numeros in lista_dados:
    numeros.append(int(cpf_numeros))
    valor_regressivo_1 = list(range(10, 10 - len(lista_dados), -1))
    valor_produto_1 = [num * v_reg for num, v_reg in zip(numeros, valor_regressivo_1)]
print("",valor_regressivo_1, "\n", numeros, "\n", valor_produto_1)

soma_valors_produto_1 = 0

for soma in valor_produto_1:
    soma_valors_produto_1 += soma
mult_resul_somaValor_1 = (soma_valors_produto_1 * 10)
resto_divisao_1 = (mult_resul_somaValor_1 % 11)

print(f"Resultado da soma: {soma_valors_produto_1}")
print(f"Multiplicação de {soma_valors_produto_1} * 10 = {mult_resul_somaValor_1}")
print(f"Resto da divisão de {mult_resul_somaValor_1} % 11 = {resto_divisao_1}")

if(resto_divisao_1 > 9):
    print('Dígito: ', 0)
elif(resto_divisao_1 >= 2):
    numeros.append(resto_divisao_1)

print()
print("-------------------------------------------")
print()
########## SEGUNDO DÍGITO #############


valor_regressivo_2 = list(range(11, 10 - len(lista_dados), -1))
valor_produto_2 = [numero * reg for numero, reg in zip(numeros, valor_regressivo_2)]
print("",numeros,"\n",valor_regressivo_2,"\n",valor_produto_2)

soma_valors_produto_2 = 0
for sum in valor_produto_2:
    soma_valors_produto_2 += sum
mult_resul_somaValor_2 = (soma_valors_produto_2 * 10)
resto_divisao_2 = (soma_valors_produto_2 % 11)
print(f"Resultado da soma: {soma_valors_produto_2}")
print(f"Multiplicação de {soma_valors_produto_2} * 10 = {mult_resul_somaValor_2}")
print(f"Resto da divisão de {mult_resul_somaValor_2} % 11 = {resto_divisao_2}")

if(resto_divisao_2 > 9):
    print("Dígito: ", 0)
elif(resto_divisao_2 <= 9):
    numeros.append(resto_divisao_2)

cpf_formatado = formatar_cpf_lista(numeros)
if(cpf_formatado == dado_cpf):
    print("CPF válido: ",cpf_formatado)
else:
    print("CPF inválido!")