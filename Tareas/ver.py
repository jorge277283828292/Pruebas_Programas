from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def ver_tareas():
    opcion = input("Deseas ver tua tareas eliminadas?, Todas las tareas?, o ya las conpletadas? (E/T/C) ")
    if opcion == "E":
        if not Tareas_eliminadas:
            print("No hay tareas eliminadas")
        else:
            print(f"Tareas completadas: {Tareas_eliminadas}")
    elif opcion == "T":        
        if not Tareas:
            print("No hay tareas")
        else:
            print(f"Tareas: {Tareas}")
    elif opcion == "C":
        if not Tareas_completadas:
            print("No hay tareas incompletas")
        else:
            print(f"Tareas incompletas: {Tareas_completadas}")