'''
class Pregunta(object):
    """Pregunta del cuestionario"""
    enunciado
    respuestas[]
    correcta

    def __init__(self, enunciado, respuestas, correcta):
        super(Pregunta, self).__init__()
        self.enunciado = enunciado
        self.respuestas = respuestas
        self.correcta = correcta

def NuevaPregunta():

def leeHTML(archivo):
    a_descartar = archivo.readline()
    while a_descartar is not '<div class="cajaGift">'
        a_descartar = archivo.readline()

    linea = archivo.readline()
    #linea.repla
    if linea.startswith('<div class="respuestasGift">')
        #leer la linea entera || Ahora lo hare
        for j in range(0, 5):
            cadena = cadena + linea[j]
        if cadena is "&nbsp":
            #na
            break;
        elif cadena is "<stro":
            caracter = ""
            while caracter is not ">":
                a_descartar = linea.getchar()
            enunciado = ""
            while caracter is not "<":
                enunciado = enunciado + caracter
'''

import re, time

archivo = open('cuestionario.html')
contenido = archivo.read()

if contenido != None:
    print("Archivo abierto")

patron = re.compile('\<strong class\=\"tituloGift\"\>[0-9a-zA-Z ?¿]+\<\/strong\>')
contenido = contenido.splitlines()
#print(contenido)
for l in contenido:
    matcher = patron.search(l)
    if matcher:
        m = matcher.group(0)
    #print(l+"\n***********************************************************\n")


archivo.close()
print("Archivo cerrado")

print(matcher)
