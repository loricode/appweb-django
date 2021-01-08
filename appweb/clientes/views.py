from django.shortcuts import render
from django.http import JsonResponse,request
from clientes.models import Cliente

def index(request):
    data =  list(Cliente.objects.values())
    return JsonResponse({ "clientes": data })

def add(request):
    data = request.POST.dict()
    print(data)
    nombre = data['nombre']
    apellido = data['apellido']
    celular = data['celular']
    Cliente.objects.create(nombre=nombre, apellido=apellido, celular=celular)
    return JsonResponse({ "msg": "agregado" })    


def deleteCliente(request, id):
    print(id)
    Cliente.objects.filter(id=id).delete()
    return JsonResponse({ "msg": "eliminado" }) 
