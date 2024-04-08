from django.urls import path
from . import views

urlpatterns = [
    path('user/authenticate', views.authenticate, name='authenticate'),
    path('user/addUser', views.addUser, name='addUser')
]
