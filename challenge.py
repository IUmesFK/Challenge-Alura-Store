import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 9})

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

calcularPromedio = lambda iter, columna: round(sum(iter[columna]) / len(iter[columna]), 2)

tiendas = [tienda, tienda2, tienda3, tienda4]
nombresTiendas = ["Primer tienda", "Segunda tienda", "Tercer tienda", "Cuarta tienda"]

ingresos = []
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8a5043']

# Ingreso total por cada tienda

for idTienda, nombre in zip(tiendas, nombresTiendas):
    ingresoTienda = sum(idTienda["Precio"])
    print(f"\nEl ingreso total de la {nombre} es de {ingresoTienda}\n")
    ingresos.append(ingresoTienda)

barras = plt.bar(nombresTiendas, ingresos, color=colores)

# La siguiente iteración sirve para colocar un texto sobre cada barra indicando el total generado por cada tienda
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, yval, f"${yval:,.0f}", ha='center', va='bottom', fontsize=10)

plt.title("Ingresos totales por tienda")
plt.xlabel("Tienda")
plt.ylabel("Ingresos ($)")
plt.tight_layout()
plt.show()

# # Ventas por categoria


# # print(f"Ventas por categoria de la primer tienda: \n{tienda["Categoría del Producto"].value_counts()}\n")
# # print(f"Ventas por categoria de la segunda tienda: \n{tienda2["Categoría del Producto"].value_counts()}\n")
# # print(f"Ventas por categoria de la tercer tienda: \n{tienda3["Categoría del Producto"].value_counts()}\n")
# # print(f"Ventas por categoria de la cuarta tienda: \n{tienda4["Categoría del Producto"].value_counts()}\n")


for idTienda, nombre in zip(tiendas, nombresTiendas):
    conteoPorCategoria = idTienda.groupby("Categoría del Producto").size().sort_values(ascending=False)
    print(f"\nVentas por categoria de la {nombre}\n")
    print(f"\n{conteoPorCategoria}\n")
    plt.pie(conteoPorCategoria, labels=conteoPorCategoria.index, autopct="% 0.1f %%")
    plt.title(f"Ventas por categoria: {nombre}")
    plt.tight_layout()
    plt.show()


# # valoraciones de las tiendas


# # calificacionPrimerTienda = calcularPromedio(tienda, "Calificación")
# # calificacionSegundaTienda = calcularPromedio(tienda2, "Calificación")
# # calificacionTercerTienda = calcularPromedio(tienda3, "Calificación")
# # calificacionCuartaTienda = calcularPromedio(tienda4, "Calificación")

# # print(f"La calificación media de la primer tienda es de {round(calificacionPrimerTienda, 2)}")
# # print(f"La calificación media de la segunda tienda es de {round(calificacionSegundaTienda, 2)}")
# # print(f"La calificación media de la tercer tienda es de {round(calificacionTercerTienda, 2)}")
# # print(f"La calificación media de la cuarta tienda es de {round(calificacionCuartaTienda, 2)}")

calificaciones = []

for idTienda, nombre in zip(tiendas, nombresTiendas):
    calificacion = calcularPromedio(idTienda, "Calificación")
    print(f"La calificación media de la {nombre} es de {calificacion}")
    calificaciones.append(calificacion)



for idTienda, nombre in zip(tiendas, nombresTiendas):
    # debido a que los datos cargados en la columna "Fecha de Compra" se cargaron como strings, con el método .to_datetime() cambiamos el tipo de dato de string a un objeto datetime de pandas
    idTienda["Fecha de Compra"] = pd.to_datetime(idTienda["Fecha de Compra"], dayfirst=True)
    # ordenamos los valores
    idTienda = idTienda.sort_values("Fecha de Compra")
    # agrupamos por trimestres y calculamos el promedio
    calificacionesTrimestrales = idTienda.resample("QE", on="Fecha de Compra")["Calificación"].mean()
    plt.plot(calificacionesTrimestrales.index, calificacionesTrimestrales, label=nombre)

plt.title("Calificación promedio por trimestre")
plt.xlabel("Trimestre")
plt.ylabel("Calificación promedio")
plt.legend()
plt.tight_layout()
plt.show()


# #print(calificaciones)


