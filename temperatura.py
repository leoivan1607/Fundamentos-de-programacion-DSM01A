T = float(input("Ingresa la temperatura del agua en Celcius: "))
if T <= 0:
  print("Estado sólido")
elif T >= 100:
  print("Ebulliicion-gaseoso")
else:
  print("Estado líquido")