cadena=str(input("ingrese una cadena: "))
n=int(input("Ingrese un valor: "))
abecedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cadena_nueva = ""
for i in cadena:
    index = abecedario.index(str(i))
    cadena_nueva+= abecedario[index + n]
print(cadena_nueva)

