from listas import Tareas, Tareas_completadas, Tareas_eliminadas

def restaurar_tareas():
   if not Tareas_eliminadas:
       print("No hay tareas para restaurar")
   else:
        print(f"Tareas eliminadas: {Tareas_eliminadas}")
        restaurar = input("Cual tarea deseas restaurar? ")
        if restaurar in Tareas_eliminadas:
            Tareas_eliminadas.remove(restaurar)
            Tareas.append(restaurar)
            print("Tarea restaurada")