from django.urls import path 

from . import views

app_name = "tienda"
urlpatterns = [
    path("", views.ProductoListView.as_view(), name="index"),
    path("<int:pk>/", views.ProductoDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.ProductoUpdateView.as_view(), name="update"),
    path("create", views.ProductoCreateView.as_view(), name="create"),
    path("<int:pk>/delete", views.ProductoDeleteView.as_view(), name="delete"),
]