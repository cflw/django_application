"""姜戈应用 URL Configuration

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
from django.urls import path, re_path
from django.views.static import serve
from 姜戈应用 import settings
import 知识库.views

urlpatterns = [
	re_path(r'^静态/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
	re_path(r'^媒体/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	path('管理/', admin.site.urls),
	path("知识库/", 知识库.views.f网页),
	path("知识库/<str:a名称>", 知识库.views.f网页),
]
