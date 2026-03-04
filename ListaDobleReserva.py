from Reserva import Reserva
from Nodo import Nodo

class ListaDobleReserva:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
        """constructor de la clase"""
        

    def buscar(self, id_buscado):
        actual = self.cabeza 
        while actual:
            if actual.reserva.id_reserva == id_buscado:
                return actual
            actual = actual.siguiente
            """recorre toda la lista verificando si el id de la reserva coincide con el que se busca"""
        return None
    """si no se encuentra el id, devuelve None"""

    def insertar_al_final(self, cliente, id_reserva, costo):
        if self.buscar(id_reserva):
            print(f"Error: El ID {id_reserva} ya existe.")
            return
        """use la funcion anterior para asegurar que los id si son unicos """
        nueva_reserva = Reserva(cliente, id_reserva, costo)
        nuevo_nodo = Nodo(nueva_reserva)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            """si la lista esta vacia, el nuevo nodo es cabeza y cola """
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.contador += 1
        print("Reserva añadida.")
        """si la lista no esta vacia, reajusta las referencias y suma el contador """

    def eliminar(self, id_reserva):
        nodo = self.buscar(id_reserva)
        if not nodo:
            print("No se encontro.")
            return
        """busca el nodo a eliminar por su id, si no se encuentra, muestra mensaje y retorna """
        if nodo == self.cabeza and nodo == self.cola:
            self.cabeza = self.cola = None
            """si el nodo que se quiere eliminar es el unico en la lista, esta se vacia """

        elif nodo == self.cabeza:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            """si el nodo que se quiere eliminar es la cabeza, se re ajusta la referencia de la nueva cabeza"""
        elif nodo == self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            """si el nodo que se quiere eliminar es la cola, se re ajusta la referencia de la nueva cola"""
        else:
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior
        self.contador -= 1
        """si el nodo que se quiere eliminar esta en el medio, se re ajustan ls referencias del nodo anterior y el siguiente,
          y se resta el contador """
        print(f"ID {id_reserva} eliminado.")

    def actualizar(self, id_reserva, nuevo_nombre, nuevo_costo):
        nodo = self.buscar(id_reserva)
        if nodo:
            nodo.reserva.cliente = nuevo_nombre
            nodo.reserva.costo = max(0, nuevo_costo)
            print("Actualizado.")
            """primero busca el nodo a actualizar por su id, si se encuentra, actualiza el nombre y costo asegurandose de que 
            este no sea negativo"""
        else:
            print("No encontrado.")

    def imprimir(self, ascendente=True):
        actual = self.cabeza if ascendente else self.cola
        """depende si se desea de forma ascendente o descendente, se inicia en la cabeza o la cola respectivamente"""
        if not actual:
            print("Vacia.")
            return
        """"si la lista esta vacia, muestra mensaje y retorna """
        print(f"--- Reporte {'Asc' if ascendente else 'Desc'} ---")
        while actual:
            r = actual.reserva
            print(f"ID: {r.id_reserva} | Cliente: {r.cliente} | Costo: ${r.costo}")
            actual = actual.siguiente if ascendente else actual.anterior
        """recorre la lista en orden e imprime los detalles de cada reserva"""

    def _intercambiar_nodos(self, nodo1, nodo2):
        prev1 = nodo1.anterior
        next2 = nodo2.siguiente
        """primero se definen las referencia del nodo anterior al 1 y el siguiente al 2"""
        if prev1:prev1.siguiente = nodo2
        
        else: self.cabeza = nodo2
        """si el nodo anterior al 1 existe, se le asigna como siguiente al nodo 2, sino el nodo 2 se convierte en la nueva cabeza"""

        if next2: next2.anterior = nodo1
        else: self.cola = nodo1
        """si el nodo anterior al 2 existe, se le asigna como anterior al nodo 1, sino el nodo 1 se convierte en la nueva cola"""
    
        nodo2.anterior = prev1
        nodo2.siguiente = nodo1
        nodo1.anterior = nodo2
        nodo1.siguiente = next2
        """"aca se intercambian las referencias del nodo 1 y el nodo 2, el nodo 2 se coloca antes del nodo 1"""

    def ordenar_por_costo_con_desempate(self):
        if not self.cabeza or not self.cabeza.siguiente: return
        """si la lista esta vacia o tiene un solo nodo, no se necesita ordenar"""
        intercambio = True
        while intercambio:
            intercambio = False
            """ponemos una "bandera" para poder saber si se hizo un intercambio, si no se hizo ninguno, 
            la lista ya esta ordenada y se puede salir del bucle"""
            actual = self.cabeza
            while actual and actual.siguiente:
                n1, n2 = actual, actual.siguiente
                c1, c2 = n1.reserva.costo, n2.reserva.costo
                nom1, nom2 = n1.reserva.cliente.lower(), n2.reserva.cliente.lower()
                """primero se definen las variables para comparar el costo y el nombre de los clientes"""
                # Criterio de ordenamiento y desempate 
                if (c1 > c2) or (c1 == c2 and nom1 > nom2):
                    self._intercambiar_nodos(n1, n2)
                    intercambio = True
                else:
                    actual = actual.siguiente
                """si el costo del nodo 1 es mayor al costo del nodo 2, o si los costos son iguales pero el nombre del cliente del 
                nodo 1 es mayor al del nodo 2, se intercambian los nodos y se marca que hubo un intercambio, sino se avanza al 
                siguiente nodo"""

    def ordenar_por_cliente(self, ascendente=True):
        if not self.cabeza or not self.cabeza.siguiente: return
        intercambio = True
        """define la bandera """
        while intercambio:
            intercambio = False
            actual = self.cabeza
            """define las vaeriables para recorrer la lista"""
            while actual and actual.siguiente:
                n1, n2 = actual, actual.siguiente
                nom1, nom2 = n1.reserva.cliente.lower(), n2.reserva.cliente.lower()
                """obtine los nombres de los clientes """
                # Intercambio por nombre 
                if (ascendente and nom1 > nom2) or (not ascendente and nom1 < nom2):
                    self._intercambiar_nodos(n1, n2)
                    intercambio = True
                else:
                    actual = actual.siguiente
                """si se desea orden ascendente y el nombre del nodo 1 es mayor al del nodo 2, o si se desea orden descendente y el 
                nombre del nodo 1 es menor al del nodo 2, se intercambian los nodos"""

    def generar_estadisticas(self):
        if not self.cabeza: return
        suma = 0
        maximo = minimo = self.cabeza.reserva.costo
        actual = self.cabeza
        """inicializa las variables"""
        while actual:
            v = actual.reserva.costo
            suma += v
            if v > maximo: maximo = v
            if v < minimo: minimo = v

            actual = actual.siguiente
            """recorre la lista, hace la suma de los costos y avtualiza el maximo y el minimo mientrentras avanza"""

        self.ordenar_por_costo_con_desempate()
        mitad = self.contador // 2
        temp = self.cabeza
        for _ in range(mitad): temp = temp.siguiente
        mediana = (temp.anterior.reserva.costo + temp.reserva.costo) / 2 if self.contador % 2 == 0 else temp.reserva.costo
        """calcula primero la mitad de la lista, luego avanza hasta que llega a la posicion de la mitad, dependiendo
        si es par o inpar la cantidad de datos calcula la mediana """
 
        moda = self.cabeza.reserva.costo
        max_frec = 0
        actual = self.cabeza
        while actual:
            c_actual, f_actual, aux = actual.reserva.costo, 0, actual
            """este primer while recorre la lista por grupos, no nodo por nodo (salta en valores diferentes)"""
            while aux and aux.reserva.costo == c_actual:
                f_actual += 1
                aux = aux.siguiente
            """este segundo while cuenta la frecuencia de cada valor, mientras que los valores sean iguales, avanza y suma la frecuencia"""
            if f_actual > max_frec:
                max_frec = f_actual
                moda = c_actual

            actual = aux
            """al ayudarse entre los bucles, este seria un orden de magnitud O(n) para calcular la moda, ya que cada nodo se visita una sola vez, aunque se tengan que contar las frecuencias 
                de los valores iguales."""
             
        """calcula la moda recoriendo la lista"""
        print(f"\n--- ESTADISTICAS ---")
        print(f"Total: {self.contador} | Promedio: ${suma/self.contador:.2f}") 
        print(f"Max: ${maximo} | Min: ${minimo} | Rango: ${maximo-minimo}") 
        print(f"Mediana: ${mediana} | Moda: ${moda} (Frec: {max_frec})") 