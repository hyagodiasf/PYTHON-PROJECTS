dado_cpf = input('Informe o CPF. EX: 746.824.890-70 \n')
lista_dados = dado_cpf.replace('.','').replace('-','')[:-3]

valor_regressivo_2 = list(range(11, 9 - len(lista_dados), -1))
print(valor_regressivo_2)