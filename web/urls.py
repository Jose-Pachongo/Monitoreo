from django.contrib import admin
from django.urls import path
from monitoreo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('monitoreo/', views.monitoreo, name='monitoreo'),
    path('checklist/', views.checklist, name='checklist'),
    path('rappi/', views.rappi, name='rappi'),
    path('didi/', views.didi, name='didi'),
    path('siesa', views.siesa, name='siesa'),
    path('planta/', views.planta, name='planta'),
    
]
