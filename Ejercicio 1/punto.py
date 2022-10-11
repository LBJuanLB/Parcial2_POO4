class Punto:
    def __init__(self,coord_x,coord_y):
        """Inicializador de la clase Punto
        Args:
            self.coord_x (double): Valor del punto en el eje X
            self.coord_y (double): Valor del punto en el eje Y
        """
        self.coord_x=coord_x
        self.coord_y=coord_y

    """
    getX-> double: devuelve el valor del punto en el eje x
    setX -> none: cambia el valor del putno en el eje x
    """
    def getX(self):
        return self.coord_x
    def setX(self,x):
        self.coord_x=x
    """
    getY -> double: devuelve el valor del punto en el eje y
    setY -> none: cambia el valor del putno en el eje y
    """
    def getY(self):
        return self.coord_y
    def setY(self,y):
        self.coord_y=y
    """
    MostrarPunto -> none: Muestra los valores que tiene el punto
    """
    def MostrarPunto(self):
        print("Punto x:",self.coord_x)
        print("Punto y:",self.coord_y)
        print()