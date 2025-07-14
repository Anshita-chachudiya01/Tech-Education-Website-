"""
URL configuration for mytask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from mytask import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('about/',views.about),
    path('Course/',views.Course),
    path('registration/',views.registration),
    path('UserForm/',views.UserForm),
    path('Submitform/',views.Submitform),
    path('calculator/',views.calculator),
    path('evenodd/',views.evenodd),
    path('newsDetails/<newsid>',views.newsDetails),
    path('placement/',views.placement,name='placement'),
    path('login/',views.login,name='login')
]
