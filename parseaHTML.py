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
    archivo.readline()
