import os
import shutil
from datetime import datetime

EXTENSIONES = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Programacion': ['.py', '.java', '.html', '.css', '.js']
}

def obtener_nombre_unico(ruta_destino, nombre_archivo):
    """
    Si el archivo existe en el destino, genera un nombre nuevo 
    agregando un contador (ej: archivo_1.jpg)
    """
    nombre, ext = os.path.splitext(nombre_archivo)
    contador = 1
    nuevo_nombre = nombre_archivo
    ruta_completa = os.path.join(ruta_destino, nuevo_nombre)
    
    while os.path.exists(ruta_completa):
        nuevo_nombre = f"{nombre}_{contador}{ext}"
        ruta_completa = os.path.join(ruta_destino, nuevo_nombre)
        contador += 1
        
    return nuevo_nombre

def organizar_profesional(ruta):
    if not os.path.exists(ruta):
        print("Ruta no válida.")
        return

    reporte = []

    for archivo in os.listdir(ruta):
        ruta_origen = os.path.join(ruta, archivo)
        
        if os.path.isfile(ruta_origen) and archivo != "reporte_limpieza.txt":
            ext = os.path.splitext(archivo)[1].lower()
            
            for categoria, lista_ext in EXTENSIONES.items():
                if ext in lista_ext:
                    carpeta_dest = os.path.join(ruta, categoria)
                    os.makedirs(carpeta_dest, exist_ok=True)
                    
                    # Usamos nuestra nueva función para evitar borrar archivos
                    nombre_final = obtener_nombre_unico(carpeta_dest, archivo)
                    ruta_destino = os.path.join(carpeta_dest, nombre_final)
                    
                    shutil.move(ruta_origen, ruta_destino)
                    reporte.append(f"Movido: {archivo} -> {categoria}/{nombre_final}")
                    break
    
    # Imprimir resumen
    if reporte:
        print(f"\n--- RESUMEN DE LIMPIEZA ---")
        for linea in reporte:
            print(linea)
    else:
        print("Nada que limpiar por aquí. ¡Todo está en orden!")

# --- PRUEBA TU CÓDIGO AQUÍ ---
ruta_test = r'C:\Users\veron\OneDrive\Desktop\prueva_0rden' 
organizar_profesional(ruta_test)