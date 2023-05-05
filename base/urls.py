from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('allmyproducts',views.allMyProducts),
    path('mycomputers',views.myComputers),
    path('myphones',views.myPhones),
    path('login/', views.login_view, name='login'), 
  # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),

    
    # path('profile/', profile, name='profile'),
    path('token/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),


]
