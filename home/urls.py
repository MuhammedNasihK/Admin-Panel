from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginv,name='login'),
    path('',views.register,name='register'),
    path('admin_panel',views.admin,name='admin')
]
