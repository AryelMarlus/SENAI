def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def calcular_fatorial_recursiva(numero):
    if numero == 1:
        return 1
    return numero * calcular_fatorial_recursiva(numero -1)

print(calcular_fatorial(5))
print(calcular_fatorial_recursiva(5))