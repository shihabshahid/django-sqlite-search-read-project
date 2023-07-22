from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import product_table

# Create your views here.

def retrieve(request):
    if request.method=='POST':
        qty = Decimal(request.POST.get('quantity',''))
        Context={
            'datas':product_table.objects.filter(quantity__lte=qty)
        }
        return render(request,"retrieve.html",Context)
    elif request.method=='GET':
        Context={
            'datas':product_table.objects.all()
        }
        return render(request,"retrieve.html",Context)

    


