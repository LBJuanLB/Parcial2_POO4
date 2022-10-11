from pagina import  Pagina

class Libro:
    def __init__(self,titulo,isbn,autor,añoPublicacion):
        """Inicializador de la clase Libro
        Args:
            self.titulo (string): Titulo del libro
            self.isbn (long): ISBN (Identificador unico para libros) del libro
            self.autor (string): Nombre del autor del libro
            self.añoPublicacion (int): Año de publicacion del libro
        """
        self.titulo=titulo
        self.isbn=isbn
        self.autor=autor
        self.añoPublicacion=añoPublicacion
        self.paginas=[]   #self.paginas (list): Una lista que contiene instancias de la clase Pagina, son las paginas que tiene el libro
    '''
    GETERS
    getTitulo -> string: Retorma el titulo del libro
    getIsbn -> long: Retorma el ISBN del libro
    getAutor -> string: Retorma el nombre del autor del libro
    getAñoPublicacion -> int: Retorna el año de publicacion del libro
    '''
    def getTitulo(self):
        return self.titulo
    def getIsbn(self):
        return self.isbn
    def getAutor(self):
        return self.autor
    def getAñoPublicacion(self):
        return self.añoPublicacion
    '''
    SETERS
    setTitulo -> none: Modifica el titulo
    setIsbn -> none: Modifica el ISBN del libro
    setAutor -> none: Modifica el nombre del autor del libro
    setAñoPublicacion -> none: Modifica el año de publicacion del libro
    '''
    def setTitulo(self,titulo):
        self.titulo=titulo
    def setIsbn(self,isbn):
        self.isbn=isbn
    def setAutor(self,autor):
        self.autor=autor
    def setAñoPublicacion(self,añoPublicacion):
        self.añoPublicacion=añoPublicacion
    '''
    IngresarPagina -> none: Ingresa una pagina, que es una clase Pagina a la lista
    '''
    def IngresarPagina(self,contenido,numero):
        pagina=Pagina(contenido,numero)
        self.paginas.append(pagina)
    '''
    MostrarLibro -> none: Muestra toda la informacion del libro, incluso las paginas
    '''
    def MostrarLibro(self):
        print("Titulo:",self.titulo)
        print("Autor:",self.autor)
        print("Año de pubiclacion:",self.añoPublicacion)
        print("Isbn:",self.isbn)
        print()
        print("Contenido del libro")
        self.MostrarPaginas()
    '''
    MostrarPaginas -> none: Muestra todas las paginas que se hayan ingresado
    '''
    def MostrarPaginas(self):
        for pagina in self.paginas:
            print()
            print("Numero de pagina:",pagina.getNumero())
            print(pagina.getContenido())
    '''
    MostrarPagina -> none: Muestra una pagina en especifico, buscada por el numero de pagina
    '''
    def MostrarPagina(self,numero):
        for pagina in self.paginas:
            if pagina.getNumero()==numero:
                print("Numero de pagina:",pagina.getNumero())
                print(pagina.getContenido())
    '''
    EditarContenidoPagina -> none: Permite modificar el contenido de una pagina, buscandola por el numero
    '''
    def EditarContenidoPagina(self,contenido,numero):
        for pagina in self.paginas:
            if pagina.getNumero()==numero:
                pagina.setContenido(contenido)
    '''
    EditarNumeroPagina -> none: Permite modificar el numero de una pagina por otro
    '''
    def EditarNumeroPagina(self,numeroActual,numeroNuevo):
        for pagina in self.paginas:
            if pagina.getNumero()==numeroNuevo:
                print("Ya hay una pagina con el numero",numeroNuevo,"de pagina")
                break
            elif pagina.getNumero()==numeroActual:
                pagina.setNumero(numeroNuevo)