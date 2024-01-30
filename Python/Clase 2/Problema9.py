ingresosMensuales = float(input("Ingrese sus Ingresos Mensuales:"))
gastosAlimentacion = float(input("Ingrese sus Gastos Mensuales por Alimentación:"))

porcentajeAlimentacion = gastosAlimentacion * 100 / ingresosMensuales
porcentajeLibre = 100 - porcentajeAlimentacion 

print("En Gastos por Alimentación usted gasto un:"+str(porcentajeAlimentacion),"%.")
print("Su porcentaje disponible es de:"+str(porcentajeLibre),"%")
