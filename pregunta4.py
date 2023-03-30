
class Alumno:
    def  __init__(self,nombre,nota):
        self.nombre= nombre
        self.nota = nota
        print("El alumno se ha creado con éxito")

    def __str__(self):
        return(f"El alumno {self.nombre} su nota es {self.nota}.")

    def calificacion(self):
        if self.nota>=5:
            return("El alumno ha aprobado.")
        elif self.nota<5:
            return("El alumno ha suspendido.")


Alumno("Carlos",6.7)
