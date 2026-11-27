total = 0
venta = float(input("ingrese el valor de la venta: "))
cantidad = 0
mil_o_mas = "no"
promedio = 0
if venta >= 1000:
  mil_o_mas = "si"

while venta != 0:
    total = total + venta
    venta = float(input("ingrese el valor de la venta: "))
    if venta < 0:
      print("ingrese un valor de venta válido")
    else:
      cantidad = (cantidad + 1)
      total = total + venta

    promedio = total / cantidad
    if venta >= 1000:
      mil_o_mas = "si"

if venta == 0:
  print("Cantidad de ventas:", cantidad,)
  print("el promedio de las ventas es:$",promedio,)
  print("total vendido:$",total,)
  print("hubo venta de $1000 o mas?: ",mil_o_mas)
