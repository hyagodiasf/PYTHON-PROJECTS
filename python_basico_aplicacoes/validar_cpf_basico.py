aux_lista = []
numeros = []

dado_cpf = input('Digite seu CPF. ex: 746.824.890-70 = ')
lista_dados = dado_cpf.replace('.','')[:-3]

for cpf_numeros in lista_dados:
    numeros.append(int(cpf_numeros))
    regressiva = list(range(10, 10 - len(lista_dados), -1))
    produto = [numero * reg for numero, reg in zip(numeros, regressiva)]
print("",numeros,"\n",regressiva,"\n",produto)

soma = 0
for sum in produto:
    soma += sum
print(f"Resultado da soma: {soma}")
print(f"Multiplicação de {soma} * 10 = {soma*10}")
print(f"Resto da divisão de {soma*10} % 11 = {(soma*10)%11}")
if(((soma*10)%11) <=9):
    print(f"Resultado é {(soma*10)%11}")
else:
    print("Resultado",0)