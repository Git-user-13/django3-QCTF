"""
URL configuration for ctf_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.SignupPage,name='signup'),
    path('',views.IndexPage,name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('index/',views.IndexPage,name='index'),
    path('addProduct/', views.addProduct,name='addProduct'),
    path('addhint/<int:pk>', views.addhint,name='addhint'),
    path('showProducts/',views.ShowAllProducts,name='showProducts'),
    path('product/<int:pk>/', views.productDetail,name='product'),
    path('updateProduct/<int:pk>/', views.updateProduct,name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct,name='deleteProduct'),
    path('updateHint/<int:pk>/', views.updateHint, name= 'updateHint'),
    path('deleteHint/<int:pk>/', views.deleteHint, name= 'deleteHint'),
    path('showQuests/',views.ShowAllQuests,name='showQuests'),
    path('quest/<int:pk>/', views.questDetail,name='quest'),
    path('addFlag/<int:pk>/', views.addFlag,name='addFlag'),
    path('leaderboard/', views.leaderboard,name='leaderboard'),
    path('profile/', views.profile,name='profile'),
    path('finish/<int:pk>', views.finish,name='finish'),

]
