"""
URL configuration for UrbanDjango project.

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

from task2.views import ClassView, function_view
from task4.views import platform_view, game_view, cart_view
from UrbanDjango.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("function_view/", function_view),
    path("class_view/", ClassView.as_view()),
    path("platform/", platform_view),
    path("platform/games/", game_view),
    path("platform/cart/", cart_view),
]
