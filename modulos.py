# from salarios import operaciones
# from db import datos

# from salarios.operaciones import sumar_numeros
# from db.datos import mostrar_informacion

from salarios import generar_numeros
from salarios import sumar_numeros

# __name__ = "__test__"

# print(__name__)



if __name__ == "__main__":
    print(sumar_numeros(*generar_numeros()))

    

# if __name__ == "modulos":
#     print("Ejecutándose dentro del shell de Python")