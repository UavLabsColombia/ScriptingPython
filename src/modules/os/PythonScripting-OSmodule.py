# Importamos librerias del sistema operativo
from datetime import datetime
import os

# imprimimos las clases, objetos y demas variables disponibles de la clase os
print(dir(os))

# traemos del entorno la variable HOME
print('El home es:', os.environ.get('HOME'))

file_path = os.environ.get('HOME')+'/Proyectos/Python/prueba'
# Imprimimos el actual directorio en el SO
print (os.getcwd())

# ahora creamos un directorio
os.mkdir(file_path)


# Para navegar a un directorio
os.chdir(file_path)

# se vuelve a imprimir
print (os.getcwd())
# Se crea un archivo de nombre demo.txt
os.mknod('demo.txt')
# Se lista el contenido del directorio
print (os.listdir())

print(os.name)
print(os.ctermid())


# ahora creamos un directorio
os.mkdir('directorio1')
os.makedirs('directorio2/subdirdedir2')
# y los borramos
os.rmdir('directorio1')
# Este borra recursivamente hasta el ultimo
os.removedirs('directorio2/subdirdedir2')

# primero vemos la informacion del archivo
print(os.stat('demo.txt'))
print("El archivo pesa: ", os.stat('demo.txt').st_size, "bytes")
print("modificado el: ", os.stat('demo.txt').st_mtime, "en timestamp")
# ahora lo pasamos a una forma mas legible
print("no entiendes el timestap?, te lo humanidifico")
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
# vamos a renombrar un archivo

os.rename('demo.txt', 'test.txt')
# y lo dejamos como estaba :D
os.rename('test.txt', 'demo.txt')

for dirpath, dirnames, filenames in os.walk('/home/heberth/Proyectos/Python/'):
    print('path actual:', dirpath)
    print('directorios', dirnames)
    print('archivos', filenames)
    print()


def metodo():
    return 1

print(metodo())
for i in range(1, 100):
    print("lala")
    print(i)

file = file_path + '/demo.txt'
os.remove(file)
os.rmdir(file_path)
