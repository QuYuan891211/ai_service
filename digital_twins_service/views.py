from django.http import Http404
from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from digital_twins_service.models import Snippet
from digital_twins_service.permissions import IsOwnerOrReadOnly
from digital_twins_service.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
# 我们不再显式地将请求或响应绑定到给定的内容类型。request.data 可以处理传入的 json 请求，但它也可以处理其他格式。同样，我们返回带有数据的响应对象，但允许 REST framework 将响应渲染成正确的内容类型。
# @csrf_exempt
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # 重写perform_create
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @csrf_exempt
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
