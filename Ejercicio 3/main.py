from carrera import Carrera

#Creamos una carrera
carrera1=Carrera(30,1,"20/01/2022")
#Agregamos 3 calles
carrera1.agregarCalle(1,"Juan",20)
carrera1.agregarCalle(2,"Juan",50)
carrera1.agregarCalle(3,"Juan",20)
#Mostramos el tiempo total
print("Tiempo total:",carrera1.tiempoTotal("Juan"))