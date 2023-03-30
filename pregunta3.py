class Alumno:
    def  __init__(self,nombre,nota):
        self.nombre= nombre
        self.nota = nota
        print("El alumno se ha creado con éxito")

    def calificacion(self):
        if self.nota>=5:
            return("El alumno ha aprobado.")
        elif self.nota<5:
            return("El alumno ha suspendido.")