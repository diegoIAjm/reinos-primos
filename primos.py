# Reino de los Números Infiltrados
# Contar primos en un rango L-R para varios casos

def criba(maximo):
    """Genera una lista donde True indica que el número es primo."""
    primos = [True] * (maximo + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(maximo ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, maximo + 1, i):
                primos[j] = False
    return primos

def main():
    limite = 10**6
    es_primo = criba(limite)

    while True:
        linea = input().strip()
        if linea == "0 0":
            break
        L, R = map(int, linea.split())
        contador = 0
        for numero in range(L, R + 1):
            if es_primo[numero]:
                contador += 1
        print(contador)

if __name__ == "__main__":
    main()
