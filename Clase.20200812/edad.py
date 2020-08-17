class Clase():
    def __init__(self, edad=17):
        self.edad = edad

    # getter
    @property
    def edad(self):
        return self.__edad

    # setter
    @edad.setter
    def edad(self, value):
        if value < 15:
            raise ValueError("Edad NO permitida")
        self.__edad = value


if __name__ == "__main__":
    objeto = Clase()

    while True:
        try:
            objeto.edad = int(input("Ingrese edad: "))
            break
        except ValueError as e:
            print(e)
