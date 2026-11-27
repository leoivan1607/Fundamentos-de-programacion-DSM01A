#ESTA FUNCION RECIBIRA LAS LECTURAS Y LAS RESTARÁ PARA CALCULAR EL CONSUMO DEL MES
def calcular_consumo(lectura_anterior, lectura_actual):
  consumo = lectura_actual - lectura_anterior
  return consumo

#ESTA FUNCION CALCULARÁ EL TOTAL A PAGAR EN BASE AL CONSUMO Y EL PRECIO FIJADO
def importe(consumo):
  tarifa = 2.50
  cuota_fija = 40
  importe = consumo * tarifa + cuota_fija
  return importe

#ESTA FUNCION DEFINIRA EL RANGO DEL CONSUMO
def clasificacion(consumo):
  if consumo <= 100:
    clasificacion = "Baja"
  elif consumo > 100 and consumo < 150:
    clasificacion = "Media"
  else:
    clasificacion = "Alta"
  return clasificacion

#ESTA FUNCION IMPRIMIRÁ EL RECIBO, RECIBIRÁ DE DATOS LAS LECTURAS, EL TOTAL A PAGAR, EL CONSUMO Y SU CLASIFICACION
def mostrar_recibo(lectura_anterior,lectura_actual,consumo,importe,clasificacion):
  print("----- RECIBO DE ELECTRICIDAD -----")
  print("Lectura anterior : " + "%.2f" % lectura_anterior + " kWh")
  print("Lectura actual   : " + "%.2f" % lectura_actual + " kWh")
  print("Consumo total    : " + "%.2f" % consumo + " kWh")
  print("Nivel de consumo : " + clasificacion_consumo)
  print("Importe a pagar  : $" + "%.2f" % importe_a_pagar)
  print("------------------------------")

lectura_anterior = float(input("Ingrese la lectura anterior en kWh: "))
lectura_actual = float(input("Ingrese la lectura actual en kWh: "))

#ESTE BUCLE EVITARÁ CONSUMOS NEGATIVOS
while lectura_actual < lectura_anterior:
  print("La lectura actual debe ser mayor que la lectura anterior.")
  lectura_actual = float(input("Ingrese la lectura actual en kWh: "))

consumo = calcular_consumo(lectura_anterior, lectura_actual)

importe_a_pagar = importe(consumo)
clasificacion_consumo = clasificacion(consumo)

consumo = calcular_consumo(lectura_anterior, lectura_actual)

calcular_consumo(lectura_anterior,lectura_actual)
importe(consumo)
clasificacion(consumo)
mostrar_recibo(lectura_anterior,lectura_actual,consumo,importe_a_pagar,clasificacion_consumo)