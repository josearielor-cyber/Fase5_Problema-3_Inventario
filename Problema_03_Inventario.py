# Universidad Nacional Abierta y a Distancia (UNAD)
# Curso: Fundamentos de programacion
# Fase 5: Evaluacion Final POA
# Problema 3: Control de Inventario y Reabastecimiento
# Estudiante : Jose Ariel Ortiz Rojas

# Matriz de datos de los articulos
inventario = [
    [101, "cable electrico", 10, 20],
    [102, "Interruptor", 15, 10],
    [103, " Tomacorriente", 5, 12],
    [104, "Bombillo LED", 30, 25],
    [105, "Breaker", 4, 10]
]
# Funcion para calcular la cantidad que se debe solicitar
def calcular_cantidad(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad


# Recorrer la matriz y analizar cada articulo 
print("CONTROL DE INVENTARIO Y REABASTECIMIENTO")
print("----------------------------------------")

i = 0

while i < len(inventario):
    codigo = inventario[i][0]
    nombre = inventario[i][1]
    stock_actual = inventario[i][2]
    stock_minimo = inventario[i][3]

    cantidad =calcular_cantidad(stock_actual, stock_minimo)

    print("codigo:", codigo)
    print("Articulo:", nombre)
    print("stock actual:", stock_actual)
    print("stock minimo:", stock_minimo)
    print("cantidad a solicitar:", cantidad)
    print("-----------------------------------------")


    i = i + 1

