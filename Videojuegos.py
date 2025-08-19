#GameStore tiene venta de videojuegos los nuevos tienen un costo de 1,000 y los usados 350.
# Escribe un programa que sirva para calcular el total de la compra.
#Entrada Dos números enteros, uno en cada renglón, el primero es la cantidad de juegos nuevos y el segundo la cantidad de juegos usados.
#Proceso
#Salida el total de la compra 

juegosNuevos = int(input("Cantidad de juegos nuevos:"))
juegosUsados = int(input("Cantidad de juegos usados:"))

totalCompra = (juegosNuevos * 1000) + (juegosUsados * 350)

print("El total de la compra es:", totalCompra)