from repositorios import Repositorios


class ProductoService():

    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        new = int(lastKey) + 1
        Repositorios.productosList[new] = producto.__dict__
        return new

    def delete_producto(self, key=0):
        del Repositorios.productosList[key]

    def get_productosList(self):
        return Repositorios.productosList
