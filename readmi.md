## Descripción del ejercicio 
Este proyecto resuelve el problema de "Reino de los Números Infiltrados"
El objetivo es encontrar cuantos números primos hay dentro de un rango (L, R), para provar el funcionamiento se toma en cuenta lo siguiente: 
- Se considera que el número 1 no es primo
- Los rangos son: 1 ≤ L ≤ R ≤ 10^6.
- La entrada termina cuando ambos números recibidos son '0 0'

## Lenguaje
El lenguaje usado en este ejercicio es Python 3.11.0

## Solución 
1. Se genera una lista de booleanos `es_primo` donde  `es_primo[i] = True` si `i` es primo. 
2. Para todas las consultas `[L, R]` recorre el rango y se cuentan los números primos usando esta lista precalculada.
3. Se incluye una validacion para ignorar líneas vacías y controlar que los números que sean ingresados no pasen el límite máximo permitido (10^6).
