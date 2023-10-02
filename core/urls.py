from django.urls import path
from . import views
from django.contrib.auth import views as av

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', av.LoginView.as_view(template_name='core/login.html'), name='login'),
    
]
