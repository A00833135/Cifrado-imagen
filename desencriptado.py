from cryptography.fernet import Fernet

# Leer la clave desde el archivo
with open('clave.key', 'rb') as archivo_clave:
    clave = archivo_clave.read()

# Crear un objeto Fernet con la clave
fernet = Fernet(clave)

# Leer los datos encriptados de la imagen
with open('imagen_encriptada.jpg', 'rb') as archivo_encriptado:
    datos_encriptados = archivo_encriptado.read()

# Desencriptar los datos de la imagen
datos_desencriptados = fernet.decrypt(datos_encriptados)

# Escribir los datos desencriptados en un nuevo archivo de imagen
with open('imagen_desencriptada.jpg', 'wb') as archivo_desencriptado:
    archivo_desencriptado.write(datos_desencriptados)
