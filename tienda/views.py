from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Producto

class ProductoListView(generic.ListView):
    model = Producto
    template_name = "list.html"


