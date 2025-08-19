print("Bajada de peso")
#Entrada PesoIn, PesoFn, meses
#Proceso (PesoIn-Pesofn)/meses
#Salida PesoPorMes

#Entrada
pesoIn=float(input("Indique cual es su peso actual: "))
pesoFn=float(input("Indique cual es el peso al que aspira llegar: "))
meses=int(input("Indique en cuantos meses desea llegar a ese peso: "))
#Proceso
PesoPorMes=(pesoIn-pesoFn)/meses
#Salida
print(f"Usted deberia bajar {PesoPorMes:.2f} por mes")