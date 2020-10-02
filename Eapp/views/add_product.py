from Eapp.modals.product import ProductModel
from Eapp.modals.category import CategoryModel
from django.shortcuts import render,redirect
from Eapp.forms import Add_product_form

def add_product_view(request):
    context= {}
    form = Add_product_form()
    context["form"]=form
    if request.method=="POST":
        form = Add_product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context["msg"]="Saved succesfully !!"
            return redirect("/dashbord")
        else:
            context["msg"]="Saved unsuccesfully !!"
            
    return render(request,"Eapp/add_product.html",context)
def my_product(request):
    pd = ProductModel.objects.filter(seller__id=request.user.id)
    return render(request,"Eapp/my_product.html",{"product":pd})

def single_product(request):
    context ={}
    spd = request.GET["pid"]
    pdid = ProductModel.objects.get(id=spd)
    context["product"]=pdid
    return render(request,"Eapp/single_product.html",context)

def update_product(request):
    context={}
    ct = CategoryModel.objects.all().order_by("name")
    spd = request.GET["uid"]
    products = ProductModel.objects.get(id=spd)
    if request.method == "POST":
        pn = request.POST["pdn"]
        cn = request.POST["pcn"]
        pp = request.POST["price"]
        spp = request.POST["sprice"]
        pc = request.POST["color"]
        ps = request.POST["size"]
        pq = request.POST["quality"]
        pd = request.POST["desc"]
        ctn = CategoryModel.objects.get(id=cn)
        products.product_name=pn
        products.product_Cat=ctn

        products.product_price=pp
        products.sale_price=spp
        products.color=pc
        products.size = ps
        products.quality=pq
        products.description=pd
        if "pimg" in request.FILES:
            img = request.FILES["pimg"]
            products.product_image=img
        products.save()
        context["msg"]="Changes Successfully Updated !!!"


    context["product"]=products
    context["category"]=ct
    return render(request,"Eapp/update_product.html",context)
def delete_product(request):
    spd = request.GET["pid"]
    pdid = ProductModel.objects.get(id=spd)
    pdid.delete()
    return redirect("/my_product")