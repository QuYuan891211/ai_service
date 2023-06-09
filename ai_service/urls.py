"""ai_service URL Configuration

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
from django.template.defaulttags import url
from django.urls import include, path

from polls import test

urlpatterns = [
    # 函数 include() 允许引用其它 URLconfs。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

    path('admin/', admin.site.urls),
    path('', include('digital_twins_service.urls')),
    # path('users/', include('digital_twins_service.urls')),
    path('polls/', include('polls.urls')),
    # 测试使用
    # path('polls/query/',test.query)  # 访问的是polls应用的tests文件下的querry对象
    # url(r'api-auth/', include('rest_framework.urls')),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
