from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def eliminar_tareas():
    if not Tareas:
        print("No hay tareas para eliminar")
    else:
        print(f"{Tareas}")
        eliminar = input("Cual tarea deseas eliminar? ")
        if eliminar in Tareas:
            Tareas.remove(eliminar)
            Tareas_eliminadas.append(eliminar)
            print("Tarea eliminada")
        else:
            print("Tarea no encontrada")
    