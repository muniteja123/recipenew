from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from . models import Menu
from django.http import HttpResponseRedirect

def index(request):
    context = Menu.objects.all()
    return render(request,'menu/index.html',{'context': context})

def detail(request, id):
    context = get_object_or_404(Menu,pk=id)
    return render(request, 'menu/detail.html',{'context': context})


def create(request):

    if request.method == 'POST':
        Menu.objects.create(
            name = request.POST['name'],
            ingrediants = request.POST['ingrediants'],
            process = request.POST['process'],
        )

        return HttpResponseRedirect(reverse('menu:index'))
    return render(request,'menu/create.html')

