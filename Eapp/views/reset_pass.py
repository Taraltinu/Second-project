from django.shortcuts import redirect,get_object_or_404,render
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def resetpass(request):
    print(request.POST)
    un = request.POST.get("username")


    return render(request,"Eapp/reset_pass.html")