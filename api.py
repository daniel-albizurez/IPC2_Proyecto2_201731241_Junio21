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
    datos = open('datos.xml', 'w')
    datos.write(string)
    datos.close()

    reportes = ""
    reportes += manager.masVendidos(xml)
    reportes += manager.mejoresClientes(xml)
    reportes += manager.clasificacion(xml)
    reportes += manager.cumple(xml)
    reportes += manager.juegos(xml)

    #reportes = manager.xmlFromString(reportes)

    file = open('reportes.xml', 'w')
    file.write(reportes)
    file.close()

    return reportes

@app.route('/revisar', methods=['POST'])
def revisar():
    return Response(status='204')

if __name__ == '__main__':
    app.run(debug=True)
