"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views as core_views

urlpatterns=[
    path('admin/', admin.site.urls),
    path("", core_views.listing, name="listing"),
    path("view_blog/<int:blog_id>/", core_views.view_blog, name="view_blog"),
    path("see_request/", core_views.see_request),
    path("user_info/", core_views.user_info),
    path("private_place", core_views.private_place),
    path("accounts/", include("django.contrib.auth.urls")),
    path("staff_place/", core_views.staff_place),
    path("add_messages/", core_views.add_messages),

]