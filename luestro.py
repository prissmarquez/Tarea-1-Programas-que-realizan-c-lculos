#Lustros
#Realiza un programa que indique el número de lustros que ha vivido una persona por medio de su año de nacimiento y el año actual.
#Entrada Dos números enteros. Primero el año de nacimiento y luego, el año actual. Uno en cada línea.
#Proceso
#Salida Un número con punto decimal que representa los lustros vividos por la persona. Solo el número. No poner ningún mensaje.

añoNacimiento = int(input ("Ingresa tu año de nacimiento:"))
añoActual = int(input("Ingresa el año actual"))

lustrosVividos = (añoActual - añoNacimiento) / 5

print(lustrosVividos)