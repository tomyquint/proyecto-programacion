from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('accounts/signup/', views.signup, name="signup"),
]
