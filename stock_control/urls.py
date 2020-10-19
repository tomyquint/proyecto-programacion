from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<pk>/borrar/', views.borrar_producto, name='borrar_producto'),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/registro_completo', views.registro_completo, name="registro_completo"),
    path('accounts/login_superuser/', views.login_superuser, name="login_superuser"),
    path('accounts/', views.lista_usuarios, name="lista_usuarios"),
    path('accounts/<username>/borrar/', views.borrar_usuario, name="borrar_usuario"),
    path('categorías/', views.lista_categorías, name="lista_categorías"),
    path('categorías/nueva', views.categoría_nueva, name='categoría_nueva'),
    path('categorías/<pk>/borrar/', views.borrar_categoría, name="borrar_categoría"),
]
