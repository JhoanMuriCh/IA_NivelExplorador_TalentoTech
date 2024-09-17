Salario, HorasExtras, Bonificacion = input().split()
Salario = float(Salario)
HorasExtras = int(HorasExtras)
Bonificacion = int(Bonificacion)
valor_hora = Salario / 192
valor_hora_extra = valor_hora * 1.25
valor_bonificacion = Salario * 0.05
salarioNeto = Salario + (HorasExtras * valor_hora_extra) + (Bonificacion * valor_bonificacion)
descuento = (salarioNeto * 0.035) +  (salarioNeto * 0.04) + (salarioNeto * 0.01)
salarioTotal = salarioNeto - descuento
print(round(salarioTotal,1))
