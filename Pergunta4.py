def completa_intervalo(array):
    if not array:
        return array

    max_numero = max(array)
    numeros_presentes = set(array)

    for i in range(max_numero):
        if i not in numeros_presentes:
            array.append(i)

    array.sort()

array_padrao = [9, 2, 3, 1, 4]

print("Array antes de completar o intervalo:", array_padrao)

completa_intervalo(array_padrao)

print("Array após completar o intervalo:", array_padrao)
