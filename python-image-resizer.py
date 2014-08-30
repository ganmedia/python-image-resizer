#coding=utf-8

"""
SCRIPT PARA REDIMENSIONAR IMAGENES DE UN DIRECTORIO 
SEGÚN EL TAMAÑO QUE LE ESPECIFIQUEMOS.
PARA QUE FUNCIONE DEBEMOS UBICAR ESTE ARCHIVO
EN EL MISMO DIRECTORIO DONDE ESTÁN LAS IMÁGENES
Y CORRERLO DESDE ALLÍ MISMO.
------- ENJOY! --------
"""
import PIL  # MODULO PARA PROCESAR IMAGENES
from PIL import Image
import os  # MODULO PARA HACER COSAS EN EL DIRECTORIO
import fnmatch  # MODULO PARA COMPARAR EXTENSIONES EN EL DIRECTORIO
import tarfile # MODULO PARA COMPRIMIR

current_dir = os.path.dirname(os.path.abspath(__file__)) # LEEMOS EL DIRECTORIO EN EL QUE ESTAMOS 
lista_archivos = fnmatch.filter(os.listdir(current_dir), '*') # CREAMOS UNA LISTA CON TODOS LOS ARCHIVOS DENTRO DEL DIRECTORIO
lista_archivos_nopy = lista_archivos[:] # CLONAMOS LA LISTA ORIGINAL PARA ITERAR SOBRE ELLA
no_py = ".py" # EXPECIFICAMOS NO INCLUIR LOS ARCHIVOS CON LA EXTENSIÓN .PY

# LOOP PARA ELIMINAR LOS ELEMENTOS QUE NO SEAN .JPG DE LA LISTA
for i in lista_archivos:
	if  no_py in i:
		lista_archivos_nopy.remove(i)

os.mkdir("peq") # CREAMOS EL DIRECTORIO DONDE VAMOS A PONER LAS IMAGENES PEQUEÑAS
os.chmod(current_dir + "/peq", 0777) # LE DAMOS PERMISO DE ESCRITURA
tamano = input("Tamaño: ") # PREGUNTAMOS EL TAMAÑO PARA LAS NUEVAS FOTOS 
comprimir = raw_input("¿Desea comprimir las fotos? (si/no): ").lower()

# COMENZAMOS EL LOOP PARA REDIMENSIONAR LAS IMAGENES
for x in lista_archivos_nopy: 
	img = Image.open(x)  # ABRIMOS LA IMAGEN PARA TRABAJAR SOBRE ELLA
	width = img.size[0] # CHEQUEAMOS EL ANCHO
	heigh = img.size[1] # CHEQUEAMOS EL ALTO
	if width > heigh: # SI EL ANCHO ES MAYOR QUE EL ALTO (FOTO HORIZONTAL), LO TOMAMOS COMO REFERENCIA
		basewidth = tamano 
		wpercent = (basewidth / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))
		img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
		img.save("peq/" + x.lower())  # SALVAMOS LA IMAGEN EN EL DIRECTORIO
		print x + " ---> OK!"  # IMPRIMIMOS UN . PARA QUE EL USUARIO NO SE DESESPERE Y QUE VEA EL PROCESO

	else: # SI EL ALTO ES MAYOR QUE EL ANCHO (FOTO VERTICAL) LO TOMAMOS COMO REFERENCIA
		baseheight = tamano
		hpercent = (baseheight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
		img.save("peq/" + x.lower()) # SALVAMOS LA IMAGEN EN EL DIRECTORIO y le ponemos el nombre en minuscula para evitar problemas con .JPG
		print x + " ---> OK!" # IMPRIMIMOS UN . PARA QUE EL USUARIO NO SE DESESPERE Y QUE VEA EL PROCESO

print ""

# COMPRIMIMOS LAS IMAGENES
if comprimir == "si" or comprimir == "s":
	os.chdir(current_dir + "/peq") # CAMBIAMOS AL DIRECTORIO DONDE ESTAN LAS PEQUEÑAS
	lista_archivos_comprimir = fnmatch.filter(os.listdir(os.getcwd()), '*')
	tar = tarfile.open("images.tar.gz", "w:gz")
	for name in lista_archivos_comprimir:
		tar.add(name)
	tar.close()
	os.chmod("images.tar.gz", 0777)
	print "Fotos comprimidas"


print "FIN" # TERMINAMOS EL PROCESO.
