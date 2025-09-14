from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def eliminar_tareas():
    if not Tareas:
        print(" ")
        print("No hay tareas para eliminar")
        print(" ")
    else:
        print(" ")
        print(f"{Tareas}")
        eliminar = input("Cual tarea deseas eliminar? ")
        if eliminar in Tareas:
            Tareas.remove(eliminar)
            Tareas_eliminadas.append(eliminar)
            print("Tarea eliminada")
            print(" ")
        else:
            print(" ")
            print("Tarea no encontrada")
            print(" ")