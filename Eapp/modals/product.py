from django.db import models
from django.contrib.auth.models import User
from Eapp.modals.category import CategoryModel




class ProductModel(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_Cat = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    product_price = models.CharField(max_length=10)
    sale_price = models.CharField(max_length=10)
    product_image = models.ImageField(upload_to="product/%y/%m/%d")
    description = models.TextField()
    quality = models.CharField(max_length=250,default="")
    size = models.FloatField( default=0)
    color = models.CharField(max_length=50,default="")
    add_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


