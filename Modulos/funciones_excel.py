import openpyxl

def crear_y_guardar_libro_excel(datos_a_escribir, ruta_archivo_salida):
    try:
        # Crear un nuevo libro de Excel y obtener la hoja activa
        libro_excel = openpyxl.Workbook()
        hoja = libro_excel.active
        
        # Escribir los encabezados de las columnas
        encabezados = ["NOMBRE PRODUCTO", "MARCA", "PRECIO PRODUCTO", "PRECIO PROMOCIONAL", "PRECIO X POR"]
        hoja.append(encabezados)
        
        # Agregar los datos a la hoja
        for fila in datos_a_escribir:
            hoja.append(fila)
        
        # Guardar el libro de Excel en la ruta especificada
        libro_excel.save(ruta_archivo_salida)
        print("Se creó el archivo Excel correctamente.")
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        return False