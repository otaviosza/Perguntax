def tem_combinacao_soma(array, X):
    numeros_vistos = set()

    for numero in array:
        complemento = X - numero
        if complemento in numeros_vistos:
            return True
        numeros_vistos.add(numero)

    return False

array_exemplo = [1, 15, 2, 7, 2, 5, 7, 1, 4]
X = int(input("Digite o valor de X: "))

resultado = tem_combinacao_soma(array_exemplo, X)

if resultado:
    print(f"True - Existe uma combinação de dois números no array que soma {X}.")
else:
    print(f"False - Não existe uma combinação de dois números no array que soma {X}.")
