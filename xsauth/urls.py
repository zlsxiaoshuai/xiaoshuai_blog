from django.urls import path
from . import views

app_name = "xsauth"

urlpatterns = [
    path('login', views.xslogin, name='login'),
    path('logout', views.xslogout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha',views.send_email_captcha,name='email_captcha')
]