from django.shortcuts import render
import requests
# Create your views here.

api_dir = 'http://localhost:5000{}'

def index(request):
    return render(request, 'index.html')

def revisar(request):
    if request.method == 'POST':
        docs = request.FILES
        """ for doc in docs.values():
            print(doc.read()) """
        #print(docs)
    return render(request, 'index.html')