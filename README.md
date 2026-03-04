El contexto del programa trara sobre una agencia de viaje que desea organizar sus reservas. En este contexto es mas como utilizar listas 
Doblemente ligadas debido a que se requiere recorrer la lista tanto al derechocomo al revez.

Para que funcione solo se requiere tener los 4 archivos y ejecutar el main.py, despues de ejecutarse una vez se van a guardar unos
"archivos".pyc, que son bytecode, es decir si se vuelve a ejecutar y no a cambiado nada, el programa lee directamente los .pyc

Algunas desiciones de diseño que tome son: Implementar una funcion intercambiar_nodos, esto debido a que era algo que se usa 
frecuentemente en las funciones de ordenaminto, y por comodidad era mas facil definirlo como funcion. Implemente un submenu en el menu
del main, para mostrar las 4 formas de ordenar la lista de una forma mas ordenada y tambien implemente un nuevo metodo de ordenamiento 
que es ordenar por id, para volver a la lista original despues de ordenerla de alguna manera (cosa que no se puede sin el metodo)

Como Herramienta de apoyo use Gemini. algunos promts que use fueron: "Como intercambiar dos nodos físicos en una lista doble en Python
sin que se rompa el orden de la lista?", "Algoritmo para la moda en una lista que ya está ordenada.", "Como vincular 2 archivos diferentes
en pyton?","el primer punto es para especificar cual nodo y el siguient . es para especificar a donde va a apuntar?"

La complejidad general del programa está determinada por sus operaciones más pesadas:empezando por operaciones simples como un print o 
un input son de orden O(1),Operaciones de búsqueda de ID, eliminación y cálculos estadísticos son de orden O(n),en el peor caso necesita
recorrer hasta el final de la lista pero con un solo ciclo, pero los metedos de ordenamiento requieren 2 ciclos anidados para comparar 
y mover nodos, por lo que son de orden O(n^2) y como este es el mayor orden que se presenta entonces, es el orden final del codigo.

Nombre: Juan Camilo Gonzalez Muñeton 

