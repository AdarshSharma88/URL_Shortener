from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('hello',views.hello_world),
path('',views.home_page),
path('task',views.task) ,   
path('all-analytics',views.all_analytics),
path('analytics',views.analytics),
path('login', views.loginFunc),
path('register', views.registerFunc),
path('logout', views.logoutFunc),
path('<slug:short_url>',views.redirect_url),
path('<slug:short_url>/analytics', views.analytics),
#path('<slug:short_url>/analytics', analytics),
]
