from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from crud.forms import CreateCustomerForm
from crud.models import Customer
from django.urls import reverse_lazy
# Create your views here.


class IndexView(TemplateView):
    template_name = 'crud/index.html'


class CreateCustomer(CreateView):
    model = Customer
    template_name = 'crud/create.html'
    form_class = CreateCustomerForm
    success_url = reverse_lazy('index')


class GetCustomerDetalis(ListView):
    model = Customer
    template_name = 'crud/list.html'
