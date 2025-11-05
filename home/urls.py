from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.register,name='register'),
    path('admin/',views.admin,name='admin'),
    path('add_user/',views.add_user,name='add_user'),
    path('logoutadmin/',views.logout,name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('dalete/<int:id>',views.delete,name='delete'),
]
