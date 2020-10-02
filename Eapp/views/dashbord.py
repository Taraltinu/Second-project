from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from Eapp.modals.registration import RegistrationModel





class DashBord(View):
    @method_decorator(login_required)
    def get(self,request):
        context ={}
        data = RegistrationModel.objects.get(user__id=request.user.id)
        context["data"]=data
        return render(request,'Eapp/dashbord.html',context)



# class CustomerDash(View):
#     @method_decorator(login_required)
#     def get(self,request):
#         return render(request,"Eapp/Costemer_dashbord.html")