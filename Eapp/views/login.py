from django.shortcuts import render ,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect



def loginform(request):
    if request.method == "POST":
        en = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=en,password=password)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/dashbord")
            # if user.is_active:
            #     return HttpResponseRedirect("/seller")
        else:
            return redirect('login')
        return HttpResponse(user)
        
    
    return render(request,'Eapp/login.html')
def logoutform(request):
    logout(request)
    return HttpResponseRedirect('/')