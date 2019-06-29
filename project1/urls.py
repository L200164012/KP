"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# additionals
import c0tracerstudy.views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home_view , name='home'),
    path('graph1', view.view_graph1, name='graph1'),
    path('graph2', view.view_graph2, name='graph2'),
    path('graph3', view.view_graph3, name='graph3'),
    path('graph4', view.view_graph4, name='graph4'),
    path('graph5', view.view_graph5, name='graph5'),
    path('graph6', view.view_graph6, name='graph6'),
    path('graph7', view.view_graph7, name='graph7'),
    path('graph8', view.view_graph8, name='graph8'),
    path('graph9', view.view_graph9, name='graph9'),
    path('graph10', view.view_graph10, name='graph10'),
    path('graph11', view.view_graph11, name='graph11'),
]
