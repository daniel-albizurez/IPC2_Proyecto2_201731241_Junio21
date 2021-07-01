from typing import ContextManager
from django.shortcuts import render
import requests
import re
import csv
from . import objects
from . import xmlManager
# Create your views here.

api_dir = 'http://localhost:5000{}'

def index(request):
    return render(request, 'index.html')

def revisar(request):
    if request.method == 'POST':
        try:
            clientesFile = request.FILES['clientes']
            mejoresCFile = request.FILES['mejores_clientes']
            juegosFile = request.FILES['juegos']
            juegosMasFile = request.FILES['juegos_mas']
        except:
            context = {
                'error' : "Seleccione 4 archivos .csv"
            }
            return render(request, 'index.html', context)
        
        dataClientes = clientesFile.read().decode('utf-8').split('\n')
        reader = csv.DictReader(dataClientes, delimiter=';')
        line = 1
        clientes = list()
        try:
            for row in reader:
                nombre = row['Nombre']
                apellido = row['Apellido']
                edad = row['Edad']
                cumple = row['FechaNac']
                primera = row['FechaUltimaCompra']
                if validarCadena(patronNombre, nombre) and validarCadena(patronNombre, apellido) and validarCadena(patronEdad, edad) and validarCadena(patronFecha, cumple) and validarCadena(patronFecha, primera):
                    #print(row)
                    cliente = objects.Cliente(nombre, apellido, edad, cumple, primera)
                    clientes.append(cliente)
                    line +=1
                else:
                    context = {
                    'error' : "Por favor corrija el error en la información de los clientes; Linea " + str(line)
                    }
                    return render(request, 'index.html', context)
        except Exception as e: 
            context = {
                    'error' : "Por favor corrija los errores en los encabezados en el csv de clientes"
                    }
            print(str(e))
            return render(request, 'index.html', context)
        
        dataMejores = mejoresCFile.read().decode('utf-8').split('\n')
        reader = csv.DictReader(dataMejores, delimiter=';')
        line = 1
        mejores = list()
        try:
            for row in reader:
                nombre = row['Nombre']
                ultima = row['FechaUltimaCompra']
                cantidad = row['CantidadComprada']
                gasto = row['CantidadGastada']
                if re.search(gasto, patronCantidad):
                    gasto += '.00'
                if validarCadena(patronNombre, nombre) and validarCadena(patronFecha, ultima) and validarCadena(patronCantidad, cantidad) and validarMoneda(gasto):
                    mejor = objects.Mejor(nombre, ultima, cantidad, gasto)
                    mejores.append(mejor)
                    line += 1
                else:
                    context = {
                    'error' : "Por favor corrija el error en la información de mejores clientes; Linea " + str(line)
                    }
                    return render(request, 'index.html', context)
        except:
            context = {
                    'error' : "Por favor corrija los errores en los encabezados del csv de mejores clientes"
                    }
            return render(request, 'index.html', context)
        
        dataJuegos = juegosFile.read().decode('utf-8').split('\n')
        reader = csv.DictReader(dataJuegos, delimiter=';')
        line = 1
        juegos = list()
        try:
            for row in reader:
                nombre = row['Nombre']
                plataforma = row['Plataforma']
                lanzamiento = row['AñoLanzamiento']
                clasificacion = row['Clasificacion']
                stock = '1' if 'Stock' not in row else row['Stock']
                stock = '1' if not stock else stock
                if validarCadena(patronAnual, lanzamiento) and validarCadena(patronClasificacion, clasificacion):
                    juego = objects.Juego(nombre, plataforma, lanzamiento, clasificacion, stock)
                    juegos.append(juego)
                    line += 1
                else:
                    context = {
                    'error' : "Por favor corrija el error en la información de juegos; Linea " + str(line)
                    }
                    return render(request, 'index.html', context)
        except:
            context = {
                    'error' : "Por favor corrija los errores en los encabezados del csv de juegos"
                    }
            return render(request, 'index.html', context)

        dataMasVendidos = juegosMasFile.read().decode('utf-8').split('\n')
        reader = csv.DictReader(dataMasVendidos, delimiter=';')
        line = 1
        masVendidos = list()
        try:
            for row in reader:
                nombre = row['Nombre']
                ultima = row['FechaUltimaCompra']
                copias = row['CopiasVendidas']
                stock = row['Stock']
                if  validarCadena(patronFecha, ultima) and validarCadena(patronCantidad, copias) and validarCadena(patronCantidad, stock):
                    masVendido = objects.MasVendido(nombre, ultima, copias, stock)
                    masVendidos.append(masVendido)
                    line += 1
                else:
                    context = {
                    'error' : "Por favor corrija el error en la información de juegos mas vendidos; Linea " + str(line)
                    }
                    return render(request, 'index.html', context)
        except:
            context = {
                    'error' : "Por favor corrija los errores en los encabezados del csv de juegos mas vendidos"
                    }
            return render(request, 'index.html', context)
    
    xml = xmlManager.writeFromCsv(clientes, mejores, masVendidos, juegos)
    context ={
        'xml':xml
    }
    return render(request, 'index.html', context)

def procesar(request):
    url = api_dir.format('/procesarXml')
    xml = str(request.POST.get('mostrar_xml'))
    """string = str(xml)
    file = open('datos.xml', 'w')
    file.write(string)
    file.close() """
    reportes = requests.post(url, {
            'mostrar_xml':xml,
        })
    context = {
        'xml_reportes' : reportes.text,
        'xml' : xml
    }
    return render(request, 'index.html', context)


patronNombre ="^([A-Z]([A-Z]|[a-z]|á|é|í|ó|ú)+($| ))+"
patronEdad = "^[0-9]+$"
patronFecha = "^([0-9]{1}|[0-9]{2})/[0-1][0-9]/[0-9]{4}$"
patronCantidad = "^[0-9]+$"
patronMoneda = "^[0-9]+.[0-9]+$"
patronAnual = "^[0-9]{4}$"
patronClasificacion = "^(E|T|M)$"


def validarCadena(patron, cadena):
    return bool(re.search(patron, cadena))

def validarMoneda(cadena):
    
    return bool(re.search(patronMoneda, cadena))

