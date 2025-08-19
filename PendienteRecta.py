print("Calcular la pendiente de una recta")
#Entrada x1,y1,x2,y2,m
#Proceso (y2-y1)/(x2-x1)
#Salida m

#Entrada
x1=float(input("Indique el valor de x1: "))
y1=float(input("Indique el valor de y1: "))
x2=float(input("Indique el valor de x2: "))
y2=float(input("Indique el valor de y2: "))
#Proceso 
m=(y2-y1)/(x2-x1)
#Salida
print(f"La pendiente de su recta es: {m:.2f}")