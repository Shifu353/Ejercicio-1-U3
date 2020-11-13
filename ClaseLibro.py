class Libro (object):
    __idLibro = 0
    __titulo = ""
    __autor = ""
    __editorial = ""
    __isbn = 0
    __CantidadCap = 0
    __Capitulos = None

    def __init__(self, id, titulo, autor, edi, isbn, cant):
        self.__idLibro = id
        self.__titulo = titulo
        self.__editorial = edi
        self.__autor = autor
        self.__isbn = isbn
        self.__CantidadCap = cant
        self.__Capitulos = []
    def getTitulo (self):
        return self.__titulo
    def AgregarCapitulo (self,uncapitulo):
        self.__Capitulos.append(uncapitulo)
    def getidLibro (self):
        return self.__idLibro
    def getCapitulos (self):
        return self.__Capitulos
    def getAutor (self):
        return self.__autor
