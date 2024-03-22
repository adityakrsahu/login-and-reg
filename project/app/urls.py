from django.urls import path
from .views import home,register,data,login

urlpatterns = [
    path('',home,name='home'),
    path('regeister',register,name='regeister'),
    path('data/',data,name='data'),
    path('login',login,name='login')
]