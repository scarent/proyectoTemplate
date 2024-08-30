from django.shortcuts import render

# Create your views here.

def rendertemplate(request):
    return render(request,'appTemplate/holamundo.html') #nombreapp/archivohtml

def saludojorge(request):
    data={"nombre" : "Jorge"}
    return render(request,'appTemplate/holapol.html',data)

def infoUsuario(request):
    datausuario = {"ID" :123, "Nombre" : "Clark Kent", "Email": "superman@jl.org"}
    return render(request,'appTemplate/infousuario.html',datausuario)

