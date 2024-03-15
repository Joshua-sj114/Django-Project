from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import User,Product


# Create your views here.
def myapp(request):
    myusers = User.objects.all().values()
    products = Product.objects.all().values()
    template = loader.get_template("index.html")
    context={
        'userlist': myusers,
        'products': products

    }
    
    return HttpResponse(template.render(context,request))

def prod_details(request,id):
    product=Product.objects.get(product_id=id)
    template = loader.get_template("prod_details.html")
    context={
        "product":product,
    }
    return HttpResponse(template.render(context,request))