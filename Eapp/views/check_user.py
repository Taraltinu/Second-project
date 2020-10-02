from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse



def check_user(request):
    if request.method == "GET":
        em = request.GET["email"]
        check = User.objects.filter(email=em)
        if len(check) == 1:
            return HttpResponse("exist")
        else:
            return HttpResponse("not Exist")
        

        return HttpResponse(check)