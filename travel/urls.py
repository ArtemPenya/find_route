"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from routes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('trains/', include('trains.urls')),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete_route'),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='routes_detail'),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list'),

]
