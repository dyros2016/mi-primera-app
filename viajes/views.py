from django.shortcuts import render
from django.utils import timezone
from .models import Material,Vehiculo,Chofer,Proveedor,Orden
from .forms import MaterialForm,VehiculoForm,ChoferForm, ProveedorForm, OrdenForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
  saludo ="Bienvenido %s" %(request.user)
  context = {
  "saludo":saludo,
  }
  return render(request, 'viajes/index.html',context)

def materiales_list(request):
 materiales = Material.objects.order_by('nombre')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de materiales"
 context = {
  "titulo":titulo,
  "saludo":saludo,
	"materiales": materiales
  }
 return render(request, 'viajes/materiales_list.html',context)

def materiales_ledit(request):
  materiales = Material.objects.order_by('nombre')
  saludo ="Bienvenido %s" %(request.user)
  titulo="Lista de materiales Editable"
  context = {
  "titulo":titulo,
  "saludo":saludo,
  "materiales": materiales
  }
  return render(request, 'viajes/materiales_ledit.html',context)

def material_nuevo(request):

 if request.user.is_authenticated():
  saludo="Bienvenido %s" %(request.user)
  titulo ="NUEVO MATERIAL"
 form = MaterialForm(request.POST or None) 
 context = {
   "saludo":saludo,
   "titulo":titulo,
   "form":form
   } 
 if form.is_valid():
   material = form.save(commit=False)
   material.save()
   return render(request,'viajes/index.html',context)
 else:
   form = MaterialForm()
   context = {
   "saludo":saludo,
     "titulo":titulo,
     "form":form
    } 
   return render(request,'viajes/material_nuevo.html',context)

def material_edit(request, pk):
    saludo="Bienvenido %s" %(request.user)
    titulo ="EDITAR MATERIAL"
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        context = {
          "saludo":saludo,
          "titulo":titulo,
          "form":form
         }
        if form.is_valid():
            material = form.save(commit=False)
            material.save()
            return render(request,'viajes/index.html',context)
    else:
        form = MaterialForm(instance=material)
        context = {
        "saludo":saludo,
        "titulo":titulo,
        "form":form
         } 
    return render(request, 'viajes/material_edit.html', context)
    #---------------------------------------------------------------------------------------
def vehiculos_list(request):
 vehiculos = Vehiculo.objects.order_by('placa')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de vehiculos"
 context = {
  "titulo":titulo,
  "saludo":saludo,
  "vehiculos": vehiculos
  }
 return render(request, 'viajes/vehiculos_list.html',context)

def vehiculos_ledit(request):
  vehiculos = Vehiculo.objects.order_by('placa')
  saludo ="Bienvenido %s" %(request.user)
  titulo="Lista de Vehiculos Editable"
  context = {
  "titulo":titulo,
  "saludo":saludo,
  "vehiculos": vehiculos
  }
  return render(request, 'viajes/vehiculos_ledit.html',context)

def vehiculo_nuevo(request):

 if request.user.is_authenticated():
  saludo="Bienvenido %s" %(request.user)
  titulo ="NUEVO VEHICULO"
 form = VehiculoForm(request.POST or None) 
 context = {
   "saludo":saludo,
   "titulo":titulo,
   "form":form
   } 
 if form.is_valid():
   vehiculo = form.save(commit=False)
   vehiculo.save()
   return render(request,'viajes/index.html',context)
 else:
   form = VehiculoForm()
   context = {
   "saludo":saludo,
     "titulo":titulo,
     "form":form
    } 
   return render(request,'viajes/vehiculo_nuevo.html',context)

def vehiculo_edit(request, pk):
    saludo="Bienvenido %s" %(request.user)
    titulo ="EDITAR VEHICULO"
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        context = {
          "saludo":saludo,
          "titulo":titulo,
          "form":form
         }
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.save()
            return render(request,'viajes/index.html',context)
    else:
        form = VehiculoForm(instance=vehiculo)
        context = {
        "saludo":saludo,
        "titulo":titulo,
        "form":form
         } 
    return render(request, 'viajes/vehiculo_edit.html', context)

#---------------------------------------------------------------------------------------
def choferes_list(request):
 choferes = Chofer.objects.order_by('nombre')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de Choferes"
 context = {
  "titulo":titulo,
  "saludo":saludo,
  "choferes": choferes
  }
 return render(request, 'viajes/choferes_list.html',context)

