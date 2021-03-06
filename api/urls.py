"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from rest_framework_jwt import views

from api import viewsets

router = routers.SimpleRouter()
router.register('users', viewsets.UserViewSet)
router.register('notes', viewsets.NoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^me/', viewsets.whoami),
    url(r'^api-token-auth/', views.obtain_jwt_token, name='api-auth'),
    url(r'^api-token-verify/', views.verify_jwt_token, name='verify-auth-token'),
    url(r'^docs/', include_docs_urls(title='Notes API')),
]
