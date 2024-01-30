distancia = float(input("Ingrese la distancia de su casa a la Universidad:"))
costo = float(input("Ingrese el costo por kilometro:"))
dias = float(input("Ingrese cuantos dias a la semana viaja a la Universidad:"))
cuatrimestre = dias*15
costoTotal = distancia*2*costo*cuatrimestre

print("El costo total por cuatrimestre es de:"+str(costoTotal))
