"""Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
"""



lista= [18, 50, 210, 80, 145, 333, 70, 30]

def multiplo(numero):
    lista2=[]
    for i in numero:
        if i%10==0 and i<=200:
            lista2.append(i)
        else:
            pass
    return lista2

def parar_en_300(numero):
    for i in numero:
        if i <300:
            break

def organizar(numero):
    lista2 = sorted(numero)
    return lista2
def el_indice(numero):
    lista_organizado=organizar(numero)
    lista_organizado.append(145)
    for i ,n in enumerate(lista_organizado):
        if 145 in lista_organizado :
            return "El índice de 145 es:", i
        elif not 145 in lista_organizado:
            return -1

multiplo(lista)
parar_en_300(lista)
organizar(lista)
el_indice(lista)