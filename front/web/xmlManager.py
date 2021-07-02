
from re import T
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

#
from . import graph
#
from . import objects

def clean(xmlStruct):
    return minidom.parseString(xmlStruct).toprettyxml()

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

    stringData = juegosRepetidos(juegosRepetidos(mejoresRepetidos(ET.tostring(root, encoding='utf-8', method='xml')), 'juegos'), 'juegosMasVendidos')
    dom = minidom.parseString(stringData)
    stringData = dom.toprettyxml()
    
    """ file = open("datos.xml", 'w')
    file.write(stringData)
    file.close() """
    return stringData

def checkStruct(struct):
    tree = ET.fromstring(struct)

def mejoresRepetidos(xml):
    tree = ET.fromstring(xml)
    conjunto = tree.find('mejoresClientes')
    for cliente in conjunto:
        nombre = cliente.find('nombre').text
        comprada = int(cliente.find('cantidadComprada').text)
        gastada = float(cliente.find('cantidadGastada').text) 
        for cliente2 in conjunto:
            if cliente2 != cliente:
                if cliente2.find('nombre').text == nombre:
                    comprada += int(cliente2.find('cantidadComprada').text)
                    gastada += float(cliente2.find('cantidadGastada').text)
                    conjunto.remove(cliente2)
        cliente.find('cantidadComprada').text = str(comprada)
        cliente.find('cantidadGastada').text = str(gastada) + '0'
    return ET.tostring(tree)

def juegosRepetidos(xml, tagPadre):
    tree = ET.fromstring(xml)
    conjunto = tree.find(tagPadre)
    print(tagPadre)
    for juego in conjunto:
        nombre = juego.find('nombre').text
        stock = int(juego.find('stock').text)
        if tagPadre == 'juegosMasVendidos':
            copias = int(juego.find('copiasVendidas').text) 
        for juego2 in conjunto:
            if juego2 != juego:
                if juego2.find('nombre').text == nombre:
                    stock += int(juego2.find('stock').text)
                    if tagPadre == 'juegosMasVendidos':
                        copias += int(juego2.find('copiasVendidas').text)
                    conjunto.remove(juego2)
        juego.find('stock').text = str(stock)
        if tagPadre == 'juegosMasVendidos':
            juego.find('copiasVendidas').text = str(copias)
    return ET.tostring(tree)

def masVendidos(xml):
    tree = ET.fromstring(xml)
    juegos = tree.find('juegos')
    juegosMasVendidos = tree.find('juegosMasVendidos')
    copias = list()
    #lanzamientos = list()
    nombres = list() 

    rootMasVendidos = ET.Element('juegosMasVendidos')
    
    for juego in juegosMasVendidos:
        nombre = juego.find('nombre').text
        copiasVendidas = juego.find('copiasVendidas').text
        """ copiasVendidas = juego.find('copiasVendidas').text
        nombres.append(nombre)
        copias.append(copiasVendidas)

        nodoJuego = ET.SubElement(rootMasVendidos, 'juego')
        nodoNombre = ET.SubElement(nodoJuego, 'nombre')
        nodoNombre.text = nombre
        nodoCopias = ET.SubElement(nodoJuego, 'copiasVendidas')
        nodoCopias.text = copiasVendidas"""
        for j in juegos:
            if j.find('nombre').text == nombre:
                nodoJuego = ET.SubElement(rootMasVendidos, 'juego')
                
                lanzamiento = j.find('lanzamiento').text
                nodoLanzamiento = ET.SubElement(nodoJuego, 'lanzamiento')
                nodoLanzamiento.text = lanzamiento
                #lanzamientos.append(lanzamiento)

                nodoCopias = ET.SubElement(nodoJuego, 'copiasVendidas')
                nodoCopias.text = copiasVendidas
                copias.append(copiasVendidas)

                nodoNombre = ET.SubElement(nodoJuego, 'nombre')
                nodoNombre.text = nombre
                nombres.append(nombre + ' ' + lanzamiento)


    xmlMasV = ET.tostring(rootMasVendidos,encoding='utf-8', method='xml')
    graph.pieGraph(copias, nombres, 'graficas/masVendidos')
    return clean(xmlMasV)

