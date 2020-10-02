from django.shortcuts import render
from Eapp.modals.category import CategoryModel
from django.views import View



class BaseView(View):
    def get(self ,request):
        context ={}
        cat = CategoryModel.objects.all().order_by('name')
        data = RegistrationModel.objects.get(user__id=request.user.id)
        context["cotegory"]=cat
        context["data"]=data
        return render(request,'Eapp/base.html',data)

 
       