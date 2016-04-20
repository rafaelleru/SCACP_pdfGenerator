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

#Obtener lista con preguntas

patron_pregunta = re.compile('<strong class="tituloGift">[\w|\W]+?</strong>')
patron_respuesta = re.compile('<strong>[\w|\W]+?</strong>')

contenido = contenido.splitlines()

lista_respuestas = []
lista_preguntas = []

for l in contenido:
    #Buscamos las preguntas
    matcher = patron_pregunta.findall(l)
    if matcher:
        for m in matcher:
            lista_preguntas.append(m)
    #Buscamos las respuestas
    matcher = patron_respuesta.findall(l)
    if matcher:
        for m in matcher:
            lista_respuestas.append(m)

archivo.close()
print("Archivo cerrado")
