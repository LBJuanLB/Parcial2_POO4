from libro import Libro

#Creamos un libro 
libro=Libro("El Principito","1203912301202","Antoine de Saint-Exupéry","6/4/1943")

print("1. Creamos una pagina")
libro.IngresarPagina("Cuando yo tenía seis años vi en un libro sobre la selva virgen que se titulaba Historias vividas, una magnífica lámina. Representaba una serpiente boa que se tragaba a una fiera. En el libro se afirmaba: La serpiente boa se traga su presa entera, sin masticarla. Luego ya no puede moverse y duerme durante los seis meses que dura su digestión.",1)
print("2. Creamos otra pagina")
libro.IngresarPagina("Hola Mundo",2)
print("3. Cambiamos el contenido de la pagina")
libro.EditarContenidoPagina("Hello world",2)
print("4. Mostramos pagina")
libro.MostrarPagina(2)
print("5. Cambiamos el numero de pagina")
libro.EditarNumeroPagina(2,1)
print("6. Cambiamos el numero de pagina")
libro.EditarNumeroPagina(2,241)
print("7. Mostramos el contenido del libro")
libro.MostrarLibro()