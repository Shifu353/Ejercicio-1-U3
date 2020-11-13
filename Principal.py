from ClaseCapitulo import Capitulo
from ClaseLibro import Libro
from ManejadorLibro import ListaLibros

if __name__ == "__main__":
    import csv
    archivo = open("libros.csv")
    leer = csv.reader(archivo,delimiter=";")
    manejador = ListaLibros()
    for libro in leer:
        if len(libro) == 6:
            libros = Libro(int(libro[0]),libro[1],libro[2],libro[3],int(libro[4]),libro[5])
            manejador.AgregarLista(libros)
        else:
            libros.AgregarCapitulo(Capitulo(libro[0],int(libro[1])))
    def op1 ():
        identificador = int(input("Ingrese identificador del libro: "))
        manejador.Item1(identificador)

    def op2 ():
        palabra = input("Ingrese palabra a buscar: ")
        manejador.Item2(palabra.lower())
    
    def op3 ():
        print("Saliendo....")
    opcion = None
    diccionario = {1:op1,2:op2,3:op3}

    while opcion != 3:
        print("|---------------------Menu de Ociones--------------------------|")
        print("| Ingrese 1 para Mostrar titulo de un libro                    |")
        print("| Ingrese 2 para mostrar titulo y autor de un libro o capitulo |")
        print("| Ingrese 3 para salir                                         |")
        print("|--------------------------------------------------------------|")
        opcion = int(input("Ingrese una opcion: "))
        op = diccionario.get(opcion,lambda: print("Opcion incorrecta"))
        op()
