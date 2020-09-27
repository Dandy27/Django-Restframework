from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, nova_transacao 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name='url_listagem'),
    path('nova/', nova_transacao, name='url_nova'),
    path('home/', home)

]
