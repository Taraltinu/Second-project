from django.shortcuts import render
from django.http import HttpResponse
from django.views import View









class About(View):
    def get(self,request):
        return render(request,'Eapp/about.html')