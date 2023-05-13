from django.urls import path
from digital_twins_service import views

urlpatterns = [
    # 将url关联到views中的方法
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]