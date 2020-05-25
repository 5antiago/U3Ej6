from Elemento import Elementos
from menu import Menu
from ObjectEncoder import ObjectEncoder
if __name__ == "__main__":
    obj = ObjectEncoder()
    elementos = obj.Decoder(obj.Leer("vehiculos.json"))
    del obj

    menu = Menu()
    print(" 1. Insertar vehiculo \n 2. Agregar \n 3. Mostrar \n 4. Modificar Base \n 5. Vehiculo mas economico")
    print(" 6. Todos los vehiculos\n 7. Guardar \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op,elementos)
        print(" 1. Insertar vehiculo \n 2. Agregar \n 3. Mostrar \n 4. Modificar Base \n 5. Vehiculo mas economico")
        print(" 6. Todos los vehiculos\n 7. Guardar \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))