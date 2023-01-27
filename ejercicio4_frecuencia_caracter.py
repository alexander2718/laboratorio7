def frecuencia_caracter(string):
    frecuencia = {}
    for char in string:
        if char in frecuencia:
            frecuencia[char] += 1
        else:
            frecuencia[char] = 1
    return frecuencia

print(frecuencia_caracter("realizando los ejercicios"))
