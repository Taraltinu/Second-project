from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User




class ChangePassword(View):
    def get(self,request):
        return render(request,"Eapp/change_password.html")
    def post(self,request):
        context = {}
        old_pass = request.POST["old_pass"]
        new_pass = request.POST["new_pass"]
        user =  User.objects.get(id=request.user.id)
        check =  user.check_password(old_pass)
        if check ==True:
            user.set_password(new_pass)
            context["msg"] = "Password Changes succesFully !!!!"
        else:
            context["error"]= "Incurrect Old Password!!!!"
        return render(request,"Eapp/change_password.html",context)
