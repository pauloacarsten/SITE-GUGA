from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('cortes/', views.cortes, name='cortes'),
    path('cortes2/', views.cortes2, name='cortes2'),
    path('tatuagens/', views.tatuagens, name='tatuagens'),
    path('tatuagens2/', views.tatuagens2, name='tatuagens2'),
    path('desenhos/', views.desenhos, name='desenhos'),
    path('desenhos2/', views.desenhos2, name='desenhos2'),
    path('produto/', views.produto, name='produto'),
    path('produto2/', views.produto2, name='produto2'),
    path('contato/', views.contato, name='contato'),
    path('perfil/', views.perfil, name='perfil'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup', views.singup, name='singup'),
]
