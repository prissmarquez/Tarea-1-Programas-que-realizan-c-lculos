#100 años
#Crea un programa que pregunte al usuario su edad y el año actual, como resultado le indicará el año en que cumplirá 100 años.
#Entrada La edad (entero positivo) de la persona y el año actual (entero positivo), en este orden.
#Proeceso 100 - edad + año
#Salida El año (entero positivo) en el que la persona cumplirá 100 años.


#edad, año = map(int, input("Ingresa tu edad y el año actual separados por un espacio: ").split())
#split es para divir las varibles en dos y las puedes ocupar cada una de forma diferente
#-----------IMPORTAMTE ------------#
#cuando quieras poner dos varibles en un mismo renglon y quieres que sean enteros debes de poner un map para converir ese entrada en una int

edad = int(input("Ingresa tu edad:"))
añoActual = int (input("Ingresa el año actual:"))
año100 = 100 - edad + añoActual

print(f"El año en el vas a cumplir 100 años es: {año100}")

