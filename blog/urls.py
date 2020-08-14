from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [ 
    path('', views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
    path('category/<int:pk>/', views.PostCategoryList.as_view(), name='post_category_list'),
    path('tag/<int:pk>/', views.PostTagList.as_view(), name='post_tag_list'),
]