class Calle:
    def __init__(self,numero):
        """Inicializador de la clase Calle
        Args:
            self.numero (int): Numero de la calle
        """
        self.numero=numero
        self.atleta=""      #self.atleta (string): Nombre del atleta
        self.tiempo=0       #self.tiempo (double): Tiempo que le tomo al atleta recorrer la calle
    '''
    GETERS
    getNumero -> int: Retorna el numero de la calle
    getAtleta -> string: Retorna el nombre del atleta 
    getTiempo -> double: Retorna el tiempo que hizo el atleta en esa calle
    '''
    def getNumero(self):
        return self.numero
    def getAtleta(self):
        return self.atleta
    def getTiempo(self):
        return self.tiempo
    '''
    SETERS
    setAtleta -> none: Modifica el nombre del atleta que corrio en la calle
    setTiempo -> none: Modifica el tiempo del atleta que hiz en la calle
    '''
    def setAtleta(self,atleta):
        self.atleta=atleta
    def setTiempo(self,tiempo):
        self.tiempo=tiempo