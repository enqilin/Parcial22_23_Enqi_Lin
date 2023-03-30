import unittest
import pregunta3 as p3

class Test(unittest.TestCase):

    def test_alumno(self):
        alumno1=p3.Alumno("Juan",4.5)
        alumno2=p3.Alumno("Carmen",7.5)
        self.assertEqual(alumno2.calificacion(),'El alumno ha aprobado.')
        self.assertEqual(alumno1.calificacion(),'El alumno ha suspendido.')
