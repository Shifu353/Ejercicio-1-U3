class Capitulo (object):
    __titulo = ""
    __cantPaginas = 0

    def __init__ (self, titulo, cantP):
        self.__titulo = titulo
        self.__cantPaginas = cantP

    def getTitulo (self):
        return self.__titulo

    def getCantPaginas (self):
        return self.__cantPaginas
