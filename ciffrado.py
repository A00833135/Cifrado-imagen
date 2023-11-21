from cryptography.fernet import Fernet

# Generar una clave para el cifrado
clave = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
fernet = Fernet(clave)

# Leer la imagen que quieres encriptar
with open('download.jpg', 'rb') as archivo:
    datos_imagen = archivo.read()

# Encriptar los datos de la imagen
datos_encriptados = fernet.encrypt(datos_imagen)

# Escribir los datos encriptados en un archivo
with open('imagen_encriptada.jpg', 'wb') as archivo_encriptado:
    archivo_encriptado.write(datos_encriptados)

# Guardar la clave en un archivo para usarla en el proceso de desencriptación
with open('clave.key', 'wb') as archivo_clave:
    archivo_clave.write(clave)
