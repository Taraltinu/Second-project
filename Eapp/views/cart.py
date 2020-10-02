from Eapp.modals.cart import Cart
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Eapp.modals.product import ProductModel
from Eapp.modals.cart import Cart
from django.http import JsonResponse

def add_to_cart(request):
    context = {}
    items = Cart.objects.filter(user__id=request.user.id,status=False)
    context['items']=items
    if request.user.is_authenticated:
        if request.method=="POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = Cart.objects.filter(product__id=pid,user__id=request.user.id,status=False)
            if len(is_exist)>0:
                context["msg"]= "item already exist"
                context["cls"]= "alert-warning"

            else:

                product = get_object_or_404(ProductModel,id=pid)
                usr = get_object_or_404(User,id=request.user.id)
                c = Cart(user=usr,product=product,quentity=qty)
                c.save()
                context["msg"]= "{} Added".format(ProductModel.product_name)
                context["cls"]= "alert-success"

        else:
            pass
            


            

    else:
        context["msg"] = "please login "
        
    return render(request,"Eapp/cart.html",context)

def get_cart_data(request):
    items = Cart.objects.filter(user__id=request.user.id,status=False)
    sale,total,qauntity = 0,0,0
    for i in items:
        print(i.product.product_price)
        sale += float(i.product.sale_price)
        total += float(i.product.product_price)
        qauntity += float(i.quentity)
    res = {
        'total':total,'offer':sale,'quan':qauntity,
    
    }
    return JsonResponse(res)
