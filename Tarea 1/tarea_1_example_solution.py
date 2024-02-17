# La función recibe como parámetro a "string", luego se verifica que el
# parámetro se un string, sea alfabético y que no sea un espacio vacío.
# Luego se revisa el estado de cada caractér (mayúscula/minúsucla) y se va
# agreagando el mismo caractér con el estado inverso en "finalstring".

def invert_case(string):
    finalstring = ""
    if isinstance(string, str):
        if string.isalpha() or string == "":
            if string != "":
                if not (string.isspace()):
                    for i in string:
                        if i.isupper():
                            finalstring = finalstring + i.lower()
                        else:
                            finalstring = finalstring + i.upper()
                    return 0, finalstring
            else:
                return -48, None
        else:
            return -32, None
    else:
        return -16, None


# La función verifiva que se recibe como parámetro un numero entero menor que
# 100, luego se crea una lista con los todos los números antes del número base
# y luego secrea otra lista que contiene los múltiplos de los números hasta el
# número quemultiplicado por si mismo sea mayor al base, luego los números de
# una lista seeliminan en la otra resultando en una lista con únicamente
# números primos.

def numero_primo(base):
    primos = []
    no_primos = []
    if not isinstance(base, int):
        return -64, None
    if isinstance(base, bool):
        return -64, None
    if base > 100:
        return -80, None
    for i in range(base, 1, -1):
        primos.append(i)
    primos.reverse()
    for n in primos:
        if n * n <= base:
            for i in range(1, base + 1):
                if i % n == 0 and i != n:
                    no_primos.append(i)
    for i in no_primos:
        if i in primos:
            primos.remove(i)
    return 0, primos
