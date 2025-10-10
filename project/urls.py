"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

print('from urls.py')
from django.contrib import admin
from django.urls import path 
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/<int:pk>/', views.home, name='home',),
    
    path('home1/<str:pk>/', views.home1, name='home1',),
    path('home2/<slug:pk>/', views.home2, name='home2',),
    #   path('home3/', views.home3, name='home',),
       path('home4/', views.home4, name='home4',),
        path('home5/', views.home5, name='home5',),
]

