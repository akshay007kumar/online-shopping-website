from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:id>', views.user_profile, name='profile'),

    path('changePassword/<int:id>',
         views.change_password, name='change-password')
]
