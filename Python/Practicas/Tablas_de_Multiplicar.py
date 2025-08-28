tabla = input("Ingrese la tabla de multiplicar que desea ver: ")
tabla = int(tabla)

for i in range(1, 11):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")