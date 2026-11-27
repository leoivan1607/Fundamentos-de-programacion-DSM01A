precio_menor_12 = 40
doce_a_59 = 100
precio_60 = 60
descuento = 0.25
edad = int(input("Ingrese la edad del visitante: "))
while edad < 0:
    print("La edad no puede ser negativa")
    edad = int(input("Ingrese la edad del visitante: "))
estudiante = input("Es estudiante? (si/no): ")
if estudiante == "si" and edad >=12 and edad <= 59:
    desc_estudiante = doce_a_59 * descuento
    precio_final = doce_a_59 - desc_estudiante
    print("edad:",edad,"estudiante:",estudiante,"precio final:$",precio_final)
elif estudiante == "no" and edad >=12 and edad <= 59:
    print("edad:",edad,"estudiante:",estudiante,"precio final:$",doce_a_59)
elif edad < 12:
  print("edad:",edad,"estudiante:",estudiante,"precio final:$",precio_menor_12)
else:
    print("edad:",edad,"estudiante:",estudiante,"precio final:$",precio_60)