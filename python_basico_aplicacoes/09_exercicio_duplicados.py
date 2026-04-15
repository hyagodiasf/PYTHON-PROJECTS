lista_de_listas = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,1,8,9,9,4,2,2,6,5]
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_de_listas:
    print(lista, 
          encontra_primeiro_duplicado(lista)
          )