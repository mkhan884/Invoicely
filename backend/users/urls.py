from django.urls import path
from . import views

urlpatterns = [
    path('user/authenticate', views.authenticate, name='authenticate'),
    path('user/addUser', views.addUser, name='addUser'),
    path('user/<int:profile_id>/addCustomer/', views.addCustomer, name='addCustomer'),
    path('user/<int:profile_id>/getCustomers/', views.getCustomers, name='getCustomer'),
    path('user/<int:profile_id>/updateCustomer/', views.updateCustomer, name='editCustomer'),
    path('user/<int:profile_id>/deleteCustomer/', views.deleteCustomer, name='deleteCustomer'),
    path('user/<int:profile_id>/addBusiness/', views.addBusiness, name='addBusiness'),
    path('user/<int:profile_id>/getBusiness/', views.getBusiness, name='getBusiness')

]