# # Productos mas y menos vendidos:

# por cantidad

for idTienda, nombre in  zip(tiendas, nombresTiendas):
    conteoProductos = idTienda.groupby("Producto").size().sort_values(ascending=False)
    masVentas = conteoProductos.head(5) # toma los 5 productos mas vendidos
    menosVentas = conteoProductos.tail(5) # toma los 5 productos menos vendidos
    print(f"\n\n{conteoProductos}\n\n")
    print(f"\nLos 5 productos mas vendidos de la {nombre} son: {masVentas} \n\n ")
    print(f"\nLos 5 productos menos vendidos de la {nombre} son: {menosVentas} \n\n ")
    plt.figure(figsize=[12, 5])
    plt.bar(masVentas.index, masVentas.values, color=colores)
    plt.title(f"Productos mas vendidos: {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Unidades vendidas")
    plt.show()

    plt.figure(figsize=[10, 5])
    plt.bar(menosVentas.index, menosVentas.values, color=colores)
    plt.title(f"Productos menos vendidos: {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Unidades vendidas")
    plt.show()

# por valor en ventas

for idTienda, nombre in zip(tiendas, nombresTiendas):
    # se agrupa por producto y suma los valores de la columna precio para cada producto
    conteoPorVentas = idTienda.groupby("Producto")["Precio"].sum().sort_values(ascending=False)
    masRentables = conteoPorVentas.head(10) # toma los 10 productos mas vendidos
    menosRentables = conteoPorVentas.tail(10)# toma los 10 productos menos vendidos
    print(f"\nProductos mas vendidos segun valor en ventas: {masRentables}\n")
    print(f"\nProductos menos vendidos según valor en ventas: {menosRentables}\n")
    plt.figure(figsize=[12.0, 5.0])
    plt.barh(masRentables.index, masRentables.values)
    plt.title(f"Productos mas rentables: {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Ventas ($)")
    plt.show()

    plt.figure(figsize=[15.0, 5.0])
    plt.barh(menosRentables.index, menosRentables.values)
    plt.title(f"Productos menos rentables: {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Ventas ($)")
    plt.show()


# for idTienda, nombre in zip([tienda, tienda2, tienda3, tienda4], ["primer tienda", "segunda tienda", "tercer tienda", "cuarta tienda"]):
#     print(f"Productos vendidos de la {nombre}: \n{idTienda["Producto"].value_counts()}\n")



# # envio promedio por tienda

promediosDeEnvios = []

for idTienda, nombre in  zip(tiendas, nombresTiendas):
    promedio = calcularPromedio(idTienda, "Costo de envío")
    print(f"En promedio, el total gastado en envios en la {nombre} fue de {promedio}")
    promediosDeEnvios.append(promedio)

plt.bar(nombresTiendas, promediosDeEnvios)
plt.title("Gastos promedios en envios")
plt.xlabel("Tienda")
plt.ylabel("Gastos ($)")
plt.show()
    
#print(promediosDeEnvios)



# # envioPromedio_tienda1 = calcularPromedio(tienda, "Costo de envío")
# # envioPromedio_tienda2 = calcularPromedio(tienda2, "Costo de envío")
# # envioPromedio_tienda3 = calcularPromedio(tienda3, "Costo de envío")
# # envioPromedio_tienda4 = calcularPromedio(tienda4, "Costo de envío")

# # print(f"En promedio, el total gastado en envios en la primer tienda fue de {round(envioPromedio_tienda1, 2)}")
# # print(f"En promedio, el total gastado en envios en la segunda tienda fue de {round(envioPromedio_tienda2, 2)}")
# # print(f"En promedio, el total gastado en envios en la tercer tienda fue de {round(envioPromedio_tienda3, 2)}")
# # print(f"En promedio, el total gastado en envios en la cuarta tienda fue de {round(envioPromedio_tienda4, 2)}")



# # fechas


for idTienda, nombre in zip(tiendas, nombresTiendas):
    idTienda["Fecha de Compra"] = pd.to_datetime(idTienda["Fecha de Compra"], dayfirst=True)
    tiendaOrdenada = idTienda.sort_values("Fecha de Compra")
    print(tiendaOrdenada[["Fecha de Compra", "Producto", "Precio"]].head())