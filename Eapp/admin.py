from django.contrib import admin
from .modals.category import CategoryModel
from .modals.registration import RegistrationModel
from .modals.product import ProductModel
from .modals.cart import Cart


# Register your models here.
from .modals.contact import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','fullname','mobile','subject','message','on_add']
    search_fields = ['fullname','subject']
    list_filter = ['on_add']
admin.site.register(Contact,ContactAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','cover_pic','description','date_add']
    search_fields = ['name',]
    list_filter = ['date_add']
admin.site.register(CategoryModel,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','seller','product_name','product_Cat','product_price','sale_price','product_image']
    search_fields = ['seller','product_name','product_Cat']
    list_filter = ['product_Cat']
admin.site.register(ProductModel,ProductAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    # list_display = 
    search_fields = ['username','email']
    # list_filter = ['date_add']
admin.site.register(RegistrationModel,RegistrationAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quentity','status','added_on','update_on']
    search_fields = ['user','product']
    list_filter = ['added_on']
admin.site.register(Cart,CartAdmin)