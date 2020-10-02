from django.shortcuts import render
from django.core.mail import EmailMessage
from Eapp.modals.registration import RegistrationModel


def sendemail(request):
    context = {}
    check = RegistrationModel.objects.filter(user__id=request.user.id)
    if len(check)>0:

        data = RegistrationModel.objects.get(user__id=request.user.id)
        context["data"]=data
    if request.POST:
        context ={}
        rec = request.POST['to']
        sub = request.POST['sub']
        msg = request.POST['msg']
        try:
            em = EmailMessage(sub,msg,to=[rec,])
            em.send()
            context['msg']="send msg"
            context['cls']="alert-success"

        except:
            context['msg']="Internet Connection problem"
            context['cls']="alert-danger"


    return render(request,"Eapp/sendemail.html",context)