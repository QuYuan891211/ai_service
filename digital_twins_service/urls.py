from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from digital_twins_service import views

urlpatterns = [
    # 将url关联到views中的方法
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)