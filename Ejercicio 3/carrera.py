from calle import Calle

class Carrera:
    def __init__(self,distancia,ronda,fecha):
        """Inicializador de la clase Libro
        Args:
            self.distancia (int): Distancia total que tiene la carrera
            self.ronda (int): Ronda de la carrera
            self.fecha (string): Fecha de la carrera
        """
        self.distancia=distancia
        self.ronda=ronda
        self.fecha=fecha
        self.calle=[]     #self.calle (list): Una lista que contiene las calles que tiene la carrera
    '''
    GETERS
    getDistancia -> int: Retorna la distancia de la carrera
    getRonda -> int: Retorna la ronda de la carrera
    getFecha -> string: Retorna la fecha de la carrera
    '''
    def getDistancia(self):
        return self.distancia
    def getRonda(self):
        return self.ronda
    def getFecha(self):
        return self.fecha
    '''
    SETERS
    setDistancia -> none: Cambia la distancia de la carrera
    setRonda -> none: Cambia la ronda de la carrera
    setFecha -> none: Cambia la fecha de la carrera
    ''' 
    def setDistancia(self,distancia):
        self.distancia=distancia
    def setRonda(self,ronda):
        self.ronda=ronda
    def setFecha(self,fecha):
        self.fecha=fecha
    '''
    agregarCalle -> none: Agrega una calle a la carrera
    '''
    def agregarCalle(self,numero,atleta,tiempo):
        calle=Calle(numero)
        calle.setAtleta(atleta)
        calle.setTiempo(tiempo)
        self.calle.append(calle)
    '''
    tiempoTotal -> double: Nos da el tiempo que tuvo un atleta en toda la carrera, suma el tiempo que tuvo en cada calle
    '''
    def tiempoTotal(self,atleta):
        total=0
        for i in self.calle:
            if i.getAtleta() == atleta:
                total+=i.getTiempo()
        return total