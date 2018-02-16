from django.shortcuts import render
from .models import Interface
from django.utils import timezone

def base(request):
    
    relays = Interface.objects.all().order_by('pin')
    return render(request, 'piwebapp/base.html', {'relays': relays})