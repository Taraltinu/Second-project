from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Eapp.modals.category import CategoryModel
from Eapp.modals.product import ProductModel
from django.db.models import Q

class Home(View):
    def get(self,request):
        context={}
        cat = CategoryModel.objects.all()
        pd = ProductModel.objects.all().order_by('product_name')
        context["ct"]=cat
        context["product"]=pd
        if "search" in request.GET:
            sr = request.GET["search"]
            pdc = ProductModel.objects.filter(Q(product_name__icontains=sr)|Q(product_Cat__name__contains=sr))
            context["product"]=pdc
        else:
            context["msg"]="Sorry This product are not found"
        if "price" in request.GET:
            pp = request.GET["price"]
            pdc = ProductModel.objects.filter(sale_price__lt=pp)
            context["product"]=pdc
        else:
            context["msg"]="Sorry This product are not found"
        return render(request,'Eapp/index.html',context)