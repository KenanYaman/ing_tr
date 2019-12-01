from django.http import HttpResponse
from django.shortcuts import render
from sozluk.models import eng_tr
# Create your views here.

def anasayfa(request,*args, **kwargs):
    obj = eng_tr.objects.all()
    context = {
        'eng_tr': obj
    }
    return render(request, "anasayfa.html", context,  {'nbar': 'home'})


def hakkinda(request,*args, **kwargs):
    my_context = {
    }
    return render(request, "hakkinda.html", my_context,{'nbar': 'hakkinda'})


def zamanlar(request,*args, **kwargs):
    my_context = {
    }
    return render(request, "zamanlar.html", my_context,{'nbar': 'zamanlar'})

