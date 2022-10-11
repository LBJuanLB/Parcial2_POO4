from circunferenciaCentrada import CircunferenciaCentrada
from punto import Punto

#Creamos un punto
punto=Punto(2,4)
#Creamos una circunferencia con radio 5 y el punto(2,4)
circunferencia=CircunferenciaCentrada(5,punto)
circunferencia.MostrarInformacion()

print("1. Cambiamos el radio")
circunferencia.setRadio(3)
circunferencia.MostrarInformacion()

print("2. Cambiamos el diametro")
circunferencia.setDiametro(20.4)
circunferencia.MostrarInformacion()

print("3. Cambiamos la longitud")
circunferencia.setLongitud(15.2)
circunferencia.MostrarInformacion()

print("4. Cambiamos el area")
circunferencia.setArea(40)
circunferencia.MostrarInformacion()

print("5. Cambiajos el punto x")
circunferencia.setXCentro(4)
circunferencia.centro.MostrarPunto()

print("6. Cambiamos el punto y")
circunferencia.setYCentro(6)
circunferencia.centro.MostrarPunto()

print("7.Trasladamos la circunferencia")
circunferencia.trasladarCircunferenciaCentrada(1,1)
circunferencia.centro.MostrarPunto()