from django.urls import path
from .views import about ,contact,home,registration,check_user,base,login,dashbord,edit_profile,change_password,add_product
from .views import send_email
from .views import reset_pass
from .views import cart


urlpatterns = [

    path('',home.Home.as_view(),name='home'),
    path('about/',about.About.as_view(),name='about'),
    path('conatct/',contact.ContactViews.as_view(),name='contact'),
    path('registration/',registration.RegistrationView.as_view(),name='registration'),
    path('check_user/',check_user.check_user,name="check_user"),
    path('base/',base.BaseView.as_view(),name="base"),
    path('login/',login.loginform,name="login"),
    path('logout/',login.logoutform,name="logout"),
    path('cpass/',change_password.ChangePassword.as_view(),name="cpass"),
    path('dashbord/',dashbord.DashBord.as_view(),name="dashbord"),
    # path('customer/',dashbord.CustomerDash.as_view(),name="customer"),
    path('profile/',edit_profile.edit_profile,name="profile"),
    path('add_product/',add_product.add_product_view,name="add_product"),
    path('my_product/',add_product.my_product,name="my_product"),
    path('single_product/',add_product.single_product,name="single_product"),
    path('update_product/',add_product.update_product,name="update_product"),
    path('delete_product/',add_product.delete_product,name="delete_product"),
    path('sendemail/',send_email.sendemail,name="sendemail"),
    # path('forggatepassword/',forggatepassword.forggatepassword,name="forggatepassword"),
    # path('resetpass/',forggatepassword.resetpass,name="resetpass"),
    path('resetpass/',reset_pass.resetpass,name="resetpass"),
    path('add_to_cart/',cart.add_to_cart,name="add_to_cart"),
    path('get_cart_data/',cart.get_cart_data,name="get_cart_data"),

    




    


    




]