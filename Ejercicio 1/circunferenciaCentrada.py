class CircunferenciaCentrada:
    def __init__(self,radio,Punto):
        """Inicializador de la clase CircunferenciaCentrada
        Args:
            self._radio (double): Radio de la circunferencia
            self._centro (Punto): Punto donde se encuentra la circunferencia
        """
        self.pi=3.1416  #self._pi (double): 3.1416 Valor de pi
        self.radio=radio
        self.centro=Punto
    """
    getRadio -> double: Devuelve el radio de la circunferencia
    setRadio -> none: Cambia el valor del radio
    """
    def getRadio(self):
        return self.radio
    def setRadio(self,radio):
        self.radio=radio
    """
    getDiametro -> double: diametro=2*radio   Formula para hallar el diametro de la circunferencia
    setDiametro -> none: radio=diametro/2   Sacamos el radio del diametro dado para cambiar el radio que habia
    """
    def getDiametro(self):
        return 2*self.radio
    def setDiametro(self,diametro):
        self.radio=diametro/2
    """
    getLongitud -> double: longitud=2*pi*radio   Formula para hallar la longitud de la circunferencia
    setDiametro -> none: radio=longitud/(2*pi)   Sacamos el radio con esta formula para cambiar el radio que habia
    """
    def getLongitud(self):
        return 2*self.pi*self.radio
    def setLongitud(self,longitud):
        self.radio=longitud/(2*self.pi)
    """
    getArea -> double : area=pi*radio^2   Formula para hallar el area de una circunferencia
    setAre -> none : radio= √(area/pi) Sacamos el radio con esta formula para cambiar el radio que habia
    """
    def getArea(self):
        return self.pi*(self.radio*self.radio)
    def setArea(self,area):
        self.radio=(area/self.pi)**(0.5)
    """
    getXCentro -> double: devuelve el valor del punto en el eje x
    setXCentro -> none: cambia el valor del putno en el eje x
    """
    def getXCentro(self):
        return self.centro.getX()
    def setXCentro(self,x):
        self.centro.setX(x)
    """
    getYCentro -> double: devuelve el valor del punto en el eje y
    setYCentro -> none: cambia el valor del putno en el eje y
    """
    def getYCentro(self):
        return self.centro.getY()
    def setYCentro(self,y):
        self.centro.setY(y)
    """
    trasladarCircunferenciaCentrada -> none: Cambia de ubicacion la circunferencia, 
                                             moviendola al punto (x,y) que se le haya enviado
    """
    def trasladarCircunferenciaCentrada(self,x,y):
        self.centro.setX(x)
        self.centro.setY(y)
    """
    MostrarInformacion -> none: Muestra en pantalla la informacion de la circunferencia 
    """
    def MostrarInformacion(self):
        print("Radio:",self.getRadio())
        print("Diametro:",self.getDiametro())
        print("Longitud:",self.getLongitud())
        print("Area:",self.getArea())
        print()