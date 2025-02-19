from django.urls import path
from .views import register, login, logout, user_details

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('user/', user_details),
]
