from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('inserirRegistro/', views.inserirRegistro),
    path('editarRegistro/<int:id_registro>', views.editarRegistro),
    path('deletarRegistro/<int:id_registro>', views.deletarRegistro),
    path('alterarRegistro/<int:id_registro>', views.alterarRegistro),
]