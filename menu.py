from IElemento import Ielemetos
from Elemento import Elementos
from Autonuevo import AutoNuevo
from AutoUsado import AutoUsado
from Auto import auto
from ObjectEncoder import ObjectEncoder
class Menu(object):
    __switcher = dict
    def __init__(self):
        self.__switcher = { 1: self.Insert, 2: self.Agregar, 3: self.Mostrarpos, 4:self.Modifbase,
                            5:self.vehiculoeconomico, 6:self.mostrar, 7:self.guardar}
    def opcion(self, op, elementos):
        self.__switcher.get(op, lambda a: print("Opcion Incorrecta"))(Ielemetos(elementos))

    def Insert(self, elementos):
        print("Insertar Vehiculo")
        if input("Ingrese N para vehiculo Nuevo, U para Usado: ").lower() == "n":
            auto = AutoNuevo(input("Ingrese Modelo: "), float(input("Ingrese Precio Base: ") ),
                            input("Ingrese Color: "), int(input("Ingrerse cant de puertas: ")), input("ingrese Version: "))
        else:
            auto=AutoUsado(input("Ingrese Modelo: "), float(input("Ingrese Precio Base: ")), input("Ingrese Color: "), int(input("Ingrerse cant de puertas: ")), 
                        input("Ingrese Marca: "),int(input("Ingrese Km: ")), int(input("Ingrese año: ")), input("Ingrese patente: "))
        try:
            elementos.insertarElemento(auto,int(input("Ingrese posicison: ")))
        except IndexError:
            print("Pocision No valida")

    def Agregar(self, elementos):
        print("Agregar Vehiculo")
        if input("Ingrese N para vehiculo Nuevo, U para Usado: ").lower() == "n":
            auto = AutoNuevo(input("Ingrese Modelo: "), float(input("Ingrese Precio Base: ")),
                            input("Ingrese Color: "), int(input("Ingrerse cant de puertas: ")), input("ingrese Version: "))
            if AutoNuevo.getmarca() =="":
                print("No se registra marca para los autos nuevos")
                AutoNuevo.setmarca(input("Ingrese la marca de los autos Nuevos: "))
        else:
            auto=AutoUsado(input("Ingrese Modelo: "), float(input("Ingrese Precio Base: ")), input("Ingrese Color: "), int(input("Ingrerse cant de puertas: ")), 
                        input("Ingrese Marca: "),int(input("Ingrese Km: ")), int(input("Ingrese año: ")), input("Ingrese patente: "))
        elementos.agregarElemeto(auto)
    def Mostrarpos(self, elementos):
        print("Mostrar vehiculo en la posicison dada")
        try:
            aux = elementos.MostrarElemento(int(input("Ingrese la posicion: ")))
        except IndexError:
            print("Posicion Invalida")
        else:
            if isinstance(aux, AutoNuevo):
                print("El Auto en esta posicion es un auto Nuevo")
            else:
                print("El Auto en esta posicion es un auto Usado")
    def Modifbase(self, elementos):
        print("Modificar precio base")
        aux=elementos.base(input("Ingrese la patente: "))
        aux.setpb(float(input("Ingrese El precio Nuevo: ")))
        print("El Nuevo precio de venta es {:.2f}".format(aux.Importe()))
    def vehiculoeconomico(self, elementos):
        print("Vehiculo mas economico")
        print(elementos.menorprecio())
    def mostrar(self, elementos):
        print("Mostrando todos los vehiculos")
        print(elementos.Mostrar())
    def guardar(self, elementos):
        print("Guardando vehiculos")
        obj = ObjectEncoder()
        if obj.Guardar(elementos.toJSON(), "vehiculos.json"):
            print("Guardado Exitoso")
        else:
            print("Error al Guardar")