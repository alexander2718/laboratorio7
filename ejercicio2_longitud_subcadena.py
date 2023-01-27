def longitud_subcadena(s):
    conj_letras = set()
    long_max = 0
    long_actual = 0
    for letra in s:
        if letra in conj_letras:
            conj_letras.clear()
            long_actual = 0
        conj_letras.add(letra)
        long_actual += 1
        long_max = max(long_max, long_actual)
    return long_max

print(longitud_subcadena("alexander"))
