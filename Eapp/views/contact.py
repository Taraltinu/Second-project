from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from Eapp.modals.contact import Contact





class ContactViews(View):
    def get(self,request):
        feedback =Contact.objects.all().order_by('-id')[:5]
        return render(request,'Eapp/contact.html',{'feedback':feedback})
    def post(self, request):
        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(fullname = fullname,mobile=mobile,subject=subject,message=message)
        data.save()
        return redirect('home')


