
def ejecutar_cotizador():
    print("[Iniciando Cotizador de productos...]")
    nombre1 = input("ingrese el nombre del producto 1: ")
    cantidad1 = int(input("ingrese la cantidad del producto 1: "))
    precio1 = float(input("ingrese el precio del producto 1: "))

    nombre2 = input("ingrese el nombre del producto 2: ")
    cantidad2 = int(input("ingrese la cantidad del producto 2: "))
    precio2 = float(input("ingrese el precio del producto 2: "))

    nombre3 = input("ingrese el nombre del producto 3: ")
    cantidad3 = int(input("ingrese la cantidad del producto 3: "))
    precio3 = float(input("ingrese el precio del producto 3: "))

    subtototal1 = cantidad1 * precio1
    subttotal2 = cantidad2 * precio2
    subttotal3 = cantidad3 * precio3

    subtotal = subtototal1 + subttotal2 + subttotal3

    iva = subtotal * 0.16

    total = subtotal + iva

    print("---FACTURA---")
    print(cantidad1, nombre1, "de $", precio1)
    print(cantidad2, nombre2, "de $", precio2)
    print(cantidad3, nombre3, "de $", precio3)
    print("el subtotal es $", subtotal)
    print("el iva es $", iva)
    print("el total es $", total)


def ejecutar_tarifas_museo():
    print("[Iniciando Sistema de tarifas de museo...]")

    precio_menor_12 = 40
    doce_a_59 = 100
    precio_60 = 60
    descuento = 0.25
    edad = int(input("Ingrese la edad del visitante: "))
    while edad < 0:
        print("La edad no puede ser negativa")
        edad = int(input("Ingrese la edad del visitante: "))
    estudiante = input("Es estudiante? (si/no): ")
    if estudiante == "si" and edad >= 12 and edad <= 59:
        desc_estudiante = doce_a_59 * descuento
        precio_final = doce_a_59 - desc_estudiante
        print("edad:", edad, "estudiante:", estudiante, "precio final:$", precio_final)
    elif estudiante == "no" and edad >= 12 and edad <= 59:
        print("edad:", edad, "estudiante:", estudiante, "precio final:$", doce_a_59)
    elif edad < 12:
        print("edad:", edad, "estudiante:", estudiante, "precio final:$", precio_menor_12)
    else:
        print("edad:", edad, "estudiante:", estudiante, "precio final:$", precio_60)


def ejecutar_registro_ventas():
    print("[Iniciando Registro diario de ventas...]")
    total = 0
    venta = float(input("ingrese el valor de la venta: "))
    cantidad = 0
    mil_o_mas = "no"
    promedio = 0


    while venta != 0:
        total = total + venta
        venta = float(input("ingrese el valor de la venta: "))
        if venta < 0:
            print("ingrese un valor de venta válido")
        else:
            cantidad = cantidad + 1
            total = total + venta

        if venta >= 1000:
          mil_o_mas = "si"

    promedio = total / cantidad

    if venta == 0:
        print("Cantidad de ventas:", cantidad)
        print("el promedio de las ventas es:$", promedio)
        print("total vendido:$", total)
        print("hubo venta de $1000 o mas?: ", mil_o_mas)


def ejecutar_calculadora_electrica():
    print("[Iniciando Calculadora de consumo eléctrico...]")

    # ESTA FUNCION RECIBIRA LAS LECTURAS Y LAS RESTARÁ PARA CALCULAR EL CONSUMO DEL MES
    def calcular_consumo(lectura_anterior, lectura_actual):
        consumo = lectura_actual - lectura_anterior
        return consumo

    # ESTA FUNCION CALCULARÁ EL TOTAL A PAGAR EN BASE AL CONSUMO Y EL PRECIO FIJADO
    def importe(consumo):
        tarifa = 2.50
        cuota_fija = 40
        importe = consumo * tarifa + cuota_fija
        return importe

    # ESTA FUNCION DEFINIRA EL RANGO DEL CONSUMO
    def clasificacion(consumo):
        if consumo <= 100:
            clasificacion = "Baja"
        elif consumo > 100 and consumo < 150:
            clasificacion = "Media"
        else:
            clasificacion = "Alta"
        return clasificacion

    # ESTA FUNCION IMPRIMIRÁ EL RECIBO, RECIBIRÁ DE DATOS LAS LECTURAS, EL TOTAL A PAGAR, EL CONSUMO Y SU CLASIFICACION
    def mostrar_recibo(lectura_anterior, lectura_actual, consumo, importe, clasificacion):
        print("----- RECIBO DE ELECTRICIDAD -----")
        print("Lectura anterior : " + "%.2f" % lectura_anterior + " kWh")
        print("Lectura actual   : " + "%.2f" % lectura_actual + " kWh")
        print("Consumo total    : " + "%.2f" % consumo + " kWh")
        print("Nivel de consumo : " + clasificacion)
        print("Importe a pagar  : $" + "%.2f" % importe)
        print("------------------------------")

    lectura_anterior = float(input("Ingrese la lectura anterior en kWh: "))
    lectura_actual = float(input("Ingrese la lectura actual en kWh: "))

    # ESTE BUCLE EVITARÁ CONSUMOS NEGATIVOS
    while lectura_actual < lectura_anterior:
        print("La lectura actual debe ser mayor que la lectura anterior.")
        lectura_actual = float(input("Ingrese la lectura actual en kWh: "))

    consumo = calcular_consumo(lectura_anterior, lectura_actual)
    importe_a_pagar = importe(consumo)
    clasificacion_consumo = clasificacion(consumo)

    mostrar_recibo(lectura_anterior, lectura_actual, consumo, importe_a_pagar, clasificacion_consumo)



# MENÚ PRINCIPAL INTERACTIVO

def mostrar_menu():
    print("-----------------------------------------")
    print("         SISTEMA MULTIFUNCIONAL          ")
    print("-----------------------------------------")
    print("1. Cotizador de productos")
    print("2. Sistema de tarifas de museo")
    print("3. Registro diario de ventas")
    print("4. Calculadora de consumo eléctrico")
    print("0. Salir")
    print("-----------------------------------------")


opcion = 5

while opcion != 0:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        ejecutar_cotizador()
    elif opcion == 2:
        ejecutar_tarifas_museo()
    elif opcion == 3:
        ejecutar_registro_ventas()
    elif opcion == 4:
        ejecutar_calculadora_electrica()
    elif opcion == 0:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")