from django.shortcuts import render, render_to_response
from htmlpublic.models import *
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from htmlpublic.forms import EnlaceForm
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.all()
    template = "index.html"
    #diccionario = {"categorias":categorias, "enlaces":enlaces}
    return render_to_response(template,locals())
def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, pk = id_categoria)
    #cat = Categoria.objects.all(pk = id_categoria)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render_to_response(template,locals())
@login_required
def add(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        form = EnlaceForm(request.POST)
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.save()
            return HttpResponseRedirect("/")
    else:
        form = EnlaceForm()
        #template = "form.html"
        #return render(request,template,context_instance=RequestContext(request,locals()))
    return render_to_response("form.html",context_instance=RequestContext(request,locals()))
        #return render_to_response(template, {'form': form},context_instance=RequestContext(request))
        #return render_to_response('form.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def minus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def plus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect("/")