def mejoresClientes(xml):
    tree = ET.fromstring(xml)
    clientes = tree.find('mejoresClientes')
    gastos = list()
    nombres = list()

    rootMejores = ET.Element('mejoresClientes')

    for cliente in clientes:
        nombre = cliente.find('nombre').text
        cantidad = cliente.find('cantidadGastada').text
        nombres.append(nombre)
        gastos.append(cantidad)

        nodoCliente = ET.SubElement(rootMejores, 'cliente')
        nodoNombre = ET.SubElement(nodoCliente, 'nombre')
        nodoNombre.text = nombre
        nodoGastos = ET.SubElement(nodoCliente, 'cantidadGastada')
        nodoGastos.text = cantidad
    xmlMejores = ET.tostring(rootMejores)

    graph.barsGraph(gastos, nombres, 'graficas/mejoresClientes')
    return clean(xmlMejores)#[gastos, nombres]

def clasificacion(xml):
    tree = ET.fromstring(xml)
    juegos = tree.find('juegos')
    clasificaciones = {}
    for juego in juegos:
        clasificacion = juego.find('clasificacion').text
        if clasificacion in clasificaciones:
            clasificaciones[clasificacion] += 1
        else:
            clasificaciones.update({clasificacion:1})
    for clasificacion in clasificaciones.keys():
        rootClas = ET.Element('clasificaciones')
        nodoClas = ET.SubElement(rootClas, 'clasificacion')
        nodoClas.text = clasificacion
        nodoCant = ET.SubElement(rootClas, 'stock')
        nodoCant.text = str(clasificaciones.get(clasificacion))
    
    xmlClas = ET.tostring(rootClas)
    """ plt.pie(clasificaciones.values(), labels=clasificaciones.keys(), labeldistance=1.15)
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('front/web/static/graficas/calsificacion') """
    graph.donutGraph(clasificaciones.values(), clasificaciones.keys(), 'graficas/clasificacion')
    return clean(xmlClas) #clasificaciones
    
def cumple(xml):
    tree = ET.fromstring(xml)
    clientes = tree.find('clientes')
    listado = {}

    rootCumple = ET.Element('cumple')

    for cliente in clientes:
        nombre = cliente.find('nombre').text
        cumple = cliente.find('fechaCumple').text
        listado.update({nombre:cumple})

        nodoCliente = ET.SubElement(rootCumple, 'cliente')
        nodoNombre = ET.SubElement(nodoCliente, 'nombre')
        nodoNombre.text = nombre
        nodoFecha = ET.SubElement(nodoCliente, 'fecha')
        nodoFecha.text = cumple
    xmlCumple = ET.tostring(rootCumple)
    #listado = dict(sorted(listado.items(), key=lambda item : datetime.strptime(item[1], '%d/%m/%Y').month))
    #print(listado.keys())
    #print(listado.values())
    return [clean(xmlCumple), listado] #listado

def juegos(xml):
    tree = ET.fromstring(xml)
    juegos = tree.find('juegos')
    listado = {}
    
    rootJuegos = ET.Element('juegos')

    for juego in juegos:
        nombre = juego.find('nombre').text
        stock = juego.find('stock').text
        listado.update({nombre:stock})

        nodoJuego = ET.SubElement(rootJuegos, 'juego')
        nodoNombre = ET.SubElement(nodoJuego, 'nombre')
        nodoNombre.text = nombre
        nodoStock = ET.SubElement(nodoJuego, 'stock')
        nodoStock.text = stock

    xmlJuegos = ET.tostring(rootJuegos)
    
    return [clean(xmlJuegos), listado]   