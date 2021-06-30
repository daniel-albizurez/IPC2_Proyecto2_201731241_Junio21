from re import T
import xml.dom.minidom
import xml.etree.ElementTree as ET

from . import objects

def writeFromCsv(clientes, mejores, masVendidos, juegos):
    root = ET.Element('chet')
    nodoClientes = ET.SubElement(root, 'clientes')
    for x in clientes:
        nodoCliente = ET.SubElement(nodoClientes, 'cliente')
        
        nodoNombre = ET.SubElement(nodoCliente, 'nombre')
        nodoNombre.text=x.nombre
        nodoApellido = ET.SubElement(nodoCliente, 'apellido')
        nodoApellido.text = x.apellido
        nodoEdad = ET.SubElement(nodoCliente, 'edad')
        nodoEdad.text = x.edad
        nodoNacimiento = ET.SubElement(nodoCliente, 'fechaCumple')
        nodoNacimiento.text=x.nacimiento
        nodoPrimera = ET.SubElement(nodoCliente, 'primeraCompra')
        nodoPrimera.text=x.primera
    
    nodoMejores =  ET.SubElement(root, 'mejoresClientes')
    for x in mejores:
        nodoMejor = ET.SubElement(nodoMejores, 'mejorCliente')

        nodoNombre = ET.SubElement(nodoMejor, 'nombre')
        nodoNombre.text = x.nombre
        nodoUltima = ET.SubElement(nodoMejor, 'fechaUltimaCompra')
        nodoUltima.text = x.ultimaCompra
        nodoCantida = ET.SubElement(nodoMejor, 'cantidadComprada')
        nodoCantida.text = x.cantidad
        nodoGasto = ET.SubElement(nodoMejor, 'cantidadGastada')
        nodoGasto.text = x.gasto
    
    nodoJuegos = ET.SubElement(root, 'juegos')
    for x in juegos:
        nodoJuego = ET.SubElement(nodoJuegos, 'juego')

        nodoNombre = ET.SubElement(nodoJuego, 'nombre')
        nodoNombre.text = x.nombre
        nodoPlataforma = ET.SubElement(nodoJuego, 'plataforma')
        nodoPlataforma.text = x.plataforma
        nodoLanzamiento = ET.SubElement(nodoJuego, 'lanzamiento')
        nodoLanzamiento.text = x.lanzamiento
        nodoClasificacion = ET.SubElement(nodoJuego, 'clasificacion')
        nodoClasificacion.text = x.clasificacion
        nodoStock = ET.SubElement(nodoJuego, 'stock')
        nodoStock.text = x.stock
    
    nodoMasVendidos = ET.SubElement(root, 'juegosMasVendidos')
    for x in masVendidos:
        nodoMas = ET.SubElement(nodoMasVendidos, 'juego')

        nodoNombre = ET.SubElement(nodoMas, 'nombre')
        nodoNombre.text = x.nombre
        nodoUltima = ET.SubElement(nodoMas, 'fechaUltimaCompra')
        nodoUltima.text = x.ultimaCompra
        nodoCopias = ET.SubElement(nodoMas, 'copiasVendidas')
        nodoCopias.text = x.copiasVendidas
        nodoStock = ET.SubElement(nodoMas, 'stock')
        nodoStock.text = x.stock


    stringData = ET.tostring(root, encoding='utf-8', method='xml', xml_declaration=True)
    dom = xml.dom.minidom.parseString(stringData)
    stringData = dom.toprettyxml()
    
    """ file = open("datos.xml", 'w')
    file.write(stringData)
    file.close() """

    return stringData
