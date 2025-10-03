class Carrera:

    def __init__(self, nombre, duracion, notas):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__notas = notas


    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        self.__notas = notas

    def __str__(self):
        return f"Carrera: {self.__nombre}, Duración: {self.__duracion}, Notas: {self.__notas}"
