"""dotlearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from dot_learn_app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # path('/favicon.ico/ HTTP/1.1', favicon),
    path('',home),
    path('branch/<str:branch_slug>/',home,name="branch"),
    path('branch/<str:branch_slug>/subject/<str:subject_slug>/',home,name="branch+sub"),
    path('branch/<str:branch_slug>/subject/<str:subject_slug>/chapter/<str:chapter_slug>',home,name="branch+sub+chap"),
    path("topic/<str:topic_slug>/",home,name="branch+sub+chap+topic"),
    # path('temp/',temp),
]
