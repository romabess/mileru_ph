from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('auth/', pass_page, name="pass_page"),
    path('success/', success_page, name="success_page"),
    path("loger/", loger, name="loger"),
    
]
