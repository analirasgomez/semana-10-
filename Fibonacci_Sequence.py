
# 0,1,1,2,3,5,8,13
# an = an-1 + an-2 si n ≥ 3 y a1 = a2 = 1

def fibonacci (n):
    if n <= 1: 
        return n 
    else: 
        return fibonacci (n-1) + fibonacci (n-2)

numero = int (input("Posición que quieres de la frecuencia de Fibonacci:"))
print (fibonacci(numero))

# Obtener la secuencia de Fibonacci hasta el numro dado.
result = [fibonacci(i) for i in range(numero+1)]
print(result)
