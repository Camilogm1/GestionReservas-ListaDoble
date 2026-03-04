from ListaDobleReserva import ListaDobleReserva

def menu():
    lista = ListaDobleReserva()
    """instancia una lista """
    while True:
        print("\n" + "="*40)
        print("1.Insertar 2.Buscar 3.Eliminar 4.Actualizar")
        print("5.Mostrar  6.Ordenar 7.Estadisticas  8.Salir")
        print("="*40)
        op = input("Seleccione una opcion: ")
        """menu e input para seleccionar la opcion del menu"""
        try:
            if op == "1":
                nom = input("Nombre del Cliente: ")
                id_res = int(input("ID de Reserva: "))
                cost = float(input("Costo del Tour: "))
                lista.insertar_al_final(nom, id_res, cost)
                """con 3 inputs guarda los datos que se desean insertar y usa la funcion insertar_al_final para agregar a la lista"""

            elif op == "2":
                id_bus = int(input("ID a buscar: "))
                res = lista.buscar(id_bus)
                if res:
                    print(f"Resultado: {res.reserva.cliente} - ${res.reserva.costo}")
                else:
                    print("Reserva no encontrada.")
                """pregunta el id que se desea buscar, usa la funcion buscar para encontrarlo y muestra el resultado o 
                un mensaje de no encontrado"""

            elif op == "3":
                id_del = int(input("ID a eliminar: "))
                lista.eliminar(id_del)
                """busca el id que se desea eliminar, usa la funcion eliminar para eliminarlo de la lista y muestra un mensaje
                  de eliminado o no encontrado"""
                
            elif op == "4":
                id_act = int(input("ID a actualizar: "))
                if lista.buscar(id_act):
                    nom_n = input("Nuevo Nombre: ")
                    cost_n = float(input("Nuevo Costo: "))
                    lista.actualizar(id_act, nom_n, cost_n)
                else:
                    print("ID no existe.")
                    """busca el id que se desea actulizar, si lo encuntra pide el nuevo nombre y costoy luego usa la funcion actualizar """

            elif op == "5":
                sub_v = input("a.Ascendente / d.Descendente: ").lower()
                lista.imprimir(ascendente=(sub_v == "a"))
                """pregunta si se desea mostrar de forma ascendente o descendente, y usa la funcion imprimir, y como en la funcion se defino 
                que si el parametro ascendente es un true, si el valor no es 'a' se muestra de forma descendente"""

            elif op == "6":
                print("\n--- MENU DE ORDENAMIENTOS ---")
                """cree un sumbmenu para los ordenamientos, ya que se pueden ordenar de 3 formas diferentes
                , por costo con desempate de nombre, por nombre de forma ascendente o por nombre de forma descendente"""

                sub = input("a.Costo (Desempate Nombre) | b.Nombre A-Z | c.Nombre Z-A: ").lower()
            
                if sub == "a":
                    lista.ordenar_por_costo_con_desempate()
                    print("\n>>> LISTA ORDENADA POR COSTO Y NOMBRE:")
                elif sub == "b":
                    lista.ordenar_por_cliente(ascendente=True)
                    print("\n>>> LISTA ORDENADA POR NOMBRE (A-Z):")
                elif sub == "c":
                    lista.ordenar_por_cliente(ascendente=False)
                    print("\n>>> LISTA ORDENADA POR NOMBRE (Z-A):")

                """dependiendo de la opcion seleccionada por el usuario, se usa o la funcion de ordenaminto por costo o la de ordenamiento por nombre, y se muestra un mensaje indicando el tipo de ordenamiento realizado
                por cliente, esta ultima se puede escojer si se desea de forma ascendente o descendente"""
                

                lista.imprimir(ascendente=True)
                input("\nPresione ENTER para volver al menú principal...")
                """muestra la lista actualizada despues del ordenamiento sin necesidad de seleccionar la opcion 5 del menu, y luego pide al usuario que presione enter 
                para volver al menu principal(para que se pueda ver el resultado antes de seguir con el menu)"""
            elif op == "7":

                lista.generar_estadisticas() 
                """usa la funcion generar estadisticas para generarlas """
                input("\nPresione ENTER para continuar...")

            elif op == "8":
                print("Saliendo del programa...")
                break

        except ValueError:

            print("\nError: Por favor ingrese unicamente numeros para el ID y el Costo.")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}")
            
        """Try except para manejar errores, si el usuario ingresa un valor no numerico para el ID o el costo, se muestra un mensaje de error, 
        y si ocurre cualquier otro error inesperado, se muestra el mensaje del error"""
        
if __name__ == "__main__":
    menu()