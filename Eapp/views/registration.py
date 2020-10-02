from django.shortcuts import redirect,render
from django.views import View
from Eapp.modals.registration import RegistrationModel
from django.contrib.auth.models import User






class RegistrationView(View):
    def get(self,request):
        return render(request,'Eapp/registration.html')

    def post(self,request):
        fn = request.POST['f_name']
        ln = request.POST['l_name']
        un = request.POST['u_name']
        em = request.POST['email']
        pw = request.POST['password']
        con = request.POST['contact']
        tp = request.POST['type']
        user = User.objects.create_user(un,em,pw)
        user.first_name =fn
        user.last_name = ln
        if tp == 'sel':
            user.is_staff = True

        user.save()

        reg = RegistrationModel(contact=con,user=user)
        reg.save()

       

        return render(request,'Eapp/index.html')