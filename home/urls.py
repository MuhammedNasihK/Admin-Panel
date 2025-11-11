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
    path('block/<int:id>',views.block,name='block'),
    path('forgot/',views.otp_creation,name='otp_creation'),
    path('otp/',views.otp_verification,name='otp'),
    path('new_password/',views.new_password,name='new_password'),

]
