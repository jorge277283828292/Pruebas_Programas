from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def tareas_completadas():
    if not Tareas:
        print(" ")
        print("No hay tareas para marcar como completadas.")
        print(f"Tareas: {Tareas}")
        print(" ")
    else:
        print(" ")
        print(f"Tareas: {Tareas}")
        marcar = input("Cual tarea deseas marcar como completada? ")
        if marcar in Tareas:
            Tareas.remove(marcar)
            Tareas_completadas.append(marcar)
            print("Tarea marcada como completada")
            print(" ")
            