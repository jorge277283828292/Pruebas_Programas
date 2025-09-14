from opciones import opcioness
from agregar import agregar_tareas
from quitar import eliminar_tareas
from ver import ver_tareas
from completadas import tareas_completadas
from restaurar import restaurar_tareas
from listas import Tareas, Tareas_completadas, Tareas_eliminadas
import time

while True:
    opcioness()
    opcion = input("Cual opcion deseas? ")
    if opcion == "1":
    #Agregar
        agregar_tareas()
        time.sleep(1.5)
        continue
    #Eliminar
    elif opcion == "2":
        eliminar_tareas()
        time.sleep(1.5)
        continue
    #Ver tareas
    elif opcion == "3":
        ver_tareas()
        time.sleep(1.5)
        continue
    #Marcar como completada
    elif opcion == "4":
        tareas_completadas()
        time.sleep(1.5)
        continue
    elif opcion == "5":
        restaurar_tareas()
        time.sleep(1.5)
        continue
    #Salir
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    #Error
    else:
        print("Opcion no valida, intenta de nuevo")
        continue