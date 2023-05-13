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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供 `list`，`create`，`retrieve`，`update`和`destroy`操作。

    另外我们还提供了一个额外的 `highlight` 操作。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # 这个装饰器可以用来添加任何不符合标准 create/update/delete 样式的自定义端点
    # 使用 @action 装饰器的自定义操作默认会响应 GET 请求。如果我们需要响应 POST 请求的操作，我们可以使用 methods 参数。
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlight)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     # 指定使用HTML渲染器去返回Response
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlight)
#
#
# # Create your views here.
# # 我们不再显式地将请求或响应绑定到给定的内容类型。request.data 可以处理传入的 json 请求，但它也可以处理其他格式。同样，我们返回带有数据的响应对象，但允许 REST framework 将响应渲染成正确的内容类型。
# # @csrf_exempt
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#
#     # 重写perform_create
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# # @csrf_exempt
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这个视图集自动提供 `list` 和 `detail` 操作。 （只读操作） 用户集不能被外部改动
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
