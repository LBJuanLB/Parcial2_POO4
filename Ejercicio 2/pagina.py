class Pagina:
    def __init__(self,contenido,numero):
        """Inicializador de la clase Pagina
        Args:
            self.contenido (string): Contenido de la pagina
            self.numero (int): Numero de la pagina
        """
        self.contenido=contenido
        self.numero=numero
    '''
    GETERS
    getContenido -> string: Retorma el contenido de la pagina
    getNumero -> int: Retorma el numero de la pagina
    '''
    def getContenido(self):
        return self.contenido
    def getNumero(self):
        return self.numero
    '''
    SETERS
    setContenido -> string: Modifica el contenido de la pagina
    setNumero -> int: Modifica el numero de la pagina
    '''   
    def setContenido(self,contenido):
        self.contenido=contenido
    def setNumero(self,numero):
        self.numero=numero