#Intercambio de edades

edadLuis = int(input("Ingrese la edad de Luis:"))
edadPedro = int(input("Ingrese la edad de Pedro:"))

edadPivote = edadLuis

edadLuis=edadPedro
edadPedro=edadPivote

print("La edad de Luis es:",edadLuis)
print("La edad de Pedro es:",edadPedro)
