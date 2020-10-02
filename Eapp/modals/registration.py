from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User



class RegistrationModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.IntegerField()
    on_add = models.DateTimeField(auto_now_add=True)
    profil_pic = models.ImageField(upload_to="profile/%y/%m/%d",blank=True,null=True)
    age = models.CharField(max_length=250,blank=True,null=True)
    city = models.CharField(max_length=250,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=6,blank=True,null=True)
    occupation = models.CharField(max_length=250,blank=True,null=True)
    added_on = models.DateTimeField(auto_now=True,blank=True,null=True)
    update_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)


    # def __str__(self):
    #     return self.user.username

    