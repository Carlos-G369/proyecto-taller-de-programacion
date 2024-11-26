#Importamos las clases para instanciarlas, y la base de datos
from crear import Crear
from read import Read
from actualizar import Actualizar
from eliminar import Delete
from database import Database
from ordenar import Ordenar


def main():
    # Instanciar las clases
    create = Crear()
    read = Read()
    update = Actualizar()
    delete = Delete()
    ordenar = Ordenar()


    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Campeón, Ítem y Partida")
        print("2. Ver Campeones, Ítems y Partidas")
        print("3. Ver Partidas")
        print("4. Ver items")
        print("5. Actualizar Campeón")
        print("6. Actualizar item")
        print("7. Actualizar partida")
        print("8. Eliminar campeon")
        print("9. Eliminar partida")
        print("10. Eliminar item")
        print("11. Salir")
        print("12. Ordenar campeones por nombre")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear Campeón con Ítem y Partida
            create.nuevo_campeon()
        elif opcion == "2":
            # Leer Campeones, Ítems y Partidas
            read.listar_campeones()
        elif opcion == "3":
            #Leer partidas 
            read.listar_partidas()
        elif opcion == "4":
            #Listar items 
            read.listar_itmes()
        elif opcion == "5":
            # Actualizar Campeón y su Ítem Relacionado
            update.actualizar_campeon()
        elif opcion == "6":
            # Actualizar item
            update.actualizar_item()
        elif opcion == "7":
            #Actualizar partida
            update.actualizar_partida()
        elif opcion == "8":
            #Elimina al un campeon 
            delete.eliminar_campeon()
        elif opcion == "9":
            #Elimina un partida
            delete.eliminar_partida()
        elif opcion == "10":
            #Elimina un item 
            delete.eliminar_item()
        elif opcion == "11":
            # Salir del Programa
            print("¡Hasta luego!")
        elif opcion == "12":
            ordenar.ordenar_campeones()
            Database.close_connection()
            break

        else:
            print("Opción no válida. Por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()
