from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {
        'nome': 'Vai tomar no cuzinho',
        'produtos': produtos,
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod,
    }

    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(template.render(), content_type='text/html; charset=utf8', status=500)