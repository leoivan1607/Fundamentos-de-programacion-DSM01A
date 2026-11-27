nombre1 = (input("ingrese el nombre del producto 1: "))
cantidad1 = int(input("ingrese la cantidad del producto 1: "))
precio1 = float(input("ingrese el precio del producto 1: "))

nombre2 = (input("ingrese el nombre del producto 2: "))
cantidad2 = int(input("ingrese la cantidad del producto 2: "))
precio2 = float(input("ingrese el precio del producto 2: "))

nombre3 = (input("ingrese el nombre del producto 3: "))
cantidad3 = int(input("ingrese la cantidad del producto 3: "))
precio3 = float(input("ingrese el precio del producto 3: "))

subtototal1 = cantidad1 * precio1
subttotal2 = cantidad2 * precio2
subttotal3 = cantidad3 * precio3

subtotal = subtototal1 + subttotal2 + subttotal3

iva = subtotal * 0.16

total = subtotal + iva

print("---FACTURA---")
print(cantidad1,nombre1,"de $", precio1)
print(cantidad2,nombre2,"de $", precio2)
print(cantidad3,nombre3,"de $", precio3)
print("el subtotal es $", subtotal)
print("el iva es $", iva)
print("el total es $", total)
