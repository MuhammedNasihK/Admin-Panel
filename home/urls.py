from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginv,name='login'),
    path('',views.register,name='register'),
    path('admin_panel',views.admin,name='admin'),
    path('add_user',views.add_user,name='add_user')
]
