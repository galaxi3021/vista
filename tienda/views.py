from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Producto

class ProductoListView(generic.ListView):
    model = Producto
    template_name = "list.html"



class ProductoDetailView(generic.DetailView):
    model = Producto
    template_name = "detail.html"



class ProductoCreateView(generic.CreateView):
    model = Producto
    fields='__all__'
    template_name = "form.html"


class ProductoUpdateView(generic.UpdateView):
    model = Producto
    fields='__all__'
    template_name = "form.html"


class ProductoDeleteView(generic.DeleteView):
    model = Producto
    template_name = "delete.html"
    success_url = reverse_lazy('tienda:index')



