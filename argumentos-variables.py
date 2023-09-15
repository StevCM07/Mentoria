# def mi_funcion(argumento1, argumento2, argumento3):
#     print(argumento1)
#     print(argumento2)
#     print(argumento3)

# mi_funcion(1, argumento3=3, argumento2=2)
# mi_funcion(1, argumento3=3, argumento2=2)
# mi_funcion(argumento3=3, argumento2=1, argumento1=2)

# def mostrar_datos(numero, status, mensaje):
#     print(numero, status, mensaje)


# if __name__ == "__main__":
#     mis_argumentos = [1, False, "Hola"]
#     # mostrar_datos(mis_argumentos[0], mis_argumentos[1], mis_argumentos[2])
#     mostrar_datos(*mis_argumentos)


def sumar_numeros(*args):
    return sum(args)

if __name__ == "__main__":
    print(sumar_numeros())
    print(sumar_numeros(1, 2, 3))
    print(sumar_numeros(1, 2, 3, 4, 5, 6))
    print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9))
    print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    
    #* Obtener la suma de los numeros del 1 al 100.

    print(sumar_numeros(*list(range(1, 101))))

datos_usuario = {
    "nombre":"Fabián",
    "edad": 22,
    "salario": 23.45
}

def mostrar_datos_usuario(nombre, edad, salario):
    print(nombre, edad, salario)

def mostrar_argumentos_llave_valor_variables(**kwargs):
    print(kwargs)

    for campo, valor in kwargs.items():
        print(campo, valor)

def combinando_argumentos_longitud_variable(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    mostrar_datos_usuario(**datos_usuario)

    mostrar_argumentos_llave_valor_variables(dato1=2, edad=34, país="Perú", matriz=[1, 2, 3])

    combinando_argumentos_longitud_variable(1, 2, 3, edad=1, precio=23.45)