def choferes_ledit(request):
 choferes = Chofer.objects.order_by('nombre')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de Choferes"
 context = {
  "titulo":titulo,
  "saludo":saludo,
  "choferes": choferes
  }
 return render(request, 'viajes/choferes_ledit.html',context)

def chofer_nuevo(request):

 if request.user.is_authenticated():
  saludo="Bienvenido %s" %(request.user)
  titulo ="NUEVO CHOFER"
 form1 = ChoferForm(request.POST or None) 
 context = {
   "saludo":saludo,
   "titulo":titulo,
   "form1":form1
   } 
 if form1.is_valid():
   chofer = form1.save(commit=False)
   chofer.save()
   return render(request,'viajes/index.html',context)
 else:
   form1 = ChoferForm()
   context = {
   "saludo":saludo,
     "titulo":titulo,
     "form1":form1
    } 
   return render(request,'viajes/chofer_nuevo.html',context)

def chofer_edit(request, pk):
    saludo="Bienvenido %s" %(request.user)
    titulo ="EDITAR CHOFER"
    chofer = get_object_or_404(Chofer, pk=pk)
    if request.method == "POST":
        form = ChoferForm(request.POST, instance=chofer)
        context = {
          "saludo":saludo,
          "titulo":titulo,
          "form":form
         }
        if form.is_valid():
            chofer = form.save(commit=False)
            chofer.save()
            return render(request,'viajes/index.html',context)
    else:
        form = ChoferForm(instance=chofer)
        context = {
        "saludo":saludo,
        "titulo":titulo,
        "form":form
         } 
    return render(request, 'viajes/chofer_edit.html', context)



    #---------------------------------------------------------------------------------------
def proveedores_list(request):
 proveedores = Proveedor.objects.order_by('nombre')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de Proveedores"
 context = {
  "titulo":titulo,
  "saludo":saludo,
  "proveedores": proveedores
  }
 return render(request, 'viajes/proveedores_list.html',context)

def proveedores_ledit(request):
 proveedores = Proveedor.objects.order_by('nombre')
 saludo ="Bienvenido %s" %(request.user)
 titulo="Lista de Provedores"
 context = {
  "titulo":titulo,
  "saludo":saludo,
  "proveedores": proveedores
  }
 return render(request, 'viajes/proveedores_ledit.html',context)

def proveedor_nuevo(request):

 if request.user.is_authenticated():
  saludo="Bienvenido %s" %(request.user)
  titulo ="NUEVO PROVEEDOR"
 form1 = ProveedorForm(request.POST or None) 
 context = {
   "saludo":saludo,
   "titulo":titulo,
   "form1":form1
   } 
 if form1.is_valid():
   proveedor = form1.save(commit=False)
   proveedor.save()
   return render(request,'viajes/index.html',context)
 else:
   form1 = ProveedorForm()
   context = {
   "saludo":saludo,
     "titulo":titulo,
     "form1":form1
    } 
   return render(request,'viajes/proveedor_nuevo.html',context)

def proveedor_edit(request, pk):
    saludo="Bienvenido %s" %(request.user)
    titulo ="EDITAR PROVEEDOR"
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        context = {
          "saludo":saludo,
          "titulo":titulo,
          "form":form
         }
        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.save()
            return render(request,'viajes/index.html',context)
    else:
        form = ProveedorForm(instance=proveedor)
        context = {
        "saludo":saludo,
        "titulo":titulo,
        "form":form
         } 
    return render(request, 'viajes/proveedor_edit.html', context)

#Orden de Recepcion

def orden_nuevo(request):

 if request.user.is_authenticated():
  saludo="Bienvenido %s" %(request.user)
  titulo ="NUEVA ORDEN"
  form1 = OrdenForm(request.POST or None) 
  context = {
   "saludo":saludo,
   "titulo":titulo,
   "form1":form1
   } 
 if form1.is_valid():
   orden = form1.save(commit=False)
   orden.save()
   return render(request,'viajes/index.html',context)
 else:
   form1 = OrdenForm()
   context = {
   "saludo":saludo,
     "titulo":titulo,
     "form1":form1
    } 
   return render(request,'viajes/orden_nuevo.html',context)