from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from digital_twins_service import views

urlpatterns = [
    # 将url关联到views中的方法
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)