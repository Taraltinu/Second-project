from django.contrib.auth.models import User
from Eapp.modals.registration import RegistrationModel
from django.shortcuts import render,redirect



def edit_profile(request):
    context = {}
    check = RegistrationModel.objects.filter(user__id=request.user.id)
    if len(check)>0:

        data = RegistrationModel.objects.get(user__id=request.user.id)
        context["data"]=data
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        uem = request.POST["email"]
        con = request.POST["ucon"]
        age = request.POST["uage"]
        city = request.POST["ucity"]
        gen = request.POST["ugen"]
        abt = request.POST["uabt"]
        occ = request.POST["uocc"]

        user = User.objects.get(id=request.user.id)
        user.first_name = fn
        user.last_name = ln
        user.email = uem
        user.save()
        data.contact=con
        data.age = age
        data.city=city
        data.gender=gen
        data.about=abt
        data.occupation=occ
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profil_pic = img
            data.save()

        context["stutas"] = "Changes Saved Succefully"
    return render(request,"Eapp/Edit_profile.html",context)
