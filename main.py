from DAO_Carrera import DAO_Carrera


def main():

    
    print("Hola, bienvenido al sistema de administracion de Carreras")
    contraseña = str(input("Introduzca la contraseña"))
    menu = """
        ===== Gestión de Carreras =====

        Seleccione una opción:

        1. Añadir carrera
        2. Actualizar carrera
        3. Ver carreras
        4. Borrar carrera
        5. Salir

        ===============================
        """
    query = DAO_Carrera(contraseña)
    print(menu)

    opcion = 0
    while opcion != 5:
        opcion = int(input("¿Que deseas hacer?: "))
        print(menu)
        if opcion == 1:
            nombre = str(input("Dime el nombre de la carrera: "))
            duracion = int(input("Duracion de la carrera en años: "))
            nota = int(input("Nota de corte para entrar: "))
            query.añadir_carrera(nombre, duracion, nota)
        elif opcion == 2:
            query.ver_carreras()
            id = int(input("Dime la carrera que deseas actualizar "))
            nombre = str(input("Dime el nuevo nombre de la carrera: "))
            duracion = int(input("Nueva duracion de la carrera: "))
            nota = int(input("Nueva nota de corte: "))
            query.actualizar_carrera(id, nombre, duracion, nota)
        elif opcion == 3:
            query.ver_carreras()
        elif opcion == 4:
            id = int(input("Dime la carrera que deseas borrar "))
            query.borrar_carrera(id)
            pass
        elif opcion == 5:
            pass
        else:
            print("Seleccione una opcion valida: Número del 1 al 5")
            pass
