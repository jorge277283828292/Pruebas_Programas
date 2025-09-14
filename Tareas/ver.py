from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def ver_tareas():
    print(" ")
    opcion = input("Deseas ver tua tareas eliminadas?, Todas las tareas?, o ya las conpletadas? (E/T/C) ")
    print(" ")
    if opcion == "E":
        if not Tareas_eliminadas:
            print(" ")
            print("No hay tareas eliminadas")
            print(" ")
        else:
            for t_e in Tareas_eliminadas:
                print(" ")
                print(f" Tareas Elimiinadas: {t_e}") 
                print(" ")
    elif opcion == "T":        
        if not Tareas:
            print(" ")
            print("No hay tareas")
            print(" ")
        else:
            for t_t in Tareas: 
                print(" ")
                print(f"Tareas: {t_t}")
                print(" ")
    elif opcion == "C":
        if not Tareas_completadas:
            print(" ")
            print("No hay tareas incompletas")
            print(" ")
        else:
            for t_c in Tareas_completadas:
                print(" ")
                print(f"Tareas Completadas: {t_c}")
                print(" ")
    else:
        print(" ")
        print("Opcion no valida")
        print(" ")