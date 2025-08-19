#Haz un programa sirva para calcular el precio que va a pagar un cliente por comprar cemento.
# El programa debe leer la cantidad de bultos de cemento que va a comprar el cliente, y el precio del bulto de cemento.
# El programa debe mostrar como salida 3 datos uno en cada renglón: el precio antes de impuestos, los impuestos (que son el 16% del precio) y el total a pagar por el cliente.

#Entrada La cantidad de bultos de cemento y El precio por bulto de cemento
#Proceso 
#Salida El precio antes de impuestos, Los impuestos, El total a pagar

bultosCementos = int(input("Cantidad de bultos de cemento:"))
precioBulto = float(input("Precio por bulto de cemento:"))

precioSinImpuestos = bultosCementos * precioBulto
impuestos = precioSinImpuestos * 0.16
totalAPagar = precioSinImpuestos + impuestos

print("Precio antes de impuestos:", precioSinImpuestos)
print("Impuestos (16%):", impuestos)
print("Total a pagar:", totalAPagar)