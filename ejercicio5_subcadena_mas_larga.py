def longitud_mas_larga(cadena):
    long_max = 0
    long_actual = 0
    for char in cadena:
        if char.isdigit():
            long_actual +=1
        else:
            long_max = max(long_max, long_actual)
            long_actual = 0
    long_max = max(long_max, long_actual)
    return long_max
print(longitud_mas_larga("prueba123456789ejercicio456"))