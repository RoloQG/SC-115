horasLaboradas = float(input("Ingrese las Horas Semanales trabajadas:"))
costoHora = float(input("Ingrese el precio pagado por hora:"))

mes = 4.2
salarioSemanal = horasLaboradas * costoHora
salarioMensual = salarioSemanal * mes
cargasSociales = salarioMensual * 10.5 / 100
asociacionSolidarista = salarioMensual * 5 / 100
salarioNeto = salarioMensual - cargasSociales - asociacionSolidarista

print("El Salario Semanal es de:"+str(salarioSemanal))
print("El Salario Mensual es de:"+str(salarioMensual))
print("Su rebajo de Cargas Sociales es de:"+str(cargasSociales))
print("Su rebajo de Asociación Solidarista es de:"+str(asociacionSolidarista))
print("El Salario Neto es de:"+str(salarioNeto))


