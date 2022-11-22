from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('key.key', 'rb').read()

def desencriptar(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as archivo:
            datos_encriptados = archivo.read()
        datos_desencriptados = f.decrypt(datos_encriptados)
        with open(item, 'wb') as archivo:
            archivo.write(datos_desencriptados)

if __name__ == '__main__':
    ruta_desencriptar = 'C:\\Users\\fedua\\OneDrive\\Documents\\Ransomware\\Prueba'    #Se pone la dirrecion en donde se encuentra el archivo
    os.remove(ruta_desencriptar+'\\'+'readme.txt')

    items = os.listdir(ruta_desencriptar)
    ruta_completa = [ruta_desencriptar+'\\'+item for item in items]

    key = cargar_key()
    desencriptar(ruta_completa, key)
