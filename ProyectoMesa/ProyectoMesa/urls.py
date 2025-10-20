from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from Mesa_de_Ayuda.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include('Mesa_de_Ayuda.urls'))
]
