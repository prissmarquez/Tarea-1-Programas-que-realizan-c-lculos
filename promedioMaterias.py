#Promedio de 4 materias
# En una universidad cada estudiante cursa 4 materias en el semestre. 
# Desarrolla un programa que reciba la calificación de cada materia, calcula el promedio de las 4 materias y lo despliega.
#Entrada 4 números enteros
#Proceso sumar todos los numero y dividrlo entre 4 
#Sañida el promedio

calificacion1 = int(input("Ingresa la calificación de la materia 1:"))
calificacion2 = int(input("Ingresa la calificación de la materia 2:"))
calificacion3 = int(input("Ingresa la calificación de la materia 3:"))
calificacion4 = int(input("Ingresa la calificación de la materia 4:"))

promedio = calificacion1 + calificacion2 + calificacion3 + calificacion4 / 4

print(f"Tu promedio es: {promedio:.2f}")
#f es para formatear el texto, es decir lleva formato y incrustas la variable y 
#esta debe de ir pegada al paratensis 

