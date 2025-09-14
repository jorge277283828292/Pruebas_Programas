from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def ver_tareas():
    opcion = input("Deseas ver tua tareas eliminadas?, Todas las tareas?, o ya las conpletadas? (E/T/C) ")
    if opcion == "E":
        if not Tareas_eliminadas:
            print("No hay tareas eliminadas")
        else:
            for t_e in Tareas_eliminadas:
                print(f" Tareas Elimiinadas: {t_e}") 
    elif opcion == "T":        
        if not Tareas:
            print("No hay tareas")
        else:
            for t_t in Tareas: 
                print(f"Tareas: {t_t}")
    elif opcion == "C":
        if not Tareas_completadas:
            print("No hay tareas incompletas")
        else:
            for t_c in Tareas_completadas:
                print(f"Tareas Completadas: {t_c}")
    else:
        print("Opcion no valida")