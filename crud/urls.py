from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateCustomer.as_view(), name='create'),
    path('list/', views.GetCustomerDetalis.as_view(), name='list')
]
