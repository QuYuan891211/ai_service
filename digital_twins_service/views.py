from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from digital_twins_service.models import Snippet
from digital_twins_service.serializers import SnippetSerializer


# Create your views here.
# 我们不再显式地将请求或响应绑定到给定的内容类型。request.data 可以处理传入的 json 请求，但它也可以处理其他格式。同样，我们返回带有数据的响应对象，但允许 REST framework 将响应渲染成正确的内容类型。
@csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    列出所有的代码 snippet，或创建一个新的 snippet。
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 此处使用函数视图形式
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    获取，更新或删除一个代码 snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
