"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
#code for video 3 above from site https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mynm/', views.myname, name = 'myname'),
    path('mysnm/', views.surname, name = 'surname'),
    path('tfile1/', views.tfile1, name = 'tfile1'),
    path('tfile2/', views.tfile2, name = 'tfile2'),
    path('nav/', views.nav, name = 'nav'),
    path('ulti/', views.ulti, name = 'ulti')
]
'''
'''#this is comment for code with harry site till video #9
#laying the pipeline
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rmpunc/', views.rmpunc, name = 'Remove punctuations'),
    path('rmspace/', views.rmspace, name = 'Eemove spaces'),
    path('cap1st/', views.cap1st, name = 'Captalize First'),
    path('rmnewln/', views.rmnewln, name = 'Remove New Line'),
    path('countchar/', views.countchar, name = 'Characters Count'),

]

'''

#video #10 starts - templates
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
]
