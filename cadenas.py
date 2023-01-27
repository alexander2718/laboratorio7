s = "Esto es una cadena"
print(s)
print(type(s))


#Declarar con comillas simples

s = 'Es también es una cadena'
print(s)
print(type(s))

#declarar una cadena:
s = ''

#Errores
s = "Esto es una comilla\""
print(s)

#Saltos de línea en una cadena
s = "Linea uno \nLinea dos"
print(s)

#Uso de caracteres asociados:
print("\110\65")
print("""
asafaf
asafaf
gfgfg
dfdfd""")

#formato de cadenas
#concatenar cadenas

x = 10
s = "Este numero es: %i" %x
print(s)

# si tengo más de una variable
s = "Los números son los siguientes %i y %i" %(4,5)
print(s)

#haciendo uso del método .format()
s = "Los números son los siguientes {a} y {b}" .format(a=4,b=5)
print(s)
a=4
b=5
s = f"Los números son los siguientes {a} y {b}"
print(s)

# más usos del f-string
a=4
b=5
s = f"a + b = {a+b}"
print(s)

def fun():
    return 20
s = f"El resultado de la función es {fun()}"
print(s)

s = "python"
s2= "3.10"
print(s+ " "+ s2)

#Uso del operador in
print("3.20" in "Python tiene ña versión 3.20")

#uso de las funciones chr() y ord()
print(chr(65))
print(chr(47))

print(ord("A"))
print(ord("a"))

print(len("Curso de estructura de datos"))

#convertir a otros tipos de datos:

x = str(3.1416)
print(x)
print(type(x))

#indexar cadenas
x = "abcdefg"
print(x[0])
print(x[-4])

print()
x = "abcdefg"
print(x[0:5:2])

#El método capitalize()
s = "python versión 3.20"
print(s.capitalize())

#El método lower()
s = "PYTHON"
print(s.lower())

#El método swapcase()
s = "EdEm DaToS"
print(s.swapcase())

#El método upper()
s = "python"
print(s.upper())

#El método count()
s = "el mejor lenguaje"
print(s.count("j"))

#El método isalnum()
s = "edem@unsch.edu.pe"
print(s.isalnum())

#El método isalpha()
s = "abcdefghi"
print(s.isalpha())

#El método strip()
s = "     hola      "
print(s.strip())

#El método zfill()
s = "123"
print(s.zfill(5))

# El método join()

s = "y" .join(["1", "2", "3"]) 
print(s)

#- El método split()
s = "Python, Ruby, Java"
print(s.split(","))

#ejercicio 01 - palindromo

def palindromo (string):
    return string == string [::-1]

print(palindromo("ana"))
print(palindromo("hola"))