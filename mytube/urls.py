from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='mytube_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='mytube_detail'),
    path('category/<str:slug>/', views.PostListByCategory.as_view(), name='category_list'),
]