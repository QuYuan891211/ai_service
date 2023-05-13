from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from digital_twins_service.models import Snippet
from digital_twins_service.serializers import SnippetSerializer


# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    列出所有的代码 snippet，或创建一个新的 snippet。
    """
    if request.method == 'GET':
        #查询所有

        snippets = Snippet.objects.all()
        # 查询数据库获取对象，转回为到python原生类型，再将原生类型转换为JSON对象
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 创建

        # 现将请求解析为一个python原生的类型
        data = JSONParser().parse(request)
        # python原生的类型反序列化，获得一个对象实例
        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    获取，更新或删除一个代码 snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # 查询1个
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # 更新

        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # 删除

        snippet.delete()
        return HttpResponse(status=204)
