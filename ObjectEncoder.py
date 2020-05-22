import json
class ObjectEncoder(object):
    def Guardar(self, elementos, archivo):
        with open(archivo, "w", encoding="UTF-8")as file:
            json.dump(elementos, file, indent=4)
        return True
    def Leer(self, archivo):
        with open(archivo, encoding="UTF-8")as file:
            aux = json.load(file)
        return aux
    def Decoder(self, diccionario):
        pass #No he entendido como realizar la lectura del
             #diccionario para Guardarlo en un objecto