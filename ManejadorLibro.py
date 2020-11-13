import os
class ListaLibros (object):
    __lista = []

    def __init__ (self):
        self.__lista = []

    def AgregarLista (self,archivo):
        self.__lista.append(archivo)
    
    def BuscarLibro (self,iden):
        i = 0
        while i<len(self.__lista) and iden != int(self.__lista[i].getidLibro()):
            i += 1
        if i<len(self.__lista):
            return i
        return -1

    def Item1 (self, identificador):
        os.system("cls")
        buscar = self.BuscarLibro(identificador)
        if buscar != -1:
            capitulos = self.__lista[buscar].getCapitulos()
            print("Titulo del libro: {}".format(self.__lista[buscar].getTitulo()))
            print("--------Capitulos--------")
            i = 1 
            total = 0
            for capitulo in capitulos:
                print("Nombre del Capitulo {}: {}".format(i,capitulo.getTitulo()))
                i += 1
                total += capitulo.getCantPaginas()
            print("Cantidad de Paginas del libro ",total)
        else:
            print("No se encontro el libro")
        input("Precione una tecla para contunuar..")
        os.system("cls")

    def Item2 (self,palabra):
        os.system("cls")
        print("Resultados busqueda de:",palabra)
        for libro in self.__lista:
            capitulo = libro.getCapitulos()
            if libro.getTitulo().lower().count(palabra)!=0:
                print(libro.getTitulo(),"de",libro.getAutor())
            for cap in capitulo:
                if cap.getTitulo().lower().count(palabra)!=0:
                    print(cap.getTitulo(),"de",libro.getAutor())
        input("Precione una tecla para contunuar..")
        os.system("cls")
