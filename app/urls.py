"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

app_name = 'app'

urlpatterns = [
    # 一覧画面
    path('', ItemFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('created/', ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]
