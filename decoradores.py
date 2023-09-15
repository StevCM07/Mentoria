
def funcion_validar(mi_funcion):
    def wrapper(numero1, numero2, numero3):
        if numero1 < 0 or numero2 < 0 or numero3 < 0:
            raise Exception("Hay un número negativo")
        return mi_funcion(numero1, numero2, numero3)
    return wrapper

@funcion_validar
def sumar_numeros(numero1, numero2, numero3):
    return numero1 + numero2 + numero3

@funcion_validar
def restar_numeros(numero1, numero2, numero3):
    return numero1 - numero2 - numero3

@funcion_validar
def multiplicar_numeros(numero1, numero2, numero3):
    return numero1 * numero2 * numero3



if __name__ == "__main__":
    # print(sumar_numeros(1, 2, -3)) # 6
    # print(restar_numeros(1, 2, -3)) # -4
    print(multiplicar_numeros(1, 2, -3)) # 6

    # resultado = funcion_validar(sumar_numeros)
    # print(resultado(1, 2, 3))
    
    # resultado = funcion_validar(restar_numeros)
    # print(resultado(1, 2, 3))
    
    # resultado = funcion_validar(multiplicar_numeros)
    # print(resultado(1, 2, 3))

    