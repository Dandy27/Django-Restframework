from django.contrib import admin
from django.urls import path
from contas.views import home, listagem 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem),
    path('home', home)
]
