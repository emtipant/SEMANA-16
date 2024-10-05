# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt y escribir en él
with open("my_notes.txt", "w") as file:  # Abrir el archivo en modo de escritura
    file.write("Espero visitar a mi tia Maria por sus cumpleaños.\n")  # Escribir la primera línea
    file.write("¿Que regalo le regalare?.\n")  # Escribir la segunda línea
    file.write("Abrigo, Pantalon, Chocolate.\n")  # Escribir la segunda línea
    file.write("Espero le guste los chocolates.\n")  # Escribir la tercera línea

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt para leer su contenido
with open("my_notes.txt", "r") as file:  # Abrir el archivo en modo de lectura
    # Leer el contenido línea por línea
    for line in file:  # Iterar sobre cada línea en el archivo
        print(line.strip())  # Mostrar cada línea leída, eliminando espacios en blanco

# El archivo se cierra automáticamente al salir del bloque with