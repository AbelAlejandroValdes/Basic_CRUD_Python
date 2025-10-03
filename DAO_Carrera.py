import mysql.connector

class DAO_Carrera:
    def __init__(self,password):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="universidad"
        )
        self.mycursor = self.mydb.cursorx

    def añadir_carrera(self, nombre, duracion, nota):
        val = (nombre, duracion, nota)
        sql = "INSERT INTO carreras(Nombre, Duracion, Nota_de_Corte) VALUES (%s, %s, %s)"
        self.mycursor.execute(sql, val)
        self.mydb.commit() 
        print("Carrera añadida exitosamente.")

    def actualizar_carrera(self,id,nombre,duracion,nota):


        if self.comprobar_carrera(id):
                sql_update = "UPDATE Carreras SET nombre = %s, duracion = %s, nota_de_corte = %s WHERE idCarrera = %s"
                val = (nombre, duracion, nota,id )
                self.mycursor.execute(sql_update, val)
                self.mydb.commit()
                print("✅ Carrera actualizada correctamente.")
        else:
                print(f"❌ No se encontró ninguna carrera con el ID {id}.")


    def ver_carreras(self):
        self.mycursor.execute("SELECT * FROM carreras")

        myresult = self.mycursor.fetchall()

        for row in myresult:
                print(row)

    def borrar_carrera(self,id):

        if self.comprobar_carrera(id):
                sql_delete = "DELETE FROM carreras WHERE idCarrera = %s"
                self.mycursor.execute(sql_delete, (id,))
                self.mydb.commit()
                print("✅ Carrera eliminada correctamente.")
        else:
                print(f"❌ No se encontró ninguna carrera con el ID {id}.")
        pass
    
    def comprobar_carrera(self,id):
        sql_check = "SELECT 1 FROM Carreras WHERE idCarrera = %s"
        self.mycursor.execute(sql_check, (id,))
        resultado = self.mycursor.fetchone()
        return resultado is not None

          