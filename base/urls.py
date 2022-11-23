from django.urls import path
from  . import views

urlpatterns= [
  path('', views.home, name="home"),
  path('podashboard/', views.podashboard, name="podashboard"),
  path("login/", views.loginPage, name="login"),
  path('logout/', views.custom_logout, name='logout'),
]