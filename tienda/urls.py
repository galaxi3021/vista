from django.urls import path 

from . import views

app_name = "tienda"
urlpatterns = [
    path("", views.ProductoListView.as_view(), name="index"),
]