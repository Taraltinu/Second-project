
from django.forms import ModelForm
from Eapp.modals.product import ProductModel


class Add_product_form(ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'