class nodo(object):
    def __init__(self):
        self.info = None
        self.sif = None
class datoPolinomio(object):
    def __init__(self,valor, termino):
        self.valor=valor
        self.termino = termino

class Polinomio(object):
    def __init__(self, termino_mayor = None,tamanio = -1):
        self.termino_mayor=termino_mayor
        self.tamanio = tamanio
    def agregar_termino(polinomio,termino , valor):

        aux=nodo()
        dato = datoPolinomio(valor,termino)
        aux.info=dato
