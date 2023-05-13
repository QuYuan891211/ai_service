from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from digital_twins_service import views

urlpatterns = [
    # 将url关联到views中的方法
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)