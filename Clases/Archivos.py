# En python existen los siguientes modos de lectura y escritur de archivos:
# 'r': Modo de lectura (read) Abre un archivo para leerlo. El archivo debe existtir , si no existe el porgrama nos marcara un error.
# 'w': Modo de escritura (write) Abre un para escribir en el. Si el archivo ya existe , se sobreescribe. Si no existe , se crea uno nuevo.
# 'a': Modo de anexado (append) Abre un archivo para anexar datos al final del mismo. Si el archivo no existe , se crea uno nuevo.
# 'r+': Modo de lectura y escritura (read and write) Abre un archivo para leer y escribir en el. El archivo debe existir , si no existe el porgrama nos marcara un error.
# 'w+': Modo de escritura y lectura (write and read) Abre un archivo para escribir y leer en el. Si el archivo ya existe , se sobreescribe. Si no existe , se crea uno nuevo.
# 'a+': Modo de anexado y lectura (append and read) Abre un archivo para anexar datos al final del mismo y leerlo. Si el archivo no existe , se crea uno nuevo.

#Apertura de archivo
# open("ruta/archivo.txt", modo)

#Cerrar archivo
# archivo.close()

#Podemos abrir el archivo haciendo uso de 'with' el cual cierra el archivo manera automatica al finalizar el bloque de codigo

#with open("ruta/archivo.txt", modo) as archivo:
                 # Operaciones con el archivo

with open("archivo.txt", "r") as f::
    contenido = f.read()
print(contenido)

with open("archi.txt", "r") as f:
    for lineas in f:
        print(lineas.strip())

with open("archivo2.txt", "w") as f:
    f.write("Esta es una nueva linea escrita en el archivo.\n")
    f.write("Otra linea añadida al archivo.\n")

with open("archivo3.txt", "a") as f:
    f.write("Esta linea se ha añadido al final del archivo.\n")

with open("archivo.txt", "r+") as f:
    contenido = f.read()
    f.write("\nEsta linea se ha añadido al final del archivo usando r+.")

with open ("archivo2.txt", "w+") as f:
    f.write("Escribiendo en archivo2 usando w+.\n")
    f.seek(0)  # Mover el cursor al inicio del archivo
    contenido = f.read()
    print(contenido)

with open("archivo3.txt", "a+") as f:
    f.write("Añadiendo una linea usando a+.\n")
    f.seek(0)  # Mover el cursor al inicio del archivo
    contenido = f.read()
    print(contenido)