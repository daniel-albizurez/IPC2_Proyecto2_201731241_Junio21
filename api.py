from flask import Flask, request, Response
from flask_cors import CORS

import matplotlib.pyplot as plt
import numpy as np

from front.web import xmlManager as manager

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})

@app.route('/procesarXml', methods=['POST'])
def procesar():
    xml = request.form.get('mostrar_xml')
    string = str(xml)
    try:
        manager.checkStruct(xml)
    except:
         return {'error' : 'Se econtraron modificaciones erroneas en el xml por favor corregirlas'}
    datos = open('datos.xml', 'w')
    datos.write(string)
    datos.close()

    reportes = ""
    reportes += manager.masVendidos(xml)
    reportes += manager.mejoresClientes(xml)
    reportes += manager.clasificacion(xml)
    fechasNac = manager.cumple(xml)
    reportes += fechasNac[0]
    juegos = manager.juegos(xml)
    reportes += juegos[0]
    
    #reportes = manager.xmlFromString(reportes)

    respuesta = {
        'report' : reportes,
        'cumples' : fechasNac[1],
        'juegos' : juegos[1]
    }

    file = open('reportes.xml', 'w')
    file.write(reportes)
    file.close()

    return respuesta

@app.route('/revisar', methods=['POST'])
def revisar():
    return Response(status='204')

if __name__ == '__main__':
    app.run(debug=True)
