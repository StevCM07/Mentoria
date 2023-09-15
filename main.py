if __name__ == "__main__":

    #* Quiero crear una lista con los números pares del 1 al 20.
    # lista = []

    # for numero in range(1, 21):
    #     #* Condición para verificar que el número es par.
    #     if numero % 2 == 0:
    #         lista.append(numero)

    # for numero in range(2, 21, 2):
    #     lista.append(numero)
        
    lista = [numero for numero in range(1, 21) if numero % 2 == 0]
    
    # * Generar una lista de las vocales dentro de un mensaje.
    message = "Hola, como estas"

    vocales = [letra for letra in message if letra in ["a", "e", "i", "o", "u"]]

    print(vocales)

    #* Generar un diccionario que me muestre una serie de cantidades relacionadas al doble de cada una de ellas
    """
    {
        "cantidad1": cantidad1 * 2
        "cantidad2": cantidad2 * 2
        "cantidad3": cantidad3 * 2
    }
    {
        "1": 2,
        "2": 4,
        "3": 6,
    }
    """
    cantidades = {str(numero): (numero * 2) for numero in range(1, 25) if numero % 2 != 0}
    print(cantidades)
